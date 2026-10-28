# Evaluation record

The first run stopped during responsive image generation when the filesystem returned ENOSPC. It produced no verdict. Baseline receipts stayed intact; the next disk check showed 10 GiB available. Only this task's redundant Howl repeat render was removed.

`acceptance/` passed all 21 gates for the initial implementation. Its first lab comparison then revealed a duplicate image transfer: the responsive homepage hero and the hidden video poster fetched different sizes. That evidence is preserved under seo-audit/2026-10-28/raw/performance-intermediate/.

The poster now loads on video-open and video preload is none. `final/` rebuilt the site and all responsive assets successfully; it exposed two stale test assumptions: the site contract required the old preload=metadata, and a newly added browser test deliberately aborted the video request while also requiring zero console errors. Both test assumptions were corrected without relaxing the intended behavior: the site contract now requires deferred poster markup; the browser uses the actual video resource and checks open/close/focus restoration.

`verified/` reran runtime, Node, browser, schema, source freshness and other checks against 3,170 unchanged production-source/output hashes. Its sole failure was the already-observed preload contract assertion, evaluated before that assertion was updated. `closeout/` rechecks the corrected site contract, shell syntax, diff whitespace and immutable build hashes. No production source/output changed between the final build and closeout. The combined gate receipt records the successful evidence for every required gate; historical failures are retained.

Earlier workflow directories remain unchanged. The browser scripts' default output initially touched old evidence paths; new receipts were copied into this audit's acceptance directory, tracked old receipts restored, and subsequent runs used dedicated paths.
