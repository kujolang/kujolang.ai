# Homepage and Examples editorial refinement

Scope: homepage, Examples index and all 21 example detail pages. This is a new bounded refinement; earlier Loop runs and the root loop.yml remain preserved.

## Workflow and design

The installed Loop Engineering skill and native runner were inspected before implementation. Existing repository architecture and generators were retained. The agent applied the requested edits, then invoked the native workflow with a separate task configuration and all 16 required gates. The runner's action hook is unused because implementation occurred in the agent's edit phase; its evaluation artifacts provide the acceptance record. No generated verdict is manually changed.

The homepage now has a spacious hero, shared content edges, centered section titles and no numbered section eyebrows. Display titles use Departure Mono; code retains conventional monospace. The gray tools backdrop and redundant hero/runtime/tools prose are removed. The final call to action spans the page in black and white. The common footer remains visible.

Copy icons remain absolutely positioned inside code blocks. A right gutter keeps the control clear of code, without reserving a blank top row. Success feedback is plain text and clears after 1,500ms; failure feedback remains available for manual copying.

## Orwell writing review

Applied /Users/robertdevore/.agents/skills/orwell-writing/SKILL.md as an editorial procedure. The skill supplies prose guidance, not an executable writing script. Reviewed the homepage, catalog descriptions/notes and shared index/detail copy for direct language, useful specifics and unnecessary abstraction. Generated HTML and Markdown from the edited source.

Representative edits:

- Hero: describes scripts, services, local execution and replay directly.
- Installation heading: replaced the uneven “Install. Check. Run.” stack with “Run your / first script.”
- Index: “Find a small program you can read, run and change.”
- Output introduction: “Your terminal should show this output.”
- Check-only note: “We checked the source but did not run the full application.”
- Files and HTTP notes retain explicit execution limits; the HTTP note correctly states that the upstream sample skips server startup in automatic VM runs.

Technical promises were preserved: Node.js requirements, supported platforms, live-provider credentials/cost caveats, sample verification modes, pinned provenance and hashes. Runnable/downloadable source bytes were not edited.

## Verification scope

Native gate logs and verdict are under ../iterations/001/. Browser evidence includes desktop/tablet/mobile homepage and Examples screenshots, accessibility results, exact clipboard contents, all 21 detail routes, no-JavaScript fallback, shared content alignment, display/code font separation and transient copy feedback. The larger hero intentionally supersedes the former requirement to show code within the first viewport.
