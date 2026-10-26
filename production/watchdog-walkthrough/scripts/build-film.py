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
# These callouts explain actual behavior; they are not fabricated product screenshots.
notes=[['Where did the tokens go?','Usage · latency · failures','Synthetic demonstration data'],['Application → Watchdog → Provider','OpenAI-compatible /proxy/v1','Local SQLite telemetry'],['199,025 requests','24,026.9M tokens','Estimated API value ≠ invoice'],['Start with the broad trend','Narrow the investigation window','Requests and tokens measure different things'],['Find the request','Inspect usage and pricing evidence','Follow related records'],['Read the error code','Find the affected session','Recovery belongs to your application'],['Model time or tool time?','Arguments and results follow capture policy','Follow request and session links'],['Workflow → spans → events','Inspect recorded operations','Detail depends on instrumentation'],['One session, related activity','Eight requests · three tool calls','Use insights to choose the next question'],['Retry ≠ fallback','Observed timing and context limits','Explicit terminal events matter'],['Observed · registered · configured','Active / stale / pending','Local evidence, not a health probe'],['JSON snapshot → further analysis','Canonical JSONL → structured records','OTLP worker → compatible backend'],['Folder · interval · retention','Encryption needs a key file','Capture policy and access controls'],['Connect → Observe → Investigate','Start with one application','kujolang.ai/ecosystem/watchdog']]
assets=['overview.jpg',None,'overview.jpg','overview.jpg','request.jpg','errors.png','tools.png','traces.png','session.jpg','canonical.png','sources.png','exporters.png','backups.png',None]
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
 if assets[i]:
  asset=assets[i]; panel=asset.endswith('.png'); w=1728; imgw=1728; h=1600 if asset=='overview.jpg' else 973 if panel else 973
  visual=f'<div class="viewport" data-hold data-layout-allow-overflow="true"><div id="{cid}-camera" class="camera"><img src="assets/screens/{asset}" width="{imgw}" style="width:{imgw}px;max-width:none" alt="Watchdog synthetic demo: {esc(c["title"])}"></div></div>'
  # Anchored camera holds; no perpetual drift or animated UI claims.
  targets=[(1,0,0),(1,0,-190),(1,0,-620),(1,0,-850)] if asset=='overview.jpg' else [(1,0,0),(1.15,-100,-90),(1.08,-60,-190),(1,0,0)]
  if i==3: targets=[(1,0,0),(1.5,-820,-110),(1,0,-620),(1,0,0)]
  for j,(scale,x,y) in enumerate(targets):
   t=dur*j/4
   if j==0:anim.append(f'tl.set("#{cid}-camera",{{scale:{scale},x:{x},y:{y},transformOrigin:"0 0"}},0);')
   else:anim.append(f'tl.to("#{cid}-camera",{{scale:{scale},x:{x},y:{y},duration:.8,ease:"power2.inOut"}},{t:.3f});')
  if i in (8,10):
   visual+=f'<div id="{cid}-insights" class="clip viewport" data-start="{dur*.64:.3f}" data-duration="{dur*.36:.3f}" data-layout-allow-overflow="true"><img src="assets/screens/{"insights.png" if i==8 else "connection.jpg"}" style="width:1728px" alt="Agent Insights from synthetic telemetry"></div>'
 else:
  labels=['Your application','Watchdog','AI provider'] if i==1 else ['Connect','Observe','Investigate']
  desc=['OpenAI-compatible client','Proxy + local SQLite','Upstream response'] if i==1 else ['One application','Usage, latency, failures','Requests, sessions, traces']
  visual='<div class="diagram" data-hold>'+''.join(f'<div id="{cid}-step-{j}" class="step"><div class="num" data-layout-ignore>0{j+1}</div><h2>{esc(x)}</h2><p>{esc(desc[j])}</p></div>'+('<div class="arrow">→</div>' if j<2 else '') for j,x in enumerate(labels))+'</div>'
  for j in range(3):anim.append(f'tl.fromTo("#{cid}-step-{j}",{{opacity:1}},{{opacity:1,duration:.6,ease:"power3.out"}},{j*3});')
  extra='Direct request / trace telemetry · Canonical batches · Supported OTLP traces' if i==1 else 'kujolang.ai/ecosystem/watchdog'
  visual+=f'<div class="diagram-note">{extra}</div>'
 callouts=''
 for j,n in enumerate(notes[i]):
  at=dur*j/3; length=dur/3
  callouts+=f'<div id="{cid}-note-{j}" class="clip callout" data-start="{at:.3f}" data-duration="{length:.3f}"><span>{esc(n)}</span></div>'
  anim.append(f'tl.fromTo("#{cid}-note-{j} span",{{opacity:0}},{{opacity:1,duration:.3}},{at:.3f});')
 css='''*{box-sizing:border-box}#root{position:absolute;inset:0;font-family:Inter,sans-serif;color:#17202d;background:#edf0f4;overflow:hidden}.ground{position:absolute;inset:0;background:#edf0f4}.top{position:absolute;left:96px;right:96px;top:48px;display:flex;justify-content:space-between;font-family:Departure,monospace;font-size:28px;letter-spacing:1px;color:#516174}h1{position:absolute;top:91px;left:96px;font-size:52px;font-weight:700;letter-spacing:-1.5px;margin:0}.viewport{position:absolute;left:96px;top:185px;width:1728px;height:665px;overflow:hidden;border:1px solid #cbd3de;border-radius:12px;background:#fff}.camera{position:absolute;left:0;top:0}.camera img{display:block}.callout{position:absolute;left:96px;top:866px;font-size:28px;color:#33475e;font-weight:700}.subtitle{position:absolute;left:170px;right:170px;top:938px;height:88px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:32px;line-height:1.3;color:#fff}.subtitle span{padding:10px 22px;border-radius:8px;background:#17202d}.foot{position:absolute;bottom:22px;left:96px;right:96px;font-family:Departure,monospace;font-size:28px;color:#516174;display:flex;justify-content:space-between}.diagram{position:absolute;left:110px;right:110px;top:300px;display:flex;align-items:center;justify-content:space-between}.step{width:450px}.num{font-family:Departure,monospace;font-size:92px;color:#bec9d6;border-bottom:3px solid #243e5b;padding-bottom:20px}h2{font-size:42px;margin:26px 0 16px}.step p{font-size:28px;color:#516174}.arrow{font-size:60px;color:#243e5b}.diagram-note{position:absolute;left:110px;top:730px;font-size:29px;color:#33475e}'''
 (P/'compositions'/f'{cid}.html').write_text(f'''<template><style>@font-face{{font-family:Departure;src:url('assets/fonts/DepartureMono-Regular.woff2')}}{css}</style><div id="root" data-composition-id="{cid}" data-width="1920" data-height="1080"><div class="ground"></div><div class="top"><span>W / WATCHDOG</span><span>FEATURE WALKTHROUGH · {i+1:02} / 14</span></div><h1>{esc(c['title'])}</h1>{visual}{callouts}{''.join(captions)}<div class="foot"><span>ISOLATED DEMO · SYNTHETIC DATA</span><span>KUJO</span></div></div><script>const tl=gsap.timeline({{paused:true}});{''.join(anim)}window.__timelines['{cid}']=tl;</script></template>''')
 hosts.append(f'<div id="{cid}" class="clip" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="1" data-width="1920" data-height="1080"></div>')
 audios.append(f'<audio id="voice-{i}" class="clip" src="assets/audio/{c["id"]}.mp3" data-start="{start+.35:.3f}" data-duration="{probe(audio):.3f}" data-track-index="2" data-volume="1"></audio>')
 start+=dur
(P/'index.html').write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Watchdog — full walkthrough</title><script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script><style>html,body{{margin:0;width:1920px;height:1080px;overflow:hidden}}#root{{position:relative;width:1920px;height:1080px}}.clip{{position:absolute;inset:0}}</style></head><body><div id="root" data-composition-id="main" data-start="0" data-duration="{start:.3f}" data-width="1920" data-height="1080" data-fps="30">{''.join(hosts)}{''.join(audios)}</div><script>window.__timelines=window.__timelines||{{}};window.__timelines.main=gsap.timeline({{paused:true}});</script></body></html>''')
(P/'captions.srt').write_text('\n'.join(srt));(P/'chapters.txt').write_text('\n'.join(chapterlines)+'\n');(P/'timing.json').write_text(json.dumps(timing,indent=2)+'\n'); print(f'{start:.3f} seconds; {cue-1} aligned captions')
