# Factories website integration inventory

Baseline: clean `main` at `5fad198eadcb5fcff0b185c952ca8748d7bb5ba1`, tracking `origin/main`. `CNAME` declares `kujolang.ai`; the production build uses `https://kujolang.ai`, and documentation remains `https://docs.kujolang.ai`. GitHub Pages publishes verified output on pushes to `main`. Work is isolated on `feat/factories-ecosystem`, which does not trigger the production deployment workflow. A pushed implementation branch is not evidence of deployment.

This inventory records source changes and editorial decisions. Passing checks, browser results and CI observations belong in the final verification record; inclusion here is not a claim that those checks passed.

## Routes

| Canonical URL | Source | Purpose |
| --- | --- | --- |
| https://kujolang.ai/ecosystem/factories/ | `content/pages/factories.md`, `templates/factories-intro.html` | Category introduction, five-product comparison, coordination explanation and getting started |
| https://kujolang.ai/ecosystem/software-factory/ | `content/ecosystem/90-software-factory.md` | Published standalone 0.1.0 software candidate workflow |
| https://kujolang.ai/ecosystem/videoops-factory/ | `content/ecosystem/91-videoops-factory.md` | Pinned source-preview video workflow and review boundary |
| https://kujolang.ai/ecosystem/publishing-house-factory/ | `content/ecosystem/92-publishing-house-factory.md` | Pinned source-preview editorial package workflow |
| https://kujolang.ai/ecosystem/webops-factory/ | `content/ecosystem/93-webops-factory.md` | Pinned source-preview static-copy repair workflow |
| https://kujolang.ai/ecosystem/product-launch-factory/ | `content/ecosystem/94-product-launch-factory.md` | Published v0.1.0 coordinator, approved demonstration and exact-version handoffs |

## Surface decisions

| Surface | Disposition | Reason / implementation |
| --- | --- | --- |
| Homepage | Added | Dedicated section after existing language/tool proof, linking the category, software candidate and launch coordinator. Language remains the hero and final getting-started identity. |
| Desktop navigation | Added | `build_navigation` adds Factories beside Ecosystem; visitors can find the category directly. |
| Mobile navigation | Added through shared navigation | The mobile drawer and desktop header consume the same `navigation` markup in `templates/layout.html`; no separate link list can drift. |
| Footer | Added | Category link beside Ecosystem, preserving existing destinations. |
| Ecosystem index | Added | Dedicated Factories section and five cards from entries with `section: Factories`. |
| Ecosystem category | Added | Substantive landing page with cards, native accessible comparison table, five-station sequence and scoped onboarding. Existing Primitives, Tooling, Showcase, Skills and Workflows routes remain. |
| Factory detail pages | Added | Shared `post-factory.html` template and per-product media fragments; input, workflow, outputs, evidence, review, prerequisites, first run, limitations, related tools and final CTA. |
| Existing tool details | Added focused links | Dispatch/Workcell link Software Factory; Lens/SiteProbe link WebOps; StoryDesk/Dossier/BluePencil/GalleyPack/VersionSeal link Publishing House. Each names the actual relationship, without generic powered-by claims. |
| Workflow pages | Intentionally unchanged | Factory pages link the canonical Publishing House Operator and category links workflow collection. Generated workflow catalogs retain their own contracts, counts and release scope. |
| Agent-related pages | Intentionally unchanged | Existing agent-system carousel remains. Factory copy explains actual role participation and direct source provenance; no unsupported universal controller claim is added. |
| Skills pages | Intentionally unchanged | Category links existing guidance collection. Factory runtime capability must not be inferred from a skill's presence or instructions. |
| Getting started | Added within category/detail pages | Choose a bounded domain, install pinned revision, run checks, inspect recording, then authorize live work. Language installation journey remains focused on writing Kujo programs. |
| Documentation links | Added pinned authoritative references | Each factory links its exact setup guide, source revision and relevant release evidence. `docs.kujolang.ai` navigation remains unchanged; no unverified documentation route is invented. |
| Examples | Intentionally unchanged | Factory examples link to their authoritative repositories and named input contracts. Existing language examples and downloadable bundles retain their source contracts. |
| Showcases | Intentionally unchanged | Factories get a separate category rather than being inserted into the application showcase count. Authentic floor screenshots and canonical demos live on factory pages. |
| Search | Included through normal discovery generation | Canonical content enters the existing `.well-known/kujo-site-index.json`; regression checks require unique entries for all six routes. No competing search index is introduced. |
| Related content | Added focused cross-links | Factories link genuine child factories and tools; selected tool pages link back. Existing unrelated recommendations remain unchanged. |
| Comparison pages | Intentionally unchanged | Language comparisons retain their subject. The factory comparison belongs on the category landing page and does not invent feature parity. |
| Social previews | Added | Six dedicated Howl cards use matching artwork, route titles/descriptions and existing font/layout conventions. |
| Sitemap | Included through normal SSG routes | The content model emits all six canonical routes; regression checks cover inclusion and preserved existing ecosystem routes. |
| Canonical and structured metadata | Existing SSG path reused | Frontmatter supplies titles/descriptions/images; normal layout emits canonical, Open Graph, X/Twitter and JSON-LD metadata. No new schema type or unsupported properties. |
| Machine-readable discovery | Existing SSG path reused | Content participates in existing public site index and `llms.txt` generation. Internal research matrix remains under repository documentation, not marketing catalog data. |
| Feed | Intentionally unchanged | Factory product pages are not dated Writing posts; no artificial feed entries are created. |
| Synchronization | Preserved canonical source | Existing catalog sync owns skills/workflows, not ecosystem Markdown. Regression test runs synchronization against temporary real Git catalogs and checks factory sources/cards survive. |
| Responsive media | Existing image workflow reused | New heroes and floors use established images; native video controls with posters and low-preload behavior avoid loading large demonstrations before interaction. |
| Accessibility | Native patterns reused | Semantic headings/table, keyboard-scroll comparison region, controls, fallback links, explicit recorded/preview labels and shared mobile menu. Actual browser/axe results must be reported separately. |
| Deployment configuration | Unchanged | CNAME/domain/Pages deployment target remain intact. Feature-branch push does not claim production publication. |

## Content boundaries checked

The five detail pages were compared with [the capability matrix](capability-matrix.md). Corrections distinguish the issue-tracker default contract from software packs; state macOS/Colima's observed isolation qualification; retain VideoOps full listening review and host execution boundary; describe Publishing source intake and installed-but-inactive components; distinguish WebOps's full imported-page static audit from bounded SiteProbe crawl; and state Product Launch's silent default, separate narration authority and later software-verifier pin.

The source matrix uses public repository revisions and retained public evidence only. Local uncommitted factory work is excluded. The Software Factory feature-integration report is a public pinned-source boundary reference, not a released capability claim.
