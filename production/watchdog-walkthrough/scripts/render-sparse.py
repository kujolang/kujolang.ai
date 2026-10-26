#!/usr/bin/env python3
"""Render every changing 30 fps frame with Hyperframes; hold identical frames via FFmpeg.

This film contains only static images/text and explicit finite GSAP camera/opacity
moves. Captions and scene boundaries are sampled on the exact output frame grid.
No animation frames are dropped. Unsupported new motion requires the normal renderer.
"""
import concurrent.futures,hashlib,json,math,os,pathlib,re,shutil,subprocess
P=pathlib.Path(__file__).resolve().parents[1];OUT=P/'output/sparse';OUT.mkdir(parents=True,exist_ok=True)
visual_files=[P/'index.html',*sorted((P/'compositions').glob('*.html')),*sorted((P/'assets/screens').glob('*.png')),*sorted((P/'assets/screens').glob('*.jpg')),*sorted((P/'assets/fonts').glob('*'))]
fingerprint=hashlib.sha256(b''.join(str(f.relative_to(P)).encode()+f.read_bytes() for f in visual_files)).hexdigest()
chapters=json.loads((P/'timing.json').read_text());fps=30;duration=float(re.search(r'data-duration="([\d.]+)"',(P/'index.html').read_text()).group(1));total=math.ceil(duration*fps);frames={0,total-1}
def event(t):
 f=math.ceil(t*fps-1e-6)
 for n in [f-1,f,f+1]:
  if 0<=n<total:frames.add(n)
def motion(a,b):
 for f in range(max(0,math.floor(a*fps)),min(total,math.ceil(b*fps)+2)):frames.add(f)
for i,c in enumerate(chapters):
 start=c['start'];dur=c['duration'];event(start);event(start+dur)
 for j in range(3):motion(start+dur*j/3,start+dur*j/3+.3)
 if i not in (1,13):
  for j in range(1,4):motion(start+dur*j/4,start+dur*j/4+.8)
 if i in (8,10):event(start+dur*.64)
 source=(P/'compositions'/f"chapter-{c['id']}.html").read_text()
 for st,du in re.findall(r'data-start="([\d.]+)" data-duration="([\d.]+)"',source):event(start+float(st));event(start+float(st)+float(du))
ordered=sorted(frames);(OUT/'frames.json').write_text(json.dumps({'fps':fps,'duration':duration,'frames':ordered},indent=2))
# Four independent Hyperframes snapshots batches, each with sorted exact timestamps.
batches=[ordered[k::4] for k in range(4)]
def capture(k):
 dest=OUT/f'batch-{k}';manifest=dest/'manifest.json';wanted=batches[k]
 if manifest.exists() and json.loads(manifest.read_text()).get('frames')==wanted and json.loads(manifest.read_text()).get('visual_sha256')==fingerprint:return
 if dest.exists():shutil.rmtree(dest)
 times=','.join(f'{f/fps:.9f}' for f in wanted)
 cmd=['npx','--yes','hyperframes@0.8.205','snapshot',str(P),'--at',times,'--no-end','--keep','--output',str(dest),'--json']
 with (OUT/f'batch-{k}.log').open('w') as log:r=subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT)
 if r.returncode:raise RuntimeError(f'Hyperframes batch {k} failed; see log')
 files=sorted(dest.glob('at-*.png'),key=lambda p:float(p.stem[3:-1]))
 if len(files)!=len(wanted):raise RuntimeError(f'Expected {len(wanted)} frames, got {len(files)}')
 manifest.write_text(json.dumps({'visual_sha256':fingerprint,'frames':wanted,'files':[str(f.relative_to(P)) for f in files]},indent=2))
 print(f'Batch {k}: {len(files)} frames captured',flush=True)
print(f'{len(ordered)} changing/boundary frames preserve {total} output frames',flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(capture,range(4)))
paths={}
for k in range(4):
 m=json.loads((OUT/f'batch-{k}/manifest.json').read_text());paths.update(dict(zip(m['frames'],m['files'])))
lines=['ffconcat version 1.0']
for idx,f in enumerate(ordered):
 end=ordered[idx+1] if idx+1<len(ordered) else total
 lines += ["file '"+str(P/paths[f]).replace("'","'\\''")+"'",'option framerate 30',f'duration {(end-f)/fps:.12f}']
lines.extend(["file '"+str(P/paths[ordered[-1]])+"'", "option framerate 30"])
concat=OUT/'frames.ffconcat';concat.write_text('\n'.join(lines)+'\n')
# Exact chapter placement, natural-speed audio, and the same 0.35 s lead as index.html.
cmd=['ffmpeg','-hide_banner','-y','-f','concat','-safe','0','-i',str(concat)]
for c in chapters:cmd+=['-i',str(P/'assets/audio'/f"{c['id']}.mp3")]
filters=[]
for i,c in enumerate(chapters):filters.append(f'[{i+1}:a]adelay={round((c["start"]+.35)*1000)}:all=1[a{i}]')
filters.append(''.join(f'[a{i}]' for i in range(len(chapters)))+f'amix=inputs={len(chapters)}:normalize=0,apad,atrim=duration={duration}[voice]')
cmd+=['-filter_complex',';'.join(filters),'-map','0:v:0','-map','[voice]','-vf','tpad=stop_mode=clone:stop_duration=1,fps=30,format=yuv420p','-c:v','libx264','-preset','ultrafast','-crf','18','-threads','4','-c:a','aac','-b:a','192k','-t',str(duration),'-movflags','+faststart',str(P/'output'/f'assembling-{os.getpid()}.mp4')]
(OUT/'encode-command.json').write_text(json.dumps(cmd,indent=2))
with (OUT/'encode.log').open('w') as log:subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT,check=True)
os.replace(P/'output'/f'assembling-{os.getpid()}.mp4',P/'output/watchdog-walkthrough-raw.mp4')
print('Raw full-length MP4 assembled',flush=True)
