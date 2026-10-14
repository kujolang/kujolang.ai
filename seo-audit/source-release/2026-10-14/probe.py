"""Read-only release URL probes with response and redirect evidence."""
import subprocess,json,sys,concurrent.futures
from pathlib import Path
root=Path(__file__).parent/'raw';phase=sys.argv[1]
urls=['https://kujolang.ai/ecosystem/source/','http://kujolang.ai/ecosystem/source/','https://www.kujolang.ai/ecosystem/source/','https://kujolang.ai/ecosystem/source','https://kujolang.ai/ecosystem/source/?release=v0.1.0','https://docs.kujolang.ai/tools/source/','https://kujolang.ai/robots.txt','https://kujolang.ai/sitemap.xml','https://docs.kujolang.ai/robots.txt','https://docs.kujolang.ai/sitemap.xml','https://kujolang.ai/assets/images/ecosystem/source-review-evidence-vault.webp','https://kujolang.ai/assets/images/social/source.jpg','https://github.com/kujolang/source/releases/tag/v0.1.0','https://mcp.kujolang.ai/health']
def probe(pair):
 i,url=pair
 r=subprocess.run(['curl','--silent','--show-error','--location','--max-time','40','--dump-header',str(root/f'{phase}-{i}.headers'),'--output',str(root/f'{phase}-{i}.body'),'--write-out','%{json}',url],capture_output=True,text=True)
 try:d=json.loads(r.stdout)
 except ValueError:d={}
 return dict(url=url,status=d.get('http_code'),effective_url=d.get('url_effective'),redirects=d.get('num_redirects'),seconds=d.get('time_total'),bytes=d.get('size_download'),error=r.stderr,exit_code=r.returncode)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(probe,enumerate(urls)))
(root/f'{phase}-probes.json').write_text(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
