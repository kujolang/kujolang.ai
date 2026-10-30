"""Verify the authorized Pages run and every new public route after deployment."""
import concurrent.futures,json,os,pathlib,subprocess,urllib.request
root=pathlib.Path(__file__).resolve().parents[1]
run_id=os.environ['KUJO_PAGES_RUN_ID']
run=json.loads(subprocess.check_output(['gh','api',f'repos/kujolang/kujolang.ai/actions/runs/{run_id}'],text=True))
assert run['status']=='completed' and run['conclusion']=='success', (run['status'],run['conclusion'])
c=json.loads((root/'examples/catalog.json').read_text())
routes=['/','/language/','/examples/','/development-workflow/','/performance/','/ecosystem/','/compare/']+['/examples/'+x['slug']+'/' for x in c['items']]
workflows=json.loads((root/'workflows/catalog.json').read_text())
workflow_routes=['/examples/'+x['slug']+'/' for x in workflows['items']]
routes+=workflow_routes
def verify(route):
 url='https://kujolang.ai'+route
 req=urllib.request.Request(url,headers={'User-Agent':'Kujo-site-release-verification','Cache-Control':'no-cache'})
 with urllib.request.urlopen(req,timeout=30) as response:
  assert response.status==200;html=response.read().decode()
 assert f'<link rel="canonical" href="{url}">' in html,route
 assert '<meta property="og:image"' in html,route
 if route=='/': assert 'data-code-explorer' in html and 'Get Started' in html
 if route=='/examples/': assert 'example-search' in html
 if route in workflow_routes: assert 'Source and verification' in html and 'Connect a live provider' in html
 if route.startswith('/examples/') and route!='/examples/' and route not in workflow_routes: assert c['commit'] in html and 'Pinned source' in html
 return dict(route=route,status=200,canonical=url)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: results=list(pool.map(verify,routes))
receipt=dict(run_id=run['id'],run_url=run['html_url'],deployed_commit=run['head_sha'],conclusion=run['conclusion'],routes=results)
path=pathlib.Path(os.environ.get('KUJO_RELEASE_RECEIPT',str(root/'.loop-engineering/release/evidence/production.json')));path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(receipt,indent=2)+'\n')
print(f"Pages run {run['id']} succeeded for {run['head_sha']}; {len(results)} public routes verified")
