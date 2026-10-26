#!/usr/bin/env python3
"""Verify cached narration, subtitle coverage, chapter arithmetic, and final media."""
import json,pathlib,re,subprocess,hashlib
p=pathlib.Path(__file__).resolve().parents[1];timing=json.loads((p/'timing.json').read_text());end=0
for c in timing:
 assert abs(c['start']-end)<.002,(c['id'],'gap')
 r=json.loads((p/'assets/audio'/f"{c['id']}.json").read_text());a=r['alignment'];text=''.join(a['characters'])
 assert re.sub(r'\s+',' ',text).strip()==re.sub(r'\s+',' ',c['text']).strip(),c['id']
 assert len(a['characters'])==len(a['character_start_times_seconds'])==len(a['character_end_times_seconds'])
 assert all(x<=y for x,y in zip(a['character_start_times_seconds'],a['character_end_times_seconds']))
 assert a['character_end_times_seconds'][-1]+.35<c['duration']
 end=c['start']+c['duration']
srt=(p/'captions.srt').read_text();body=' '.join(line for line in srt.splitlines() if line and not line.isdecimal() and '-->' not in line)
assert re.sub(r'\s+',' ',body).strip()==re.sub(r'\s+',' ',' '.join(c['text'] for c in timing)).strip()
report={'chapters':len(timing),'caption_blocks':srt.count(' --> '),'expected_duration_seconds':round(end,3),'alignment_and_text_coverage':'pass','timeline_continuity':'pass'}
video=p/'output/watchdog-walkthrough.mp4'
if video.exists():
 info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_chapters','-show_format','-of','json',str(video)],text=True));v=next(s for s in info['streams'] if s['codec_type']=='video');a=next(s for s in info['streams'] if s['codec_type']=='audio')
 assert len(info['chapters'])==14
 assert (v['width'],v['height'],v['r_frame_rate'])==(1920,1080,'30/1')
 assert abs(float(info['format']['duration'])-end)<.15
 report.update({'video_codec':v['codec_name'],'audio_codec':a['codec_name'],'width':v['width'],'height':v['height'],'fps':v['r_frame_rate'],'duration_seconds':float(info['format']['duration']),'size_bytes':video.stat().st_size,'sha256':hashlib.file_digest(video.open('rb'),'sha256').hexdigest() if hasattr(hashlib,'file_digest') else hashlib.sha256(video.read_bytes()).hexdigest()})
(p/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
