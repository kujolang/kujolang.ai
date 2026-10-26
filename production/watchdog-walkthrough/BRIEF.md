---
workflow: general-video
flow: automation
storyboard: no
message: "Understand AI usage and diagnose failures with Watchdog's local telemetry."
audience: "Developers and operators evaluating or starting Watchdog"
aspect: "16:9"
language: "en"
length: "Narration-led, approximately 6–8 minutes"
destination: "Website and YouTube walkthrough"
---

# Watchdog: the full walkthrough

User asked for a full walkthrough and overview of Watchdog's features using HyperFrames and ElevenLabs. Continue the isolated synthetic demo from the website session; never inspect the live instance. Keep release numbers out of product titles and claims. Apply clear Orwell-style narration.

Execution: autonomous, based on the user's standing instruction to do the work without approval pauses. Deliver a rendered MP4, editable HyperFrames project, narration transcript, captions, and chapter timestamps. Final render is within the requested video scope.

Defaults chosen: 1920×1080, 30 fps, English, an instructional pace, Siren voice from the existing Kujo homepage ElevenLabs setup. No cloned personal voice, no new subscription, no music bed competing with technical explanations. Real screenshots with deliberate camera moves, chapter labels, focused highlights, and designed setup/export diagrams. Clearly label synthetic data. Broad feature coverage, not an exhaustive API reference.

## Design
Use Watchdog's actual pale interface and blue accent, with ink-colored title and chapter cards and the shipped Departure Mono font. Screenshot content is real; overlays explain the view and do not fabricate application state.

## Sources
watchdog README and docs: CONNECTED_SOURCES, GRANULAR_TRACING, OBSERVABILITY_SEMANTICS, PRICING_ESTIMATES, exporters, native-producers, telemetry-jsonl-v2, runtime-measurements. The demo is /tmp/watchdog-showcase-20261026/demo.db on loopback port 7791.
