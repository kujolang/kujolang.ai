#!/usr/bin/env python3
"""Build deterministic Hyperframes chapters and aligned subtitles from cached narration."""
import json,math,subprocess,html,re
from pathlib import Path
P=Path(__file__).resolve().parents[1]
chapters=json.loads((P/'script.json').read_text())
def probe(p):return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',str(p)],text=True))
def esc(s):return html.escape(s)
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
# Product screens only; captions remain available as a separate SRT.
assets=['overview.jpg','connection.jpg','overview.jpg','overview.jpg','request.jpg','errors.png','tools.png','traces.png','session.jpg','canonical.png','sources.png','exporters.png','backups.png','overview.jpg']
start=0;hosts=[];audios=[];srt=[];chapterlines=[];timing=[];cue=1
for i,c in enumerate(chapters):
 cid='chapter-'+c['id'];audio=P/'assets/audio'/f"{c['id']}.mp3"; dur=math.ceil((probe(audio)+1.3)*30)/30
 c.update(start=round(start,3),duration=dur); timing.append(c)
 chapterlines.append(f'{int(start)//60:02}:{int(start)%60:02} {c["title"]}')
 receipt=json.loads(audio.with_suffix('.json').read_text()); a=receipt['alignment']; chars=a['characters']; starts=a['character_start_times_seconds']; ends=a['character_end_times_seconds']; txt=''.join(chars)
 words=list(re.finditer(r'\S+',txt)); captions=[]
 for k in range(0,len(words),11):
  block=words[k:k+11]; begin=starts[block[0].start()]+.35; end=ends[block[-1].end()-1]+.35; text=txt[block[0].start():block[-1].end()]
  captions.append(f'<div id="{cid}-cap-{k}" class="clip subtitle" data-start="{begin:.3f}" data-duration="{max(.1,end-begin):.3f}"><span>{esc(text)}</span></div>')
  srt.extend([str(cue),f'{stamp(start+begin)} --> {stamp(start+end)}',text,'']);cue+=1
 visual=''; anim=[]
 asset=assets[i]
 # Fit complete modal screenshots without cropping or distorting the UI.
 # The tall overview scrolls through its content at native aspect ratio.
 is_overview=asset=='overview.jpg'
 visual=f'<div class="viewport" data-hold data-layout-allow-overflow="true"><div id="{cid}-camera" class="camera{" overview" if is_overview else ""}"><img src="assets/screens/{asset}" alt="Watchdog: {esc(c["title"])}"></div></div>'
 if is_overview:
  for j,y in enumerate([0,-180,-480,-698]):
   if j==0:anim.append(f'tl.set("#{cid}-camera",{{y:0}},0);')
   else:anim.append(f'tl.to("#{cid}-camera",{{y:{y},duration:.8,ease:"power2.inOut"}},{dur*j/4:.3f});')
 if i in (8,10):
  extra='insights.png' if i==8 else 'connection.jpg'
  visual+=f'<div id="{cid}-detail" class="clip viewport" data-start="{dur*.64:.3f}" data-duration="{dur*.36:.3f}" data-layout-allow-overflow="true"><div class="camera"><img src="assets/screens/{extra}" alt="Watchdog detail"></div></div>'
 css='*{box-sizing:border-box}#root{position:absolute;inset:0;background:#fff;overflow:hidden}.viewport{position:absolute;inset:0;width:1920px;height:1080px;overflow:hidden;background:#fff}.camera{position:absolute;inset:0;display:flex;justify-content:center;align-items:center}.camera img{display:block;max-width:1920px;max-height:1080px;width:1920px;height:1080px;object-fit:contain}.camera.overview{display:block;bottom:auto}.camera.overview img{width:1920px;height:auto;max-height:none}'
 (P/'compositions'/f'{cid}.html').write_text(f'''<template><style>{css}</style><div id="root" data-composition-id="{cid}" data-width="1920" data-height="1080">{visual}</div><script>const tl=gsap.timeline({{paused:true}});{''.join(anim)}window.__timelines['{cid}']=tl;</script></template>''')
 hosts.append(f'<div id="{cid}" class="clip" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="1" data-width="1920" data-height="1080"></div>')
 audios.append(f'<audio id="voice-{i}" class="clip" src="assets/audio/{c["id"]}.mp3" data-start="{start+.35:.3f}" data-duration="{probe(audio):.3f}" data-track-index="2" data-volume="1"></audio>')
 start+=dur
(P/'index.html').write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Watchdog — full walkthrough</title><script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script><style>html,body{{margin:0;width:1920px;height:1080px;overflow:hidden}}#root{{position:relative;width:1920px;height:1080px}}.clip{{position:absolute;inset:0}}</style></head><body><div id="root" data-composition-id="main" data-start="0" data-duration="{start:.3f}" data-width="1920" data-height="1080" data-fps="30">{''.join(hosts)}{''.join(audios)}</div><script>window.__timelines=window.__timelines||{{}};window.__timelines.main=gsap.timeline({{paused:true}});</script></body></html>''')
(P/'captions.srt').write_text('\n'.join(srt));(P/'chapters.txt').write_text('\n'.join(chapterlines)+'\n');(P/'timing.json').write_text(json.dumps(timing,indent=2)+'\n'); print(f'{start:.3f} seconds; {cue-1} aligned captions')
