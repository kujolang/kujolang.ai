# Watchdog walkthrough specification
1920×1080, 30 fps. Duration follows the unmodified ElevenLabs narration, with 0.35 s lead and at least 0.95 s tail per chapter. Fourteen chapters; SRT timing comes from provider character alignment.

Screen-only revision (2026-10-27, explicit user direction): the product viewport occupies 1920×1080. No presentation titles, brand rails, disclosure rails, callouts, routing diagrams, or burned-in subtitles. Keep captions in the separate SRT. Preserve complete modal screenshots with aspect-ratio fitting; scroll the tall overview through y=0, -180, -480, -698 with 0.8 s power2.inOut moves. No simulated clicks or application actions.

Opening: actual overview, then the connection modal. Middle: overview and range, request, errors, tools, traces, session and insights, canonical evidence, sources, exports, backups. Closing: dashboard overview under the unchanged narration.

Screenshots: three prior browser captures plus static renders of actual demo DOM fragments, captured through the browser and rendered offline with Hyperframes after browser pixel capture failed. Styling and values retained; crop only. Canonical examples use accepted fixture records; unconfigured exporter states remain honest. Synthetic provenance remains in the documentation and narration, without a video overlay. Live Watchdog never touched.

Voice: ElevenLabs Siren, eleven_v4, natural speed, no clone. No music: narration-first instructional delivery; available provider music generation was not configured. No code-generated score. Loudness and peak measured after export; no claim of an auditory review unless performed.

QA: Hyperframes check, review contact sheets, camera range sample, output ffprobe, loudness/peak and black-frame checks. Correct captions, readable close-ups, no misleading product capabilities. Commit editable sources and media; ignore bulky renders and caches.
