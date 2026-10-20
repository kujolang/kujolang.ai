import subprocess, pathlib, json, os, platform
p=pathlib.Path(__file__).resolve().parent
out=pathlib.Path(os.environ.get("EVIDENCE_DIR", str(p/"results")));out.mkdir(exist_ok=True)
cases=[]
def run(name,args,exit=0,contains=None):
 try:
  r=subprocess.run(args,cwd=p,capture_output=True,text=True,timeout=600)
  v=dict(name=name,args=args,exit=r.returncode,stdout=r.stdout,stderr=r.stderr,passed=r.returncode==exit and (contains is None or contains in r.stdout+r.stderr))
 except Exception as e:v=dict(name=name,args=args,error=str(e),passed=False)
 cases.append(v);(out/"bend.json").write_text(json.dumps(dict(platform=platform.platform(),cases=cases),indent=2));print(name,v['passed'],flush=True)
run("version",["bend","version"],contains="2.0.37")
run("independent-kernel-valid",["bend","good-proof.bend","--verdict"],contains="ALL PROOFS CHECK")
for n in ["bad-proof","bad-type","bad-affine"]:run(n,["bend",n+".bend","--verdict"],exit=1)
run("emit-kernel-input",["bend","good-proof.bend","-o",str(out/"proof.bendtt")])
kernels=list((pathlib.Path.home()/".bend/bendtt").glob("*/bendtt"))
if kernels and (out/"proof.bendtt").exists():
 kernel=str(kernels[0]);run("kernel-direct-valid",[kernel,str(out/"proof.bendtt")],contains="ALL PROOFS CHECK")
 lines=(out/"proof.bendtt").read_text().splitlines()
 index=next(i for i,line in enumerate(lines) if line.startswith("main :"))
 lines[index+1]="  ()"
 (out/"corrupted.bendtt").write_text("\n".join(lines)+"\n")
 run("kernel-direct-corrupted-proof",[kernel,str(out/"corrupted.bendtt")],exit=1,contains="SOME PROOFS FAIL")
run("parallel-native-build",["bend","parallel.bend","-o",str(out/"parallel")])
run("parallel-native-result",[str(out/"parallel")],contains="4096")
run("parallel-js-build",["bend","parallel.bend","-o",str(out/"parallel.js")])
run("parallel-js-result",["node",str(out/"parallel.js")],contains="4096")
raise SystemExit(0 if all(x['passed'] for x in cases) else 1)
