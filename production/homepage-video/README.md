# Kujo — From output to trust

Editable source for the October 2026 homepage introduction: **77 seconds, 1920×1080, 30 fps**. The shipping master is `../../assets/videos/kujo-intro.mp4`; the homepage uses `../../assets/videos/kujo-intro.vtt` for optional English captions.

This updates the original `kujolang/kujo-hyperframes/video-kujo-intro` film while preserving its monochrome halftone artwork, local pixel/mono typography, and deterministic Three.js core. The old catalog counters and simulated runtime verification are replaced by current language/toolchain, evidence, SDK, Ability/MCP, and application capabilities. See `claim-sources.md` and `source-manifest.json` for review provenance.

## Rebuild

Requires Node.js, Python with NumPy, and FFmpeg. No provider request is needed to reuse the committed narration takes.

```sh
npm ci
python3 audio/generate_elevenlabs.py
python3 audio/build_score.py
python3 audio/make_captions.py
node /path/to/hyperframes-audio/scripts/carve.mjs --comp index.html --bed music-bed --voice narration --strength 0.15
npm run check
npm run preview
HF_CAPTURE_PARALLEL_STREAM=true npm run render
```

The spectral carve and automation are already committed in `index.html`; rerun the carve only if the voice or score changes. The motion bundle is reproducible with `npx esbuild motion-entry.js --bundle --minify --format=iife --global-name=MotionMini --outfile=assets/motion.js`.

Narration is **ElevenLabs `eleven_v4`, Siren `eXpIbVcVbLo8ZJQDlDnl`**, pronounced Koo-joe and played at natural 1× speed. Generation reuses a take only when its full request hash matches. A changed script makes paid requests using `ELEVENLABS_API_KEY` or the existing `kujo-videoops-elevenlabs` / `videoops` Keychain item. Credentials are never written to project files. Alignment receipts preserve the source for subtitle timing. Generation fails if speech exceeds its allotted window.

Delivery is encoded at H.264 CRF 22 with fast-start and mastered to -18 LUFS / -1.5 dBTP; Studio previews the same stem balance before delivery loudness normalization.

Original score and Foley are synthesized by `audio/build_score.py`: suspended harmony, an original midrange plucked motif with stereo eighth-note replies, sparse machine pulses, stereo relays, soft transition air, and a resolving three-note mark. No stock loops or borrowed samples: the composition and generated waveforms have no third-party music royalties. ElevenLabs Music was attempted but its saved key lacks music_generation permission; no ElevenLabs music was generated or used. HyperFrames mixes the same three stems shown in Studio; music has gentle speech-following spectral carving (strength 0.15, maximum 3.6 dB duck) and a 0.25 music fader. The first mix combined 19.2 dB ducking with another 9.4 dB attenuation, burying the low-register bed. This revision removes that stacked attenuation, adds speaker-friendly musical detail, and raises the synchronized Foley by about 18 dB. See `audio/provenance.json` for provider/rights metadata.

Motion.dev mini produces paused native WAAPI animations. HyperFrames seeks them in absolute time alongside the existing GSAP-controlled Three.js clock. Scenes dissolve with a 600 ms overlap; text enters after the overlap so two headlines never compete. The final frame holds the brand and URL.

`verification.json` records technical checks and final artifact identity. Visual scene/transition samples were inspected. Subjective voice timbre, pronunciation, and music balance still benefit from human listening; automated audio checks are not an audition.
