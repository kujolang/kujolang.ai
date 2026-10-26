# Watchdog walkthrough specification
1920×1080, 30 fps. Duration follows the unmodified ElevenLabs narration, with 0.35 s lead and at least 0.95 s tail per chapter. Fourteen chapters; SRT timing comes from provider character alignment.

Palette: #edf0f4 paper, #17202d ink, #33475e annotation, #516174 secondary. Inter 52 px headings, 32 px subtitles; local Departure Mono 28 px brand rails. 96 px side safe area. Actual application imagery sits at x96/y185 in a 1728×665 clipped viewport. Camera reframes take 0.8 s with power2.inOut; each then holds for reading. No endless drift, false cursor clicks, or simulated application actions.

Opening: real 30-day demo overview, then proxy routing diagram. Middle: overview and range, individual request, error list, tools, agent activity, session and insights, canonical evidence, sources, exports, backups. Closing: three-step operating loop and source URL. Diagram labels explain behavior and are not presented as screenshots.

Screenshots: three prior browser captures plus static renders of actual demo DOM fragments, captured through the browser and rendered offline with Hyperframes after browser pixel capture failed. Styling and values retained; crop only. Canonical examples use accepted fixture records; unconfigured exporter states remain honest. Synthetic disclosure is visible throughout. Live Watchdog never touched.

Voice: ElevenLabs Siren, eleven_v4, natural speed, no clone. No music: narration-first instructional delivery; available provider music generation was not configured. No code-generated score. Loudness and peak measured after export; no claim of an auditory review unless performed.

QA: Hyperframes check, review contact sheets, camera range sample, output ffprobe, loudness/peak and black-frame checks. Correct captions, readable close-ups, no misleading product capabilities. Commit editable sources and media; ignore bulky renders and caches.
