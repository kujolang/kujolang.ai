"""Verify retained receipts; reproducing a defect is not a healthy runtime pass."""
from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
rows=json.loads((p/'probe-results.json').read_text());r={x['name']:x for x in rows};assert len(r)==32
expected_returns={'int':('int','42'),'string':('str',"'wrong'"),'numeric-string':('str',"'42'"),'bool':('bool','True'),'float':('float','1.5'),'null':('NoneType','None'),'list-to-int':('list',"[1, 'bad']"),'async-string':('str',"'wrong'"),'list-valid':('list','[1, 2]'),'list-invalid-member':('list',"[1, 'bad']"),'plus-valid':('int','42'),'field-forged':('str',"'bad'")}
for name,(kind,value) in expected_returns.items():
 x=r[name];v=json.loads(x['stdout']);assert x['exit']==0 and (v['kind'],v['type'],v['repr'])==('return',kind,value),name
for name in ['model-valid','model-coercion','class-return-valid','class-dict','parse-valid','parse-coercion','parse-wrong-domain']:
 x=r[name];v=json.loads(x['stdout']);assert x['exit']==0 and v==dict(kind='return',type='Answer',repr='Answer(value='+('41' if name=='parse-wrong-domain' else '42')+')'),name
errors={'optional-invalid':'TypeError','missing-arg':'BamlError','unknown-arg':'BamlError','duplicate-arg':'TypeError','unsupported-object':'TypeError','large-int':'TypeError','model-invalid':'ValidationError','strict-model':'ValidationError','class-return-forged':'ValidationError','constructed-return-invalid':'ValidationError','parse-invalid':'BamlError','strict-host-wrapper':'ValidationError'}
for name,kind in errors.items():
 x=r[name];v=json.loads(x['stdout']);assert x['exit']==0 and (v['kind'],v['type'])==('error',kind),name
assert 'baml.errors.ParseError' in r['parse-invalid']['stdout']
assert r['plus-invalid']['exit']==-11
f={x['name']:x for x in json.loads((p/'followup-results.json').read_text())}
assert f['crash-unsandboxed']['exit']==-11 and 'Segmentation fault' in f['crash-unsandboxed']['stderr']
assert f['valid-unsandboxed']['stdout'].strip()=='42' and f['valid-unsandboxed']['exit']==0
assert f['mutated-field']['stdout'].strip()=="'bad'" and f['mutated-field']['exit']==0
assert f['mutated-class-return']['exit']==1 and 'ValidationError' in f['mutated-class-return']['stderr']
assert f['strict-wrapper-valid']['exit']==0 and f['strict-wrapper-valid']['stdout'].strip()=='42'
assert all(f['baml-check-'+k]['exit']==2 for k in ['good','bad'])
c={x['name']:x for x in json.loads((p/'compiler-results.json').read_text())};assert c['good']['exit']==0 and c['bad']['exit']==4 and 'E0001' in c['bad']['stderr']
assert 'Success:' in (p/'mypy-valid.txt').read_text() and '[arg-type]' in (p/'mypy-invalid.txt').read_text()
manifest=json.loads((p/'sha256.json').read_text())
for file,digest in manifest.items():assert hashlib.sha256((p/file).read_bytes()).hexdigest()==digest,file
print(json.dumps({'retainedRuntimeCases':32,'additionalRuntimeObservations':5,'compilerChecks':2,'staticChecks':2,'unsupportedCommandAttemptsExcluded':2,'filesVerified':len(manifest),'evidenceMatchesRecordedOutcomes':True,'upstreamCrashResolved':False},indent=2))
