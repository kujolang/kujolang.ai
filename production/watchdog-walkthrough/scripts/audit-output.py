#!/usr/bin/env python3
"""Measure final audio, inspect black frames, and compare exported pixels with review frames."""
import json,pathlib,re,subprocess
P=pathlib.Path(__file__).resolve().parents[1];video=P/'output/watchdog-walkthrough.mp4';metrics={}
audio=subprocess.run(['ffmpeg','-hide_banner','-i',str(video),'-vn','-af','loudnorm=I=-16:TP=-1:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
(P/'output/audio-analysis.log').write_text(audio.stderr);m=json.JSONDecoder().raw_decode(audio.stderr[audio.stderr.rfind('{'):])[0];metrics['audio']={k:float(m[k]) for k in ['input_i','input_tp','input_lra','input_thresh']}
assert -17<=metrics['audio']['input_i']<=-15
assert metrics['audio']['input_tp']<=-1
frames=[]
for t in [105,280,420,500,560]:
 ref=next((P/'output/screen-only-review').glob(f'frame-*-at-{t}s.png'));dest=P/'output'/f'verified-frame-{t}.png'
 subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(video),'-frames:v','1',str(dest)],check=True)
 r=subprocess.run(['ffmpeg','-hide_banner','-i',str(ref),'-i',str(dest),'-lavfi','ssim','-f','null','-'],capture_output=True,text=True,check=True)
 score=float(re.findall(r'All:([0-9.]+)',r.stderr)[-1]);assert score>.98,(t,score);frames.append({'seconds':t,'ssim':score})
metrics['frame_matches']=frames
black=subprocess.run(['ffmpeg','-hide_banner','-i',str(video),'-an','-vf','blackdetect=d=0.1:pix_th=0.02','-f','null','-'],capture_output=True,text=True,check=True)
(P/'output/black-frame-analysis.log').write_text(black.stderr);metrics['black_intervals']=re.findall(r'black_start:.*',black.stderr);assert not metrics['black_intervals']
path=P/'verification.json';report=json.loads(path.read_text());report.update(metrics);path.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(metrics,indent=2))
