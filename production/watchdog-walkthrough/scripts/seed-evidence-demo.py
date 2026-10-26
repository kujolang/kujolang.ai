#!/usr/bin/env python3
"""Supplement ONLY the isolated showcase on port 7791 with documented test evidence."""
import json,urllib.request,datetime,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[4]/'watchdog'
now=datetime.datetime.now(datetime.timezone.utc);day=now.strftime('%Y-%m-%d');receipts=[]
def post(path,payload):
 req=urllib.request.Request('http://127.0.0.1:7791'+path,data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
 with urllib.request.urlopen(req) as r: result=json.load(r)
 receipts.append({'path':path,'result':result});print(path,result)
for name in ['retry-fallback-recovery','timing-context-billing']:
 s=(ROOT/'tests/fixtures/telemetry-v2'/f'{name}.json').read_text().replace('2026-09-02',day)
 payload=json.loads(s)
 if name=='timing-context-billing': payload['records']=payload['records'][:1]
 post('/telemetry/v2/batches',payload)
base=int(now.timestamp()*1000)-20000
spans=[]
for i,(kind,name,start,end) in enumerate([('workflow','Research and summarize',0,12000),('tool','Search documentation',200,1800),('model','Summarize retrieved evidence',2000,10000),('persistence','Save session result',10300,11500)]):
 spans.append({'span_id':f'demo-span-{i}','parent_span_id':None if i==0 else 'demo-span-0','span_kind':kind,'name':name,'status':'success','started_at_ms':base+start,'ended_at_ms':base+end,'duration_ms':end-start,'attributes':{'synthetic':True}})
payload={'schema_version':'kujo.telemetry.v1','source_app':'watchdog-video-demo','trace_id':'demo-video-research-trace','session_id':'demo-video-research-session','trace':{'trace_id':'demo-video-research-trace','name':'Research and summarize','status':'success','started_at_ms':base,'ended_at_ms':base+12000,'duration_ms':12000},'spans':spans,'events':[{'event_id':'demo-first-output','span_id':'demo-span-2','sequence':1,'event_name':'first_token','occurred_at_ms':base+2450,'attributes':{'synthetic':True}},{'event_id':'demo-persisted','span_id':'demo-span-3','sequence':2,'event_name':'persistence_saved','occurred_at_ms':base+11500,'attributes':{'state':'committed','synthetic':True}}]}
post('/api/telemetry/traces',payload)
(pathlib.Path(__file__).resolve().parents[1]/'evidence-demo-receipt.json').write_text(json.dumps({'synthetic':True,'receipts':receipts},indent=2)+'\n')
