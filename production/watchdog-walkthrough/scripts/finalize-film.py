#!/usr/bin/env python3
"""Normalize narration and add native MP4 chapter markers without re-encoding video."""
import json,os,pathlib,subprocess
p=pathlib.Path(__file__).resolve().parents[1];items=json.loads((p/'timing.json').read_text());rows=[';FFMETADATA1','title=Watchdog: full feature walkthrough','comment=Isolated demonstration with synthetic telemetry. Narration by ElevenLabs.']
for c in items:
 rows+=['[CHAPTER]','TIMEBASE=1/1000',f"START={round(c['start']*1000)}",f"END={round((c['start']+c['duration'])*1000)}",'title='+c['title'].replace('=','\\=')]
meta=p/'output/chapters.ffmetadata';meta.write_text('\n'.join(rows)+'\n')
analysis=subprocess.run(['ffmpeg','-hide_banner','-i',str(p/'output/watchdog-walkthrough-raw.mp4'),'-vn','-af','loudnorm=I=-16:TP=-2:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
measured=json.JSONDecoder().raw_decode(analysis.stderr[analysis.stderr.rfind('{'):])[0]
(p/'output/normalization-measurement.json').write_text(json.dumps(measured,indent=2)+'\n')
normalizer='loudnorm=I=-16:TP=-2:LRA=11:measured_I='+measured['input_i']+':measured_TP='+measured['input_tp']+':measured_LRA='+measured['input_lra']+':measured_thresh='+measured['input_thresh']+':offset='+measured['target_offset']+':linear=true'
subprocess.run(['ffmpeg','-hide_banner','-xerror','-y','-i',str(p/'output/watchdog-walkthrough-raw.mp4'),'-i',str(meta),'-map','0:v:0','-map','0:a:0','-map_metadata','1','-map_chapters','1','-c:v','copy','-af',normalizer,'-ar','48000','-c:a','aac','-b:a','192k','-movflags','+faststart',str(p/'output'/f'normalizing-{os.getpid()}.mp4')],check=True)

os.replace(p/'output'/f'normalizing-{os.getpid()}.mp4',p/'output/watchdog-walkthrough.mp4')
