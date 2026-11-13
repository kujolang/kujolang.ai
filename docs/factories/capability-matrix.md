# Factory capability matrix

Research date: 2026-11-13. Internal editorial evidence, not a claim that every factory has equal capabilities. No fresh provider-backed missions were run. Each field links to the exact inspected source revision. GitHub release presence was checked through the releases API, independently of package versions.

| Factory | Source commit | GitHub release | Public status |
| --- | --- | --- | --- |
| Software Factory | `cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24` | 0.1.0 | Published GitHub release |
| VideoOps Factory | `dcf2dc4fa7311f59ba3dd16f58a227439a155979` | None found | Default-branch source preview; no published GitHub release found |
| Publishing House Factory | `38e7900a16f8482d12ad6b8b6a15f538d7ee3099` | None found | Default-branch source preview; no published GitHub release found |
| WebOps Factory | `a2aba2c63777f37bf47d64dc93748949658b977b` | None found | Default-branch source preview; no published GitHub release found |
| Product Launch Factory | `d61c7021b0469c45f909b8371205f0df3afbac8b` | v0.1.0 | Published GitHub release |

## Software Factory

Repository: [software-factory](https://github.com/kujolang/software-factory); remote main `cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24`. Package version `0.1.0` is separate from GitHub release status.

| Field | Verified scope | Evidence |
| --- | --- | --- |
| Audience | Developers preparing locally reviewed Node HTTP APIs, optional SQLite and static browser interfaces from a software mission; single trusted operator. | [README.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/README.md), [PACKS.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/PACKS.md) |
| Input | Mission text plus an optional reviewed and sealed JSON software pack. Packs define requirements, allowed files and bounded API/browser tests as data; issue tracker is default, converter and notes are examples. | [mission.txt](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/factory/mission.txt), [converter.json](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/packs/converter.json), [PACKS.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/PACKS.md) |
| Roles | Commander interprets mission; architect scopes work; backend and frontend workers propose files concurrently; independent reviewer gates corrections; separate release reviewer examines the exact candidate. Read-only observer has no execution authority. | [worker.mjs](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/factory/worker.mjs), [dispatch.kujo](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/factory/dispatch.kujo), [ARCHITECTURE.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/ARCHITECTURE.md) |
| Execution | Node controller invokes pinned native Kujo Dispatch; tool-free Codex proposals enter allowlisted files. Trusted Workcell adapter executes generated code and API/browser checks in rootless containers. npm run factory -- run factory/mission.txt starts live work. | [cli.mjs](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/factory/cli.mjs), [dispatch.kujo](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/factory/dispatch.kujo), [workcell.mjs](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/factory/workcell.mjs), [worker.mjs](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/factory/worker.mjs) |
| Outputs | Locally approved build only after release verification; source, frozen pack, reports and audit/export bundle. Export schema is kujo.factory.export/v1. Examples are untrusted smoke fixtures, not current approval. | [export.mjs](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/factory/export.mjs), [USAGE.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/USAGE.md), [PROVENANCE.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/PROVENANCE.md) |
| Evidence | Run journal, worker proposals, rejected attempts, native Dispatch and Workcell evidence, API/browser results and exact source/harness/pack hashes; read-only Factory Floor and replay. | [core.mjs](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/factory/core.mjs), [index.html](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/factory/web/index.html), [VERIFICATION.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/VERIFICATION.md) |
| Review | Independent model review plus trusted acceptance checks, separate release review and repeated source-bound gates. Human reviews the software pack before sealing and reviews intended deployment separately. Source identity does not establish correctness or test completeness. | [PACKS.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/PACKS.md), [ARCHITECTURE.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/ARCHITECTURE.md), [VERIFICATION.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/VERIFICATION.md) |
| Boundaries | Rootless Docker with seccomp, read-only root, no outside network, scoped mounts, process/memory/deadline limits. Provider home, Docker socket and host evidence are not mounted. Nested Chromium sandbox unavailable inside qualified outer Workcell; no kernel-exploit guarantee. | [SECURITY.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/SECURITY.md), [WORKCELL.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/factory/WORKCELL.md) |
| Dependencies | Kujo runtime 1.9.0, Codex 0.144.4, AJV 8.20.0 and ajv-formats 3.0.1; exact Dispatch, Workcell and kujo-agents commits in source lock. No shipped Spec/Eval/ShipCheck/RunLedger/Casefile integration in this release. | [sources.lock.json](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/sources.lock.json), [package.json](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/package.json), [dispatch.kujo](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/factory/dispatch.kujo) |
| Demo | Canonical narrated issue-tracker demonstration is historical Agent City extraction, predates software packs, and does not qualify the standalone release. SHA-256 4046393dc1e7c836ee8b944a6006ab81c8ea28aeae1c9a8a387581104ff0288e. | [PROVENANCE.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/PROVENANCE.md), [software-factory-demo.png](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/media/software-factory-demo.png) |
| Setup | Git, Node >=26.12.1 <27, Codex account and local rootless Docker/seccomp. npm ci; npm run setup; npm run login; configure rootless engine; npm run image:build; npm run doctor; npm run verify; npm run smoke; npm start. Floor port 4380. Linux/WSL intended but live native Linux/ARM/WSL not qualified; recorded live engine qualification is macOS/Colima. | [README.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/README.md), [INSTALL.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/INSTALL.md), [ENGINE.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/ENGINE.md), [VERIFICATION.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/VERIFICATION.md) |
| Limitations | Local single operator only; no hosted multi-tenant service, unattended crash recovery or deployment qualification. Future ecosystem integration work in feature branches is outside published 0.1.0. Current public main and release match at research time. | [README.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/README.md), [SECURITY.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/SECURITY.md), [VERIFICATION.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/VERIFICATION.md) |
| Relationships | Standalone software-production system; no universal factory controller. Product Launch separately pins a newer Software Factory evidence-verifier revision; that is not a feature of this published baseline. | [ARCHITECTURE.md](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/docs/ARCHITECTURE.md), [sources.lock.json](https://github.com/kujolang/software-factory/blob/cfddc146e225229a9c15d3bf8ad2bfc01e2c8e24/sources.lock.json) |

### Exact dependencies

```json
{
  "npm": {
    "@kujolang/kujo-runtime": "1.9.0",
    "@openai/codex": "0.144.4",
    "ajv": "8.20.0",
    "ajv-formats": "3.0.1"
  },
  "overrides": {},
  "source_lock": {
    "schema": "kujo.software-factory.sources/v1",
    "repositories": {
      "dispatch": {
        "url": "https://github.com/kujolang/dispatch.git",
        "commit": "18b5c737a73904ae942f0bd1c3baa1f77c2bfb40"
      },
      "workcell": {
        "url": "https://github.com/kujolang/workcell.git",
        "commit": "189d7ab6e975301a0e5100b65e8ad3fe4a584573"
      },
      "kujo-agents": {
        "url": "https://github.com/kujolang/kujo-agents.git",
        "commit": "a7e9d0236d6e64b5db30273b32f4ad8c124f5173"
      }
    }
  }
}
```

## VideoOps Factory

Repository: [videoops-factory](https://github.com/kujolang/videoops-factory); remote main `dcf2dc4fa7311f59ba3dd16f58a227439a155979`. Package version `0.1.0` is separate from GitHub release status.

| Field | Verified scope | Evidence |
| --- | --- | --- |
| Audience | Small teams creating screenshot-led product launch clips from sourced facts and registered media. | [README.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/README.md), [AGENT-SETUP.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/AGENT-SETUP.md) |
| Input | kujo.videoops.brief/v1 JSON: request, facts with sources, CTA, registered asset IDs; 1920×1080 or 1080×1920, 30fps, 3–60 seconds, silent. Operator registers trusted assets with provenance, rights and SHA-256. | [launch-brief.json](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/examples/launch-brief.json), [social-brief.json](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/examples/social-brief.json), [catalog.json](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/assets/catalog.json), [contracts.mjs](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/src/contracts.mjs) |
| Roles | Producer validates scope; Creative Director proposes timed plan; Asset Scout checks supplied provenance; Media Generator records NOT_REQUIRED for silent registered assets; HyperFrames Editor reviews plan; Video Critic reviews technical evidence. Calls are sequential. | [runner.mjs](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/src/runner.mjs), [agent.mjs](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/src/agent.mjs) |
| Execution | Canonical videoops-production initializer; tool-free Codex proposals; trusted compiler creates HyperFrames scenes, checks and renders; canonical Python review tool records exact-candidate status. npm run factory -- run examples/launch-brief.json. | [runner.mjs](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/src/runner.mjs), [render.mjs](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/src/render.mjs), [template.mjs](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/src/template.mjs) |
| Outputs | output/draft.mp4, editable production/hyperframes project, metadata, frames, logs, role proposals and handoffs. Landscape and portrait examples are intentionally silent 12-second clips. | [README.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/README.md), [render.mjs](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/src/render.mjs), [run.json](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/examples/software-factory-launch/run.json) |
| Evidence | State timestamps/elapsed time, JSONL events, kujo.handoff/v1 records, registered file hashes, metadata/technical checks, exact candidate SHA and videoops-review-decision/v1 ledger. | [runner.mjs](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/src/runner.mjs), [REVIEW.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/REVIEW.md) |
| Review | Successful run stops at REVIEW_INCOMPLETE. Full visual playback and listening (including intentional silence) required by capable reviewer; local record/promote commands bind exact SHA. Rendering, contact sheets and model statements do not provide perceptual approval. | [REVIEW.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/REVIEW.md), [runner.mjs](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/src/runner.mjs) |
| Boundaries | Tools/apps/web disabled for private Codex proposals; trusted renderer accepts validated data, not model HTML/JS. Loopback read-only floor. Registered codecs/media remain trusted host operations; this factory does not inherit Workcell isolation. | [SECURITY.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/SECURITY.md), [contracts.mjs](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/src/contracts.mjs) |
| Dependencies | Kujo 1.9.0, Codex 0.144.4, GSAP 3.14.2, HyperFrames 0.9.40, Undici override 7.30.2; kujo-agents and kujo-workflows pinned sources; Python kujo-agents-videoops 0.3.0 with exact requirements. Retired kujo-videoops is historical, not a dependency. | [package.json](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/package.json), [sources.lock.json](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/sources.lock.json), [REUSE.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/REUSE.md) |
| Demo | Canonical narrated showcase uses actual floor/review stills and example renders from distinct recorded runs. Technical PASS; full listening not attested; REVIEW_INCOMPLETE. Separate authorized Siren demo does not make automatic narration part of silent runner. | [DEMO.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/DEMO.md), [manifest.json](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/media/manifest.json), [playback-verification.json](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/media/playback-verification.json) |
| Setup | macOS/Linux; Git, Node >=26.12.1 <27, Python 3.10+, FFmpeg/ffprobe 6+ with libx264/AAC, Codex account; browser download for render and libatomic1 on minimal Ubuntu. npm ci; setup; login; doctor; verify; npm start. Floor 4381. Model usage is separate from setup; no paid media generation on silent route. | [README.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/README.md), [REUSE.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/REUSE.md), [ONBOARDING-BENCHMARK.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/ONBOARDING-BENCHMARK.md) |
| Limitations | Three to five template scenes and final Kujo bumper; no general footage timeline, automatic narrated campaigns, arbitrary remote assets, automatic editor repair loop or publication. Failed runs require a new run; no mid-render resume. | [AGENT-SETUP.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/AGENT-SETUP.md), [REVIEW.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/REVIEW.md), [contracts.mjs](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/src/contracts.mjs) |
| Relationships | Standalone factory; Product Launch consumes pinned tools via a coordinator adapter. Canonical VideoOps tools live in kujo-agents, not retired kujo-videoops. | [REUSE.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/docs/REUSE.md), [README.md](https://github.com/kujolang/videoops-factory/blob/dcf2dc4fa7311f59ba3dd16f58a227439a155979/README.md) |

### Exact dependencies

```json
{
  "npm": {
    "@kujolang/kujo-runtime": "1.9.0",
    "@openai/codex": "0.144.4",
    "gsap": "3.14.2",
    "hyperframes": "0.9.40"
  },
  "overrides": {
    "undici": "7.30.2"
  },
  "source_lock": {
    "schema": "kujo.videoops-factory.sources/v1",
    "repositories": {
      "kujo-agents": {
        "url": "https://github.com/kujolang/kujo-agents.git",
        "commit": "a7e9d0236d6e64b5db30273b32f4ad8c124f5173"
      },
      "kujo-workflows": {
        "url": "https://github.com/kujolang/kujo-workflows.git",
        "commit": "d766eae4fd9a131e51c34796d029fd3bc6974689"
      }
    },
    "python": {
      "distribution": "kujo-agents-videoops",
      "version": "0.3.0",
      "requirements": {
        "pip": "24.3.1",
        "setuptools": "80.9.0",
        "wheel": "0.45.1",
        "jsonschema": "4.26.0",
        "attrs": "23.2.0",
        "jsonschema-specifications": "2025.9.1",
        "referencing": "0.37.0",
        "rpds-py": "0.30.0",
        "typing-extensions": "4.15.0"
      }
    }
  }
}
```

## Publishing House Factory

Repository: [publishing-house-factory](https://github.com/kujolang/publishing-house-factory); remote main `38e7900a16f8482d12ad6b8b6a15f538d7ee3099`. Package version `0.1.0` is separate from GitHub release status.

| Field | Verified scope | Evidence |
| --- | --- | --- |
| Audience | Editorial teams producing a reviewable article and adaptations from supplied source material. | [README.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/README.md), [AGENT-SETUP.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/AGENT-SETUP.md) |
| Input | Brief schema kujo.publishing-house-factory.brief/v1 with title/audience/objective/voice/constraints and 1–10 UTF-8 source files inside brief directory; each <=100 KB, brief <=64 KB; HTTPS URLs are provenance, not remote retrieval. | [AGENT-SETUP.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/AGENT-SETUP.md), [videoops-launch.json](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/examples/videoops-launch.json), [factory.py](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/src/factory.py) |
| Roles | Commissioning Editor proposes angle/outline; Standards & Evidence Editor maps claims and separately reviews article; Technical Editor/Writer drafts/revises; Franchise & Adaptation Editor creates newsletter, three social posts and landing copy; Copy Chief reviews adaptations. Production code packages records. | [README.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/README.md), [editorial.py](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/src/editorial.py) |
| Execution | Canonical Publishing House Operator owns phases, leases, retries/checkpoints and approval pause. Python adapter calls Codex directly for sequential tool-free proposals and allowlisted Kujo tool commands. Text-only asset stage runs no media generator. | [common.py](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/src/common.py), [factory.py](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/src/factory.py), [editorial.py](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/src/editorial.py), [ARCHITECTURE.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/ARCHITECTURE.md) |
| Outputs | Article and newsletter Markdown/JSON, exactly three social drafts, escaped landing HTML, retained source packet and versioned package manifest; local six-preview Factory Floor. | [editorial.py](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/src/editorial.py), [manifest.json](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/example-campaign/manifest.json), [README.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/README.md) |
| Evidence | Source snapshots and hashes; exact-excerpt claim mapping in Dossier; request/proposal pairs; BluePencil reviews; GalleyPack version/revision lineage and frozen manifest; VersionSeal request. | [editorial.py](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/src/editorial.py), [ARCHITECTURE.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/ARCHITECTURE.md) |
| Review | Separate writer/reviewer calls, at most two article revisions and two adaptation revisions. Excerpt presence is observed support, not truth. Model pass ends at approval_required/AWAITING_HUMAN_REVIEW; human must inspect exact package. | [REVIEW.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/REVIEW.md), [editorial.py](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/src/editorial.py) |
| Boundaries | No model code execution, browse or general tools; private read-only Codex proposals, regular confined source files, escaped HTML and loopback read-only viewer. Source text goes to model provider. No Workcell sandbox or publication credentials. | [SECURITY.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/SECURITY.md), [propose.mjs](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/scripts/propose.mjs) |
| Dependencies | Kujo 1.9.0 and Codex 0.144.4; exact pinned canonical operator/roles and StoryDesk, Dossier, GalleyPack, BluePencil, VersionSeal. Dispatch and Agents SDK satisfy installed operator layout but do not run this adapter’s workers. PressWire initialized for compatibility; no publication effects. | [package.json](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/package.json), [sources.lock.json](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/sources.lock.json), [ARCHITECTURE.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/ARCHITECTURE.md), [factory.py](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/src/factory.py) |
| Demo | Recorded live campaign and narrated canonical demo; inspect source/transition/playback verification. These are recorded evidence, not new work or campaign publication approval. | [DEMO.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/DEMO.md), [manifest.json](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/media/manifest.json), [playback-verification.json](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/media/playback-verification.json), [factory-floor.png](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/factory-floor.png) |
| Setup | macOS/Linux/compatible WSL, Git, Python 3.10+, Node >=26.12.1 <27 and Codex account. npm ci; npm run setup; npm run login; npm run doctor; npm run verify; npm start. Run examples/videoops-launch.json in another terminal. Floor 4382. No Docker/FFmpeg/database needed. | [README.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/README.md), [AGENT-SETUP.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/AGENT-SETUP.md) |
| Limitations | One fixed text campaign contract; no source research, media production or publication destinations. No approval/publish CLI, and direct publication phases rejected. Resume preserves completed matching artifacts; changed input or exhausted revisions require new run. | [REVIEW.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/REVIEW.md), [SECURITY.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/SECURITY.md), [factory.py](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/src/factory.py) |
| Relationships | Standalone editorial system coordinated by canonical operator. Product Launch invokes this factory for copy; Software and VideoOps remain independent. | [README.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/README.md), [ARCHITECTURE.md](https://github.com/kujolang/publishing-house-factory/blob/38e7900a16f8482d12ad6b8b6a15f538d7ee3099/docs/ARCHITECTURE.md) |

### Exact dependencies

```json
{
  "npm": {
    "@kujolang/kujo-runtime": "1.9.0",
    "@openai/codex": "0.144.4"
  },
  "overrides": {},
  "source_lock": {
    "schema": "kujo.publishing-house-factory.sources/v1",
    "repositories": {
      "kujo-workflows": {
        "url": "https://github.com/kujolang/kujo-workflows.git",
        "commit": "d766eae4fd9a131e51c34796d029fd3bc6974689"
      },
      "kujo-agents": {
        "url": "https://github.com/kujolang/kujo-agents.git",
        "commit": "a7e9d0236d6e64b5db30273b32f4ad8c124f5173"
      },
      "storydesk": {
        "url": "https://github.com/kujolang/storydesk.git",
        "commit": "31b4d2965c1a977c37fc9560cbc13480f7cf8f5b"
      },
      "dossier": {
        "url": "https://github.com/kujolang/dossier.git",
        "commit": "670def8c62e690bcd3c0936cd85b224257ca4a03"
      },
      "galleypack": {
        "url": "https://github.com/kujolang/galleypack.git",
        "commit": "f829584070b098488b7538f30ed6e97c32c62c0e"
      },
      "bluepencil": {
        "url": "https://github.com/kujolang/bluepencil.git",
        "commit": "88df35c3514c78fd986d750b3ff281ca280efabf"
      },
      "versionseal": {
        "url": "https://github.com/kujolang/versionseal.git",
        "commit": "f005374d72026a57c5246b6ed38473209e4bfc32"
      },
      "presswire": {
        "url": "https://github.com/kujolang/presswire.git",
        "commit": "2f8bd7054a62101ff3e97f3e1a0a61a77d35fe22"
      },
      "dispatch": {
        "url": "https://github.com/kujolang/dispatch.git",
        "commit": "18b5c737a73904ae942f0bd1c3baa1f77c2bfb40"
      },
      "agents-sdk": {
        "url": "https://github.com/kujolang/agents-sdk.git",
        "commit": "70cd1fb780cf102dd4d09d2d5ba4d24a85ce462c"
      }
    }
  }
}
```

## WebOps Factory

Repository: [webops-factory](https://github.com/kujolang/webops-factory); remote main `a2aba2c63777f37bf47d64dc93748949658b977b`. Package version `0.1.0` is separate from GitHub release status.

| Field | Verified scope | Evidence |
| --- | --- | --- |
| Audience | Owners of bounded static exports needing scoped metadata, image-alternative and internal-link fixes on a disposable copy. | [README.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/README.md), [AGENT-SETUP.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/AGENT-SETUP.md) |
| Input | JSON title/site/objective; static site relative to mission. At most 120 files and 8,000,000 bytes; worker context 150 KB. HTML/CSS/SVG/common images/text/XML allowed. Scripts, event handlers, frames, symlinks and active embeds rejected; hidden files/node_modules excluded. | [studio.json](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/examples/studio.json), [siteops.py](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/src/siteops.py), [factory.py](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/src/factory.py), [README.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/README.md) |
| Roles | Metadata Auditor owns missing/empty title and description; Link Health Auditor owns broken local file destinations; Accessibility Auditor supplies missing alt attributes; Site QA Operator independently reviews exact patch. Sequential tool-free calls. | [factory.py](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/src/factory.py), [ARCHITECTURE.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/ARCHITECTURE.md) |
| Execution | Snapshot original, deterministic HTML audit, SiteProbe crawl/verify and Lens check; validate values, repair candidate copy, repeat checks, independent model review and package. --fixture supplies fixed proposals but real browser/crawl tools; --live uses Codex. | [factory.py](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/src/factory.py), [siteops.py](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/src/siteops.py) |
| Outputs | before/ snapshot, candidate/ repaired copy, before/after findings, proposals/ and requests/, patches/repairs.diff, evidence/ SiteProbe/Lens output and package.json. | [README.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/README.md), [factory.py](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/src/factory.py), [package.json](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/example-run/package.json) |
| Evidence | Original byte comparison, exact source diff, before/after homepage desktop/mobile screenshots, crawl/browser/accessibility/link reports, worker values and reasons, independent review, manifest file hashes. | [ARCHITECTURE.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/ARCHITECTURE.md), [factory.py](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/src/factory.py), [VERIFICATION.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/VERIFICATION.md) |
| Review | Zero supported findings, passing final Lens threshold and passing independent review required for approval_required package. Broader crawl warnings retained. Human reviews patch/candidate before separate release process. | [factory.py](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/src/factory.py), [VERIFICATION.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/VERIFICATION.md) |
| Boundaries | Workers cannot submit commands, markup, external targets or new repair types. Original never modified; preview CSP blocks scripts and network effects. Local floor read-only; manifest integrity is not a signature or malicious-host defense. | [SECURITY.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/SECURITY.md), [siteops.py](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/src/siteops.py), [factory.py](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/src/factory.py) |
| Dependencies | Kujo 1.9.0, Codex 0.144.4, Playwright 1.61.1; exact SiteProbe, Lens, kujo-agents and kujo-workflows commits. Canonical finding-to-fix PROPOSE contract informs adapter; production mutation step is not invoked. | [package.json](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/package.json), [sources.lock.json](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/sources.lock.json), [ARCHITECTURE.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/ARCHITECTURE.md) |
| Demo | Canonical narrated video shows exported recorded live run, not real-time execution. Media REVIEW_INCOMPLETE because listening not attested. npm run demo imports verified checked-in record without new model work. | [VERIFICATION.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/VERIFICATION.md), [manifest.json](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/media/manifest.json), [readme-playback.json](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/media/readme-playback.json) |
| Setup | macOS/Linux/compatible WSL; Git, Python 3.10+, Node >=26.12.1 <27, Codex for live mode. npm ci; setup; login; doctor; npm run factory -- run examples/studio.json --live; npm start. Linux may need npx playwright install-deps chromium. Floor 4383. | [README.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/README.md), [AGENT-SETUP.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/AGENT-SETUP.md), [setup.mjs](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/scripts/setup.mjs) |
| Limitations | Only four repair operations; no full WCAG/SEO certification, external link health, fragments, rankings/analytics, JavaScript sites, frameworks, authenticated crawling, retry/resume, source mutation or deployment. Static audit covers imported HTML; Lens checks homepage desktop/mobile. | [README.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/README.md), [ARCHITECTURE.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/ARCHITECTURE.md), [siteops.py](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/src/siteops.py) |
| Relationships | Standalone bounded adapter using SiteProbe/Lens; Product Launch consumes website candidate and browser evidence. Other factories are related, not runtime parents. | [README.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/README.md), [ARCHITECTURE.md](https://github.com/kujolang/webops-factory/blob/a2aba2c63777f37bf47d64dc93748949658b977b/docs/ARCHITECTURE.md) |

### Exact dependencies

```json
{
  "npm": {
    "@kujolang/kujo-runtime": "1.9.0",
    "@openai/codex": "0.144.4",
    "playwright": "1.61.1"
  },
  "overrides": {},
  "source_lock": {
    "schema": "kujo.webops-factory.sources/v1",
    "repositories": {
      "siteprobe": {
        "url": "https://github.com/kujolang/siteprobe.git",
        "commit": "957ce6b72b2a1c2f1a46650a33bdc44498ddcc96"
      },
      "lens": {
        "url": "https://github.com/kujolang/lens.git",
        "commit": "91049646d70c11bf0c6071f39cf7dfac6b1ba70b"
      },
      "kujo-agents": {
        "url": "https://github.com/kujolang/kujo-agents.git",
        "commit": "a7e9d0236d6e64b5db30273b32f4ad8c124f5173"
      },
      "kujo-workflows": {
        "url": "https://github.com/kujolang/kujo-workflows.git",
        "commit": "d766eae4fd9a131e51c34796d029fd3bc6974689"
      }
    }
  }
}
```

## Product Launch Factory

Repository: [product-launch-factory](https://github.com/kujolang/product-launch-factory); remote main `d61c7021b0469c45f909b8371205f0df3afbac8b`. Package version `0.1.0` is separate from GitHub release status.

| Field | Verified scope | Evidence |
| --- | --- | --- |
| Audience | Product teams preparing consistent editorial, website and video deliverables from existing product evidence. | [README.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/README.md), [AGENT-SETUP.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/AGENT-SETUP.md) |
| Input | kujo.product-launch.brief/v1: captured text sources with HTTPS provenance, audience/objective/voice/constraints, software-export or webops-package evidence, up to three PNG/JPEG product visuals with rights; silent video default, narration separate. | [launch-brief.json](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/schemas/launch-brief.json), [webops-launch.json](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/examples/webops-launch.json), [AGENT-SETUP.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/AGENT-SETUP.md) |
| Roles | Five stations: Source evidence verifies existing package; Publishing House commissions/writes/reviews/adapts; WebOps inspects bounded landing repairs; VideoOps plans/compiles/renders/checks; Launch review collects versions and awaits human approval. Uses child roles rather than a new universal worker team. | [README.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/README.md), [launch.py](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/src/launch.py), [ARCHITECTURE.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/ARCHITECTURE.md) |
| Execution | Python coordinator freezes brief/evidence, invokes pinned child adapters, constructs static landing page from escaped editorial data and passes checked screenshots/facts to VideoOps. Software adapter invokes evidence.mjs verify only, never application construction. | [launch.py](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/src/launch.py), [video.mjs](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/src/video.mjs), [ARCHITECTURE.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/ARCHITECTURE.md) |
| Outputs | Local package with article, newsletter, three social posts, landing website, MP4, editable composition and underlying evidence. Export strips private homes and omits local approval. | [launch.py](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/src/launch.py), [AGENT-SETUP.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/AGENT-SETUP.md), [manifest.json](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/example-run/package/manifest.json) |
| Evidence | kujo.product-launch.handoff/v1 records input hashes, factory revisions, output inventory and prior dependency hashes. Exact package manifest and approval checks detect edited, added or deleted files. Recorded example includes 200 packaged files. | [launch.py](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/src/launch.py), [core.py](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/src/core.py), [package.json](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/example-run/handoffs/package.json) |
| Review | Technical/model gates remain child-specific. Completed handoffs reused only with matching bytes; changed input needs new version, invalidates downstream review. Human reads every deliverable and plays full video before exact-hash local approve command; no publication authority. | [AGENT-SETUP.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/AGENT-SETUP.md), [core.py](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/src/core.py), [VERIFICATION.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/VERIFICATION.md) |
| Boundaries | Local trusted single operator; confined source paths and trusted pinned child execution, no arbitrary repository builds. Loopback read-only floor; generated previews block scripts/external assets/forms. Sources sent to configured model. Paid speech requires exact authorization and budget. | [SECURITY.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/SECURITY.md), [video.mjs](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/src/video.mjs), [launch.py](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/src/launch.py) |
| Dependencies | Pinned Publishing House, WebOps and VideoOps factories plus newer Software Factory evidence-verifier commit 259aff26e3ca627873eec6b40a89d6942b039d7c (not public Software 0.1.0). Direct npm Codex 0.144.4 and Playwright 1.61.1; child locks determine inherited tools. | [sources.lock.json](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/sources.lock.json), [package.json](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/package.json), [setup.py](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/scripts/setup.py) |
| Demo | Approved v0.1.0 coordinator demo: releases/download/v0.1.0/launch.mp4; 31.6s, 1920×1080, 30fps; SHA 60102b8d687173399387df3cd4bb1f4e37446538ef7705cabc524e94dc28fa45. Owner presentation approval recorded in release notes; raw technical ledger still REVIEW_INCOMPLETE and no independent listening attestation. Underlying example campaign remains unapproved. | [v0.1.0.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/releases/v0.1.0.md), [README.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/demo/README.md), [manifest.json](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/media/product-launch-demo/manifest.json) |
| Setup | macOS/Linux; Git, Python 3.10+, Node 26.12.1, npm, FFmpeg/ffprobe, Chromium OS libraries; Codex login/model allowance for live work. npm ci; setup; login; doctor; factory -- run examples/webops-launch.json; npm start. npm run demo; npm start gives read-only recorded replay without model calls. Floor 4384. | [README.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/README.md), [AGENT-SETUP.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/AGENT-SETUP.md) |
| Limitations | No new software application creation, automatic campaign publication or deployment. Silent default; speech requires explicit separate authorization. Recorded campaign awaiting editorial/listening approval is distinct from approved coordinator presentation. Hashes prove identity, not truth/authorship. | [v0.1.0.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/releases/v0.1.0.md), [SECURITY.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/SECURITY.md), [VIDEO.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/VIDEO.md) |
| Relationships | Coordinator of existing domain factories through exact-version handoffs. Software Factory remains standalone and supplies existing export verification only. Child pins may differ from independently public factory releases. | [sources.lock.json](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/sources.lock.json), [launch.py](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/src/launch.py), [ARCHITECTURE.md](https://github.com/kujolang/product-launch-factory/blob/d61c7021b0469c45f909b8371205f0df3afbac8b/docs/ARCHITECTURE.md) |

### Exact dependencies

```json
{
  "npm": {
    "@openai/codex": "0.144.4",
    "playwright": "1.61.1"
  },
  "overrides": {},
  "source_lock": {
    "schema": "kujo.product-launch.sources/v1",
    "repositories": {
      "publishing-house-factory": {
        "url": "https://github.com/kujolang/publishing-house-factory.git",
        "commit": "38e7900a16f8482d12ad6b8b6a15f538d7ee3099"
      },
      "webops-factory": {
        "url": "https://github.com/kujolang/webops-factory.git",
        "commit": "a2aba2c63777f37bf47d64dc93748949658b977b"
      },
      "videoops-factory": {
        "url": "https://github.com/kujolang/videoops-factory.git",
        "commit": "dcf2dc4fa7311f59ba3dd16f58a227439a155979"
      },
      "software-factory": {
        "url": "https://github.com/kujolang/software-factory.git",
        "commit": "259aff26e3ca627873eec6b40a89d6942b039d7c"
      }
    }
  }
}
```

## Release and evidence distinctions

- Software Factory public `0.1.0` and remote main matched at research time. Local feature-branch integration changes were deliberately excluded. Spec, Eval, ShipCheck, RunLedger, Casefile and broader catalogs must not be described as shipped by this release.
- Product Launch pins a later Software Factory verifier source than the standalone published release. That source boundary is deliberate and must remain visible in research.
- VideoOps, Publishing House and WebOps package manifests say 0.1.0, but the GitHub releases API returned no releases. Public pages must say source preview, not latest release.
- Product Launch coordinator presentation approval is explicitly recorded by the owner in release notes. The retained video technical manifest still says REVIEW_INCOMPLETE; owner acceptance does not create a listening attestation or campaign approval.
- Product Launch onboarding receipt measures commit `5f5c697f9734b2c7ccb347993c19492ba4956325`: 67.073 seconds before login and 69.625 seconds total, 23 tests, empty application caches on Ubuntu 24.04. Git, Node and Python were provisioned first. Sign-in and live model calls were excluded. This is retained qualification evidence, not a new benchmark of release HEAD.
- A checked-in CI workflow documents intended checks. It does not itself prove a successful run. Source-reported qualification evidence remains distinct from website verification.

## Research verification

The Product Launch release checkout passed 12 Python and 11 Node contract tests on Node 26.12.1 during this audit, with no provider calls. This independently confirms the 23-test count; it does not repeat the fresh Ubuntu installation measurement. See [the research check receipt](research-verification.json).
