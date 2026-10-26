"""Generate cached ElevenLabs chapter narration; never persists credentials."""
import base64,hashlib,json,os,subprocess,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
voice='eXpIbVcVbLo8ZJQDlDnl'
config=dict(provider='ElevenLabs',voice_id=voice,voice_name='Siren',model_id='eleven_v4',voice_settings=dict(stability=.5,similarity_boost=.75))
(ROOT/'voice.json').write_text(json.dumps(config,indent=2)+'\n')
key=None
for c in json.loads((ROOT/'script.json').read_text()):
 payload=dict(text=c['text'],model_id=config['model_id'],voice_settings=config['voice_settings'])
 digest=hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()
 stem=ROOT/'assets/audio'/c['id']; receipt=stem.with_suffix('.json'); audio=stem.with_suffix('.mp3')
 if receipt.exists() and audio.exists() and json.loads(receipt.read_text()).get('input_sha256')==digest:
  print(c['id'],'cached',flush=True);continue
 key=key or os.environ.get('ELEVENLABS_API_KEY') or subprocess.check_output(['security','find-generic-password','-s','kujo-videoops-elevenlabs','-a','videoops','-w'],text=True).strip()
 req=urllib.request.Request('https://api.elevenlabs.io/v1/text-to-speech/'+voice+'/with-timestamps?output_format=mp3_44100_128',data=json.dumps(payload).encode(),headers={'xi-api-key':key,'Content-Type':'application/json'})
 with urllib.request.urlopen(req,timeout=120) as r:
  data=json.load(r);rid=r.headers.get('request-id')
 audio.write_bytes(base64.b64decode(data.pop('audio_base64')))
 receipt.write_text(json.dumps(dict(provider='ElevenLabs',voice_id=voice,model_id=config['model_id'],input_sha256=digest,request_id=rid,**data),indent=2)+'\n')
 print(c['id'],'generated',flush=True)
