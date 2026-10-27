"""Measure process startup plus one pinned script, never cross-language speed."""
import hashlib,json,os,pathlib,platform,statistics,subprocess,time,datetime
root=pathlib.Path(__file__).resolve().parents[1]
binary=os.environ.get('KUJO_BIN','kujo')
sample=root/'public/samples/functions.kujo'
version=subprocess.check_output([binary,'--version'],text=True).strip()
assert version=='kujo 1.9.0',version
runs=[]
for _ in range(10):
 start=time.perf_counter();out=subprocess.check_output([binary,'run',str(sample)],text=True);runs.append((time.perf_counter()-start)*1000)
 assert out=='total: 42\n',out
receipt=dict(scope='process startup plus script execution; no cross-language comparison',runtime=version,os=platform.platform(),architecture=platform.machine(),cpu=subprocess.check_output(['sysctl','-n','machdep.cpu.brand_string'],text=True).strip() if platform.system()=='Darwin' else platform.processor(),measured_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),command='kujo run public/samples/functions.kujo',source_sha256=hashlib.sha256(sample.read_bytes()).hexdigest(),samples_ms=runs,median_ms=statistics.median(runs))
(root/'public/samples/performance.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
