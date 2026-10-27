"""Carry verified unchanged application gates into a focused browser-test retry."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
log=(root/'.loop-engineering/evidence/language-first-run-03/001/eval.log').read_text()
gates=['examples_source','examples_runtime','node_tests','build','responsive','site_contract','generated_output','language_contract','social','comparisons','javascript','shell','audit','diff']
for gate in gates: assert f'gate {gate}: pass' in log,gate
for path,digest in json.loads((root/'.loop-engineering/evidence/verified-application-sha256.json').read_text()).items():
 assert hashlib.sha256((root/path).read_bytes()).hexdigest()==digest,'Application changed since full evaluation: '+path
print('All 14 non-browser full-run gates passed; application source and generated artifact unchanged')
