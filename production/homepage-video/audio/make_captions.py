"""Build sidecar SRT from ElevenLabs character alignment, without timing estimates."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parent
cfg=json.loads((ROOT/'voiceover.json').read_text()); blocks=[]
fix={'Koo-joe':'Kujo','jay-sawn':'JSON','H T T P':'HTTP','H T M L':'HTML','L L M':'LLM','S D Ks':'SDKs','M C P':'MCP','C I':'CI','J unit':'JUnit'}
for cue in cfg['cues']:
 d=json.loads((ROOT/'takes'/f"{cue['id']}.json").read_text()); a=d.get('normalized_alignment') or d['alignment']; s=''.join(a['characters'])
 tokens=[]
 for m in re.finditer(r'Koo-joe|S D Ks|M C P|jay-sawn|H T T P|H T M L|L L M|C I|J unit|\S+',s):
  tokens.append((fix.get(m.group(),m.group()),a['character_start_times_seconds'][m.start()],a['character_end_times_seconds'][m.end()-1]))
 chunk=[]
 for t in tokens:
  if chunk and (len(' '.join(x[0] for x in chunk+[t]))>48 or len(chunk)>=7):
   blocks.append((cue['start']+chunk[0][1],cue['start']+chunk[-1][2],' '.join(x[0] for x in chunk)));chunk=[]
  chunk.append(t)
 if chunk:blocks.append((cue['start']+chunk[0][1],cue['start']+chunk[-1][2],' '.join(x[0] for x in chunk)))
blocks=[(s,e,re.sub(r'\s+([.,!?;:])',r'\1',text)) for s,e,text in blocks]
def tm(t):
 ms=round(t*1000);h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);s,ms=divmod(ms,1000);return f'{h:02}:{m:02}:{s:02},{ms:03}'
assert all(s<e<=77 for s,e,t in blocks)
assert all(a[1]<=b[0] for a,b in zip(blocks,blocks[1:]))
(ROOT.parent/'captions.srt').write_text('\n\n'.join(f'{i+1}\n{tm(s)} --> {tm(e)}\n{t}' for i,(s,e,t) in enumerate(blocks))+'\n')
print(len(blocks),'aligned caption cues')
