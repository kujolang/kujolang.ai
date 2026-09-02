#!/usr/bin/env python3
import argparse
import pathlib
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument("--origin", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()
origin = args.origin.rstrip("/")
output = pathlib.Path(args.output)
output.mkdir(parents=True, exist_ok=True)
def request(url):
    error = None
    for attempt in range(3):
        try:
            return urllib.request.urlopen(
                urllib.request.Request(url, headers={"User-Agent": "KujolangSEOAudit/1.0"}),
                timeout=30,
            ).read()
        except Exception as current_error:
            error = current_error
            if attempt < 2:
                time.sleep(attempt + 1)
    raise error
sitemap = request(origin + "/sitemap.xml")
(output / "sitemap.xml").write_bytes(sitemap)
root = ET.fromstring(sitemap)
urls = [node.text for node in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
for url in urls:
    path = urllib.parse.urlparse(url).path.strip("/")
    destination = output / path / "index.html" if path else output / "index.html"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(request(url))
for name in ("robots.txt", "llms.txt"):
    (output / name).write_bytes(request(origin + "/" + name))
print(f"downloaded {len(urls)} canonical pages")
