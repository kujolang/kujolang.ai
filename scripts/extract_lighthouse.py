#!/usr/bin/env python3
"""Normalize Lighthouse JSON receipts into the audit performance CSV."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


FIELDS = [
    "phase", "url", "template", "run_date", "environment", "lighthouse_version",
    "html_bytes", "css_bytes", "js_bytes", "image_bytes", "font_bytes", "requests",
    "lcp_ms", "inp_ms", "cls", "ttfb_ms", "source", "notes",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-dir", required=True)
    args = parser.parse_args()
    audit = Path(args.audit_dir).resolve()
    raw = audit / "raw" / "performance"
    rows = []
    for receipt_path in sorted(raw.glob("*.json")):
        phase, template = receipt_path.stem.split("-", 1)
        report = json.loads(receipt_path.read_text(encoding="utf-8"))
        audits = report.get("audits", {})
        requests = audits.get("network-requests", {}).get("details", {}).get("items", [])
        totals = {"Document": 0, "Stylesheet": 0, "Script": 0, "Image": 0, "Font": 0}
        for request in requests:
            kind = request.get("resourceType", "")
            if kind in totals:
                totals[kind] += int(request.get("transferSize") or 0)
        rows.append({
            "phase": phase,
            "url": report.get("finalDisplayedUrl") or report.get("finalUrl") or report.get("requestedUrl"),
            "template": template,
            "run_date": report.get("fetchTime", ""),
            "environment": "local static output; Lighthouse mobile simulated throttling",
            "lighthouse_version": report.get("lighthouseVersion", ""),
            "html_bytes": totals["Document"], "css_bytes": totals["Stylesheet"],
            "js_bytes": totals["Script"], "image_bytes": totals["Image"],
            "font_bytes": totals["Font"], "requests": len(requests),
            "lcp_ms": audits.get("largest-contentful-paint", {}).get("numericValue", ""),
            "inp_ms": "NOT AVAILABLE — DATA ACCESS REQUIRED",
            "cls": audits.get("cumulative-layout-shift", {}).get("numericValue", ""),
            "ttfb_ms": audits.get("server-response-time", {}).get("numericValue", ""),
            "source": f"raw/performance/{receipt_path.name}",
            "notes": "Lab run; not field Core Web Vitals. One run per representative template.",
        })
    with (audit / "performance.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Normalized {len(rows)} Lighthouse receipts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
