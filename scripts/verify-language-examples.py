import hashlib,json,os,pathlib,subprocess,tempfile,tarfile,atexit
root=pathlib.Path(__file__).resolve().parents[1];c=json.loads((root/'examples/catalog.json').read_text());binary=os.environ.get('KUJO_BIN','kujo')
assert subprocess.check_output([binary,'--version'],text=True).strip()=='kujo '+c['version']
# Run the downloadable bundle in an isolated directory, including replay fixtures.
binary=str(pathlib.Path(binary).resolve()) if '/' in binary else binary
temporary=tempfile.TemporaryDirectory();atexit.register(temporary.cleanup)
samples=pathlib.Path(temporary.name)
with tarfile.open(root/'public/samples/kujo-examples.tar.gz') as archive:
 for member in archive.getmembers():
  destination=samples/member.name
  assert member.isfile() and destination.resolve().is_relative_to(samples.resolve()),member.name
  destination.parent.mkdir(parents=True,exist_ok=True)
  destination.write_bytes(archive.extractfile(member).read())
seen=set()
for x in c['items']:
 assert x['slug'] not in seen;seen.add(x['slug']);p=samples/f"{x['slug']}.kujo"
 assert hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'],x['slug']
 assert x['mode'] in ['run','check','test-run']
 subprocess.run([binary,'check',p.name],cwd=p.parent,check=True,capture_output=True,timeout=20)
 result=subprocess.run([binary,x['mode'],*x.get('args',[]),p.name],cwd=p.parent,check=True,capture_output=True,text=True,timeout=20)
 if x['mode']=='run': assert result.stdout==x['expected'],(x['slug'],result.stdout)
 print(x['slug']+': '+x['mode']+' passed')
print(f'{len(seen)} pinned examples verified')

denied=subprocess.run([binary,'run','--untrusted','capabilities.kujo'],cwd=samples,capture_output=True,text=True,timeout=20)
assert denied.returncode != 0 and 'Capability denied' in denied.stderr
print('AI capability denied without grant and allowed with explicit grant')

# Exercise the actual routing helper, including rejected traversal-like inputs.
import tempfile
build=(root/'build.kujo').read_text()
helpers=build[build.index('func clean_slug('):build.index('func markdown_files(')]
assertions='\n'.join('assert_equal(custom_slug_override({"custom_url": '+json.dumps(value)+'}), '+json.dumps(expected)+')' for value,expected in [('examples/hello-world','examples/hello-world'),('../escape',''),('examples/../escape',''),('examples//hello',''),('/absolute',''),('examples/Hello',''),('examples/hello.kujo',''),('examples/','')])
with tempfile.TemporaryDirectory() as temporary:
 path=pathlib.Path(temporary)/'routes.kujo';path.write_text(helpers+'\n'+assertions)
 subprocess.run([binary,'run',str(path)],check=True,capture_output=True,text=True,timeout=20)
print('Nested page route acceptance and traversal rejection passed')
