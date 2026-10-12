"""Generate explicitly authorized Siren V4 takes, reusing matching cached requests.

Credentials stay in ELEVENLABS_API_KEY or the existing macOS Keychain entry.
Never silently changes provider/model/voice or accelerates an overlong take.
"""
import base64
import hashlib
import json
import os
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    config = json.loads((ROOT / 'voiceover.json').read_text())
    takes = ROOT / 'takes'
    takes.mkdir(exist_ok=True)
    fitted = ROOT / 'tts-siren'
    fitted.mkdir(exist_ok=True)
    key = None
    timing = []
    for cue in config['cues']:
        payload = {'text': cue['spoken_text'], 'model_id': config['model_id'],
                   'voice_settings': config['voice_settings']}
        digest = hashlib.sha256(json.dumps({'voice': config['voice_id'], **payload}, sort_keys=True).encode()).hexdigest()
        receipt = takes / (cue['id'] + '.json')
        mp3 = takes / (cue['id'] + '.mp3')
        cached = receipt.exists() and mp3.exists() and json.loads(receipt.read_text()).get('input_sha256') == digest
        if not cached:
            key = key or os.environ.get('ELEVENLABS_API_KEY') or subprocess.check_output(
                ['security', 'find-generic-password', '-s', 'kujo-videoops-elevenlabs', '-a', 'videoops', '-w'], text=True).strip()
            request = urllib.request.Request(
                'https://api.elevenlabs.io/v1/text-to-speech/' + config['voice_id'] + '/with-timestamps?output_format=mp3_44100_128',
                data=json.dumps(payload).encode(), headers={'xi-api-key': key, 'Content-Type': 'application/json'})
            with urllib.request.urlopen(request, timeout=90) as response:
                result = json.load(response)
                request_id = response.headers.get('request-id')
            mp3.write_bytes(base64.b64decode(result.pop('audio_base64')))
            receipt.write_text(json.dumps({'provider': 'ElevenLabs', 'voice_id': config['voice_id'],
                'voice_name': config['voice_name'], 'model_id': config['model_id'], 'request': payload,
                'request_id': request_id, 'input_sha256': digest,
                'audio_sha256': hashlib.sha256(mp3.read_bytes()).hexdigest(), **result}, indent=2) + '\n')
        wav = fitted / (cue['id'] + '.wav')
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', str(mp3), '-ar', '48000', '-ac', '1', str(wav)], check=True)
        duration = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(wav)], text=True))
        fits = cue['start'] + duration <= cue['must_end']
        timing.append({'id': cue['id'], 'start': cue['start'], 'duration': duration, 'end': cue['start'] + duration, 'must_end': cue['must_end'], 'fits': fits, 'playback_rate': 1.0})
        print(cue['id'], 'cached' if cached else 'generated', round(duration, 3), 'fits' if fits else 'OVERLONG', flush=True)
    (ROOT / 'timing-check.json').write_text(json.dumps(timing, indent=2) + '\n')
    if not all(c['fits'] for c in timing):
        raise SystemExit('Revise overlong cue text or scene timing before mixing.')


if __name__ == '__main__':
    main()
