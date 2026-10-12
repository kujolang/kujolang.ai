"""Original deterministic industrial score and synchronized Foley; no samples."""
import json, wave
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent
SR=48000; DUR=77; N=SR*DUR
rng=np.random.default_rng(20261012)

def write(name,x):
 with wave.open(str(R/name),'wb') as w:
  w.setnchannels(2 if x.ndim==2 else 1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.clip(x,-1,1)*32767).astype('<i2').tobytes())
def put(buf,x,at,gain=1,pan=0):
 st=round(at*SR);x=x[:len(buf)-st]
 if buf.ndim==2 and x.ndim==1:x=np.column_stack([x*np.sqrt((1-pan)/2),x*np.sqrt((1+pan)/2)])
 buf[st:st+len(x)]+=x*gain

def tone(f,d,kind='pad'):
 t=np.arange(int(d*SR))/SR
 if kind=='pad':
  env=np.minimum(t/.6,1)*np.minimum((d-t)/1.3,1)
  return (np.sin(2*np.pi*f*t)+.24*np.sin(2*np.pi*f*2.002*t)+.08*np.sin(2*np.pi*f*3*t))*env*.11
 if kind=='pulse':return np.sin(2*np.pi*(f*t+2*(1-np.exp(-15*t))))*np.exp(-12*t)*np.minimum(t/.005,1)*.17
 if kind=='relay':return (np.sin(2*np.pi*f*t)+.4*rng.normal(size=len(t)))*np.exp(-60*t)*np.minimum(t/.002,1)*.12
 if kind=='air':
  noise=rng.normal(size=len(t));noise=np.convolve(noise,np.ones(16)/16,mode='same')
  return noise*np.sin(np.pi*t/d)**2*.20

music=np.zeros((N,2));sfx=np.zeros((N,2));voice=np.zeros(N)
# Restrained D-minor / suspended voicings. Harmony opens when tools connect;
# percussion drops out for the final spoken promise.
for a,b,notes in [(0,6,[73.416,110]),(6,17,[73.416,110,146.832]),(17,31,[65.406,98,146.832]),(31,45,[87.307,130.813,174.614]),(45,57,[73.416,110,164.814]),(57,69,[65.406,98,146.832]),(69,77,[73.416,110,146.832])]:
 for i,f in enumerate(notes):put(music,tone(f,b-a),a,.6,[-.45,.45,0][i])
for i,at in enumerate(np.arange(1,68,.7142857)):
 if i%4==0:put(music,tone(48,.5,'pulse'),at,.55)
 if at>17 and i%2==1:put(music,tone(1450+i%3*140,.10,'relay'),at,.14,(-1)**i*.5)
# Soft motion air lands on each scene change; no stock swoosh library.
for at in [6,17,31,45,57,69]:
 put(sfx,tone(0,.7,'air'),at-.28,.62,-.2)
 put(sfx,tone(58,.55,'pulse'),at+.15,.65)
for i,at in enumerate([8,8.18,8.36,18.3,19.8,21.3,22.8,24.3,32.3,34.8,37.3,46.3,46.95,47.6,58.2,59.3,70,70.5,71]):
 put(sfx,tone(1100+(i%4)*220,.12,'relay'),at,.65,(-1)**i*.35)
# Bespoke three-note resolving sonic mark under the final URL.
for i,f in enumerate([146.832,220,293.664]):put(music,tone(f,3.5-i*.25),73+i*.22,.40,[-.3,0,.3][i])
config=json.loads((R/'voiceover.json').read_text())
for c in config['cues']:
 with wave.open(str(R/'tts-siren'/(c['id']+'.wav')),'rb') as w:x=np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').astype(float)/32768
 assert c['start']+len(x)/SR<=c['must_end']
 put(voice,x,c['start'])
# Keep sufficient headroom; renderer owns spectral carving and gain automation.
music*=np.minimum(np.arange(N)/SR/1.2,1)[:,None]*np.minimum((DUR-np.arange(N)/SR)/1.1,1)[:,None]
write('narration.wav',voice);write('music.wav',music);write('sfx.wav',sfx)
print('77-second original score, SFX and natural-speed narration written')
