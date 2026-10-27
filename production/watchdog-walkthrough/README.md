# Watchdog: full feature walkthrough

A 9:27 narrated tour of Watchdog, authored in Hyperframes at 1920×1080 / 30 fps. Fourteen chapters cover connection paths, the overview and range controls, requests and pricing, errors, tools, traces, sessions and insights, canonical evidence, sources, exports, backups, and an operating workflow.

## Deliverables

- `index.html` and `compositions/`: editable film.
- `script.json` / `narration.md`: source-grounded narration.
- `assets/audio/`: ElevenLabs Siren narration and character-alignment receipts; no credentials.
- `assets/screens/`: synthetic Watchdog demo views.
- `captions.srt`, `chapters.txt`, `timing.json`: timed accessibility and navigation assets.
- `output/watchdog-walkthrough.mp4`: local final export with native chapter markers (ignored by Git).

The current cut shows only Watchdog screens: no top/bottom rails, titles, callouts, diagrams, or burned-in subtitles. Modal views retain their original aspect ratio and complete content; the tall dashboard pans vertically. Narration and chapter timing are unchanged. `captions.srt` remains available separately. A 480p preview is at `output/watchdog-walkthrough-480p.mp4`.

## Rebuild

Requires Node/npm, Python 3, FFmpeg and ffprobe. Cached narration and captured media are included.

```sh
python3 scripts/build-film.py
npm run check
npx --yes hyperframes@0.8.205 preview --background
python3 scripts/render-sparse.py
python3 scripts/finalize-film.py
python3 scripts/verify-film.py
npx --yes hyperframes@0.8.205 snapshot --at 105,280,420,500,560 --no-end --output output/screen-only-review
python3 scripts/audit-output.py
```

The delivered export uses `render-sparse.py`: Hyperframes captures every 30 fps frame during the authored finite animations and every scene/detail boundary. FFmpeg holds identical states between them and assembles the complete film. This preserves motion and natural-speed audio while avoiding redundant captures on long reading holds. For arbitrary new animation, use the normal `npm run render` command instead, or extend the sparse schedule.

`generate-narration.py` uses an existing ElevenLabs key from the environment or the named local Keychain entry. It caches by payload digest and preserves request IDs. Do not commit credentials or dump the keychain result. The current cached narration needs no network regeneration.

## Evidence and provenance

Product source: `github.com/kujolang/watchdog`, revision `b0a682a3a0beaa7482b34e83245c607de81d260d`; README, `docs/GRANULAR_TRACING.md`, `docs/OBSERVABILITY_SEMANTICS.md`, connected-source and exporter documentation, and the actual dashboard.

The initial overview, request, and session images came from the earlier website showcase captures. Its deterministic seed is `../../scripts/seed-watchdog-showcase.py`; receipt is `../../assets/images/watchdog-demo/receipt.json`. The 30-day calendar view contains 199,025 requests and 24,026,933,218 tokens, with matching estimated values, errors, and sessions. All records are synthetic. Estimated API value is not an invoice or a subscription charge.

Additional panel images preserve the rendered DOM of the isolated demo at `127.0.0.1:7791`, restaged with its own CSS as bounded static compositions and rendered by Hyperframes. This was necessary because the desktop browser's pixel capture failed. Values and labels were not invented or retouched. Only framing changed. Sources and exporter/backup configuration views show the actual unconfigured state. The synthetic-data provenance is retained here and in the narration; the screen-only revision has no disclosure overlay.

`scripts/seed-evidence-demo.py` supplements only port 7791 with documented canonical retry/timing fixture examples plus a four-span research workflow. It never sends provider requests. Its receipt records accepted counts. The five canonical fixture records and seven records translated from trace intake are separate demonstrations from the historical request dataset. Screens show these progressively introduced examples; historical request totals are unchanged.

No live Watchdog database, configuration, credentials, or customer data were used or modified. The presentation is a narrated tour of actual captured states, with full-frame product screens, not a recording of continuous mouse interaction. Canonical semantics and features depend on producer instrumentation; missing evidence is not fabricated.

No music was added to the instructional narration. Output loudness is normalized and measured; the review distinguishes visual/technical checks from an auditory listening pass.
