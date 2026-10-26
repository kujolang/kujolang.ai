# Watchdog screenshot provenance

Captured from the unmodified Watchdog dashboard on 2026-10-26, using synthetic
records in `/tmp/watchdog-showcase-20261026/demo.db` and a loopback server on port
7791. No live telemetry or provider calls were used. See receipt.json for seed totals.

Reproduce with `scripts/seed-watchdog-showcase.py DEMO_DB WATCHDOG_REPO` after
starting Watchdog against an empty database named `demo.db` inside a directory
containing `showcase`. Set WDG_HOST=127.0.0.1, a spare WDG_PORT, WDG_DB_PATH,
WDG_PROXY_CONFIG_PATH, WDG_SOURCES_CONFIG_PATH, WDG_EXPORTERS_CONFIG_PATH and
WDG_BACKUP_DIR to that isolated directory; set WDG_BACKUP_ENABLED=false.
The seeder refuses nonempty request tables and uses only the checked-in pricing
catalog. Do not point these paths at an existing installation.

Select Last 30 days. Its calendar-aligned date filter omits the partial first day
of the rolling 30-day seed: the captured view contains 199,025 requests,
24,026,933,218 tokens, and $21,398.1514 estimated direct API value. The dashboard
formats billions as millions (24026.9M). Costs are estimates, not invoices.

Capture the overview and request/session dialogs through the browser. The
request image scrolls to input/output usage; the session image shows related
requests and tools. The overview is a 1274 × 1180 capture; dialog images use the
normal viewport. No values or UI elements were altered for the screenshots.

Source revision: kujolang/watchdog b0a682a3a0beaa7482b34e83245c607de81d260d.
The site builder escapes raw HTML in Markdown. The Watchdog-only gallery marker
is replaced with templates/watchdog-gallery.html after Markdown rendering.
