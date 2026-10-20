"""Check retained evidence integrity and the narrow claims made in README.md.

This does not rerun a competitor or establish coverage beyond captured fixtures.
"""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
checks = []
def require(label, condition):
    checks.append({'claim': label, 'passed': bool(condition)})

def load(name):
    return json.loads((root / (name + '-receipts.json')).read_text())['cases']

def case(rows, args, exit_code=None):
    return [r for r in rows if r['args'] == args and (exit_code is None or r['exit'] == exit_code)]

for name, digest in json.loads((root / 'sha256.json').read_text()).items():
    require('hash: ' + name, hashlib.sha256((root / name).read_bytes()).hexdigest() == digest)
bend, baml, zero = (load(n) for n in ('bend', 'baml', 'zero'))
require('Bend valid proof accepted', case(bend, ['good-proof.bend', '--check-only'], 0))
for name in ('bad-proof', 'bad-type', 'bad-affine', 'open-law'):
    require('Bend rejects ' + name, case(bend, [name + '.bend', '--check-only'], 1))
for args in (['arithmetic.bend'], ['node', 'arithmetic.js'], []):
    require('Bend arithmetic: ' + repr(args), any(r['stdout'].strip() == '42' for r in case(bend, args, 0)))
require('Bend independent verdict unavailable', any('v4.34.0' in r['stderr'] and 'BENDTT' in r['stderr'] for r in case(bend, ['good-proof.bend', '--verdict'], 1)))
require('BAML function returns 42', any(r['stdout'].strip() == '42' for r in case(baml, ['run', 'total'], 0)))
require('BAML one assertion passes', any('1 passed' in r['stderr'] for r in case(baml, ['test'], 0)))
require('BAML wrong assertion fails', any('right = 41' in r['stderr'] for r in case(baml, ['test'], 2)))
require('BAML type mismatch rejected', any('expected `int`' in r['stderr'] for r in case(baml, ['check'], 4)))
require('BAML generator completed', case(baml, ['generate'], 0))
require('BAML packaging remains environment-blocked', any('No space left on device' in r['stderr'] for r in case(baml, ['pack', 'total', '--output', './total-packed'], 4)))
require('Zerolang greeting runs', any(r['stdout'].strip() == 'hello from zero' for r in case(zero, ['run'], 0)))
require('Zerolang test count is nonzero', any(r['stdout'].strip() == '1 test(s) ok' for r in case(zero, ['test'], 0)))
require('Zerolang wrong expectation fails', any('wrong expectation' in r['stderr'] for r in case(zero, ['test'], 1)))
for code in ('GPH002', 'TYP003'):
    require('Zerolang rejects and preserves graph: ' + code, any(r['args'][0] == 'patch' and r['exit'] != 0 and code in r['stdout'] and r.get('graphUnchanged') is True for r in zero))
require('Zerolang export succeeds after sandbox correction', case(zero, ['export', '--json'], 0))
require('Zerolang projection matches', case(zero, ['verify-projection', '--json'], 0))
require('Zerolang edited projection rejected', zero[-1]['args'] == ['verify-projection', '--json'] and zero[-1]['exit'] == 1 and 'RGP006' in zero[-1]['stdout'])
result = {'passed': all(c['passed'] for c in checks), 'checks': len(checks), 'failures': [c for c in checks if not c['passed']], 'scope': 'Captured evidence integrity and bounded reported outcomes; not a runtime rerun.'}
print(json.dumps(result, indent=2))
raise SystemExit(0 if result['passed'] else 1)
