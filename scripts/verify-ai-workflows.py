#!/usr/bin/env python3
"""Exercise real Kujo programs with isolated files and a local provider server."""
import contextlib
import http.server
import json
import os
import pathlib
import shutil
import subprocess
import tempfile
import threading
import time
import unittest
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
BIN = os.environ.get('KUJO_BIN', 'kujo')
BASE = ROOT/'public/workflows'
CATALOG = json.loads((ROOT/'workflows/catalog.json').read_text())
SLUGS = [x['slug'] for x in CATALOG['items']]
OUTPUTS = {x['slug']: x['artifact'] for x in CATALOG['items']}

class Workflows(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = pathlib.Path(self.temp.name)
        self.env = {k:v for k,v in os.environ.items() if not k.startswith(('KUJO_AI_', 'KUJO_WORKFLOW_', 'KUJO_PRIMARY_', 'KUJO_BACKUP_', 'KUJO_STOP_'))}

    def setup(self, slug):
        with zipfile.ZipFile(BASE/(slug+'.zip')) as archive:
            archive.extractall(self.path)
        self.slug = slug

    def run_program(self, *args, code=0, **env):
        result = subprocess.run([BIN,'run','main.kujo',*(['--',*args] if args else [])], cwd=self.path, env={**self.env,**env}, capture_output=True,text=True,timeout=25)
        if code is None:self.assertNotEqual(result.returncode,0,result.stdout)
        else:self.assertEqual(result.returncode,code,result.stdout+result.stderr)
        return result

    def read(self, name):return json.loads((self.path/name).read_text())
    def write(self,name,value):(self.path/name).write_text(json.dumps(value)+'\n')
    def responses(self,value):self.write('responses.json',[json.dumps(value)])

    def test_offline_outputs(self):
        for slug in SLUGS:
            with self.subTest(slug=slug):
                directory=self.path/slug;directory.mkdir()
                old=self.path;self.path=directory;self.setup(slug)
                self.run_program()
                self.assertTrue((self.path/OUTPUTS[slug]).is_file())
                data=self.read(OUTPUTS[slug])
                if slug=='repository-review':self.assertEqual(data['findings'][0]['line'],2)
                if slug=='ticket-triage':self.assertEqual((data['attempts'],data['sent']),(2,False))
                if slug=='document-extraction':self.assertEqual(data['missing_fields'],['due_date'])
                if slug=='cited-research':self.assertEqual(data['citations'][0]['id'],'handbook')
                if slug=='resumable-batch':self.assertEqual([data[x]['label'] for x in ['r1','r2','r3']],['billing','account','technical'])
                if slug=='safe-editor':self.assertEqual((self.path/'draft.txt').read_text(),data['before'])
                if slug=='prompt-regression':self.assertEqual([x['passed'] for x in data['scores']],[1,2])
                if slug=='provider-fallback':self.assertEqual((data['selected'],len(data['trace'])),('backup',2))
                self.path=old

    def test_bounded_invalid_responses(self):
        self.setup('document-extraction');self.write('responses.json',['invalid','{}'])
        self.run_program(code=2);self.assertEqual(self.read('failure.json')['attempts'],2)
        self.assertFalse((self.path/'record.json').exists())

    def test_review_rejects_invented_location(self):
        self.setup('repository-review');self.responses({'findings':[{'path':'secrets.txt','line':99,'reason':'invented','suggestion':'delete'}]})
        self.run_program();data=self.read('review.json');self.assertEqual(data['findings'],[]);self.assertEqual(len(data['rejected_locations']),1)

    def test_ticket_rejects_invented_invoice(self):
        self.setup('ticket-triage');data=json.loads(self.read('responses.json')[-1]);data['invoice']='INV-999';self.responses(data)
        self.run_program(code=None);self.assertFalse((self.path/'triage.json').exists())

    def test_extraction_rejects_invented_amount(self):
        self.setup('document-extraction');data=json.loads(self.read('responses.json')[0]);data['total']=999;self.responses(data)
        self.run_program(code=None);self.assertFalse((self.path/'record.json').exists())

    def test_extraction_rejects_invented_due_date(self):
        self.setup('document-extraction');data=json.loads(self.read('responses.json')[0]);data['due_date']='2030-01-01';self.responses(data)
        self.run_program(code=None);self.assertFalse((self.path/'record.json').exists())

    def test_research_no_evidence_and_recovery(self):
        self.setup('cited-research');original=self.read('input.json');changed={**original,'terms':['unobtainium']};self.write('input.json',changed)
        self.run_program();self.assertEqual(self.read('answer.json')['status'],'insufficient_evidence')
        self.write('input.json',original);self.run_program();self.assertEqual(self.read('answer.json')['status'],'needs_review')

    def test_research_rejects_fabricated_quote(self):
        self.setup('cited-research');data=json.loads(self.read('responses.json')[0]);data['citations'][0]['quote']='Backups last forever.';self.responses(data)
        self.run_program(code=None);self.assertFalse((self.path/'answer.json').exists())

    def test_batch_resume_skips_completed_requests(self):
        self.setup('resumable-batch');self.run_program(code=3,KUJO_STOP_AFTER='1')
        self.assertEqual(list(self.read('checkpoint.json')['results']),['r1'])
        (self.path/'responses-r1.json').unlink()
        self.run_program();self.assertEqual(len(self.read('batch-results.json')),3)
        self.run_program();self.assertEqual(len(self.read('batch-results.json')),3)

    def test_hundred_record_batch(self):
        self.setup('resumable-batch')
        records=[{'id':f'r{i}','text':'Duplicate payment'} for i in range(100)]
        self.write('input.json',{'records':records})
        for record in records:self.write('responses-'+record['id']+'.json',[json.dumps({'label':'billing'})])
        self.run_program(code=3,KUJO_STOP_AFTER='37')
        self.assertEqual(len(self.read('checkpoint.json')['results']),37)
        for record in records[:37]:(self.path/('responses-'+record['id']+'.json')).unlink()
        self.run_program();self.assertEqual(len(self.read('batch-results.json')),100)

    def test_batch_detects_changed_input(self):
        self.setup('resumable-batch');self.run_program(code=3,KUJO_STOP_AFTER='1')
        data=self.read('input.json');data['records'][0]['text']='Changed';self.write('input.json',data)
        self.run_program(code=None);self.assertEqual(list(self.read('checkpoint.json')['results']),['r1'])

    def test_batch_rejects_duplicate_ids(self):
        self.setup('resumable-batch');data=self.read('input.json');data['records'][1]['id']='r1';self.write('input.json',data)
        self.run_program(code=None);self.assertFalse((self.path/'checkpoint.json').exists())

    def test_editor_requires_exact_approval(self):
        self.setup('safe-editor');r=self.run_program();digest=r.stdout.strip().split()[-1]
        before=(self.path/'draft.txt').read_bytes();self.run_program('apply','wrong',code=None);self.assertEqual((self.path/'draft.txt').read_bytes(),before)
        self.run_program('apply',digest);self.assertEqual((self.path/'draft.txt').read_text(),self.read('proposal.json')['after'])
        self.assertEqual(self.read('applied.json')['proposal_hash'],digest)

    def test_editor_rejects_stale_file(self):
        self.setup('safe-editor');r=self.run_program();digest=r.stdout.strip().split()[-1]
        (self.path/'draft.txt').write_text('User changed this.');self.run_program('apply',digest,code=None)
        self.assertEqual((self.path/'draft.txt').read_text(),'User changed this.')

    def test_editor_rejects_other_paths(self):
        self.setup('safe-editor');data=json.loads(self.read('responses.json')[0]);data['path']='../escape.txt';self.responses(data)
        self.run_program(code=None);self.assertFalse((self.path/'proposal.json').exists())

    def test_regression_gate_and_recovery(self):
        self.setup('prompt-regression');p=self.path/'responses-candidate-refund.json';old=p.read_text();p.write_text('["{\\"label\\":\\"technical\\"}"]')
        self.write('responses-candidate-login.json',[json.dumps({'label':'technical'})])
        self.run_program(code=4);self.assertTrue(self.read('evaluation.json')['regression'])
        p.write_text(old);self.write('responses-candidate-login.json',[json.dumps({'label':'account'})]);self.run_program()
        self.assertFalse(self.read('evaluation.json')['regression'])

    def test_fallback_exhaustion(self):
        self.setup('provider-fallback');self.write('responses-backup.json',['{}']);self.run_program(code=2)
        data=self.read('routing.json');self.assertIsNone(data['selected']);self.assertEqual(data['requests_remaining'],0)

    def test_redaction_transport_and_output_boundary(self):
        self.setup('redacted-summary');original=self.read('input.json')
        with self.server(lambda path,body: {'summary':'A customer needs help.'}) as (url,calls):
            self.run_program(KUJO_WORKFLOW_MODE='live',KUJO_AI_ENDPOINT=url+'/chat',KUJO_AI_MODEL='mock')
            payload=json.dumps(calls[0]['body'])
            for value in original['private_values']:self.assertNotIn(value,payload)
            self.assertNotIn('private_values',payload)
            self.assertEqual(self.read('summary.json')['redacted_input'].count('[REDACTED]'),3)
        self.responses({'summary':original['private_values'][0]})
        self.run_program(code=None)
        self.responses({'summary':'A customer needs help.'});self.run_program()

    def test_redaction_rejects_empty_filter(self):
        self.setup('redacted-summary');data=self.read('input.json');data['private_values']=[''];self.write('input.json',data)
        with self.server(lambda path,body: {'summary':'unused'}) as (url,calls):
            self.run_program(code=None,KUJO_WORKFLOW_MODE='live',KUJO_AI_ENDPOINT=url+'/chat',KUJO_AI_MODEL='mock')
            self.assertEqual(calls,[])

    def test_analytics_checks_numbers_and_recovers(self):
        self.setup('grounded-analytics');data=json.loads(self.read('responses.json')[0]);data['total_cents']=9999;self.responses(data)
        self.run_program(code=None);self.assertFalse((self.path/'analysis.json').exists())
        data['total_cents']=9000;self.responses(data);self.run_program()
        self.assertEqual(self.read('analysis.json')['metrics'],{'order_count':3,'total_cents':9000})
        data['order_count']=4;self.responses(data);self.run_program(code=None)

    def test_analytics_rejects_bad_records_before_request(self):
        self.setup('grounded-analytics');original=self.read('input.json')
        with self.server(lambda path,body: {}) as (url,calls):
            for amount in [-1,1.5]:
                data=json.loads(json.dumps(original));data['orders'][0]['total_cents']=amount;self.write('input.json',data)
                self.run_program(code=None,KUJO_WORKFLOW_MODE='live',KUJO_AI_ENDPOINT=url+'/chat',KUJO_AI_MODEL='mock')
            data=json.loads(json.dumps(original));data['orders'][1]['id']='o1';self.write('input.json',data)
            self.run_program(code=None,KUJO_WORKFLOW_MODE='live',KUJO_AI_ENDPOINT=url+'/chat',KUJO_AI_MODEL='mock')
            self.assertEqual(calls,[])

    def test_context_budget_no_request_and_recovery(self):
        self.setup('context-packing');original=self.read('input.json');self.write('input.json',{**original,'budget_bytes':2})
        with self.server(lambda path,body: {}) as (url,calls):
            self.run_program(KUJO_WORKFLOW_MODE='live',KUJO_AI_ENDPOINT=url+'/chat',KUJO_AI_MODEL='mock')
            self.assertEqual(calls,[]);self.assertEqual(self.read('context-answer.json')['status'],'insufficient_context')
        self.write('input.json',original);self.run_program();data=self.read('context-answer.json')
        self.assertEqual(data['selected_ids'],['retention','encryption']);self.assertEqual(data['omitted_ids'],['appendix'])
        self.assertLessEqual(data['context_bytes'],180)
        self.responses({'answer':'Invented','source_ids':['appendix']});self.run_program(code=None)

    def test_context_utf8_and_duplicate_ids(self):
        self.setup('context-packing');passages=[{'id':'unicode','text':'é'*20}]
        self.write('input.json',{'question':'Explain','budget_bytes':200,'passages':passages})
        with self.server(lambda path,body: {'answer':'Unicode passage','source_ids':['unicode']}) as (url,calls):
            self.run_program(KUJO_WORKFLOW_MODE='live',KUJO_AI_ENDPOINT=url+'/chat',KUJO_AI_MODEL='mock')
            data=self.read('context-answer.json');size=data['context_bytes']
            self.assertGreater(size,len(json.dumps(passages,ensure_ascii=False,separators=(',',':'))))
            self.write('input.json',{'question':'Explain','budget_bytes':size-1,'passages':passages});self.run_program()
            self.assertEqual(self.read('context-answer.json')['status'],'insufficient_context')
            self.write('input.json',{'question':'Explain','budget_bytes':200,'passages':passages*2});self.run_program(code=None)

    def test_routing_policy_and_recovery(self):
        self.setup('intent-routing');self.responses({'intent':'account','confidence':0.4});self.run_program()
        self.assertEqual(self.read('route.json')['handler'],'human_review')
        self.responses({'intent':'account','confidence':0.8});self.run_program();self.assertEqual(self.read('route.json')['handler'],'account_help')
        self.assertFalse(self.read('route.json')['dispatched'])
        self.responses({'intent':'shell','confidence':1});self.run_program(code=2)
        self.responses({'intent':'billing','confidence':0.95});self.run_program();self.assertEqual(self.read('route.json')['handler'],'billing_review')

    def test_cache_hit_invalidation_and_corruption(self):
        self.setup('response-cache');self.run_program();first=self.read('cached-result.json');self.assertFalse(first['cache_hit'])
        fixture=(self.path/'responses.json').read_bytes();(self.path/'responses.json').unlink();self.run_program()
        self.assertTrue(self.read('cached-result.json')['cache_hit'])
        data=self.read('input.json');data['prompt_revision']='v2';self.write('input.json',data);self.run_program(code=None)
        (self.path/'responses.json').write_bytes(fixture);self.run_program();second=self.read('cached-result.json')
        self.assertFalse(second['cache_hit']);self.assertNotEqual(first['key'],second['key'])
        cached=self.read('cache.json');cached['data']={'label':'invented'};self.write('cache.json',cached);self.run_program(code=None)
        (self.path/'cache.json').unlink();self.run_program();self.assertFalse(self.read('cached-result.json')['cache_hit'])

    def test_cache_live_identity_and_schema_invalidation(self):
        self.setup('response-cache')
        with self.server(lambda path,body: {'label':'account'}) as (url,calls):
            env=dict(KUJO_WORKFLOW_MODE='live',KUJO_AI_ENDPOINT=url+'/chat',KUJO_AI_MODEL='mock')
            self.run_program(**env);self.run_program(**env);self.assertEqual(len(calls),1)
            self.run_program(**{**env,'KUJO_AI_MODEL':'other'});self.assertEqual(len(calls),2)
            self.run_program(**{**env,'KUJO_AI_ENDPOINT':url+'/other'});self.assertEqual(len(calls),3)
            schema=self.read('schema.json');schema['properties']['label']['description']='Updated policy';self.write('schema.json',schema)
            self.run_program(**env);self.assertEqual(len(calls),4)
            p=self.path/'common.kujo';p.write_text(p.read_text()+'\n# New request policy revision\n')
            self.run_program(**env);self.assertEqual(len(calls),5)

    @contextlib.contextmanager
    def server(self, responder):
        calls=[]
        class Handler(http.server.BaseHTTPRequestHandler):
            def log_message(self,*a):pass
            def do_POST(self):
                data=json.loads(self.rfile.read(int(self.headers['Content-Length'])))
                calls.append({'path':self.path,'body':data,'authorization':self.headers.get('Authorization')})
                response=responder(self.path,data)
                if response is None:time.sleep(3);return
                body=json.dumps({'choices':[{'message':{'content':json.dumps(response)},'finish_reason':'stop'}]}).encode()
                try:self.send_response(200);self.send_header('Content-Type','application/json');self.end_headers();self.wfile.write(body)
                except (BrokenPipeError,ConnectionResetError):pass
        server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Handler);threading.Thread(target=server.serve_forever,daemon=True).start()
        try:yield f'http://127.0.0.1:{server.server_port}',calls
        finally:server.shutdown();server.server_close()

    def test_live_adapter_all_applications(self):
        for slug in SLUGS:
            with self.subTest(slug=slug):
                old=self.path;self.path=old/slug;self.path.mkdir();self.setup(slug)
                def response(path,body):
                    prompt=body['messages'][-1]['content']
                    if slug=='resumable-batch':
                        data=json.loads(prompt.split('INPUT:\n')[1]);return json.loads(self.read('responses-'+data['id']+'.json')[0])
                    if slug=='prompt-regression':
                        candidate='Charges and refunds' in prompt
                        login='password reset' in prompt
                        return {'label':'account' if candidate and login else 'technical' if login else 'billing'}
                    if slug=='provider-fallback':return {} if path=='/primary' else {'label':'account'}
                    return json.loads(self.read('responses.json')[-1])
                with self.server(response) as (url,calls):
                    self.run_program(KUJO_WORKFLOW_MODE='live',KUJO_AI_ENDPOINT=url+'/chat',KUJO_AI_MODEL='mock',KUJO_AI_KEY='test-only-key',KUJO_PRIMARY_ENDPOINT=url+'/primary',KUJO_PRIMARY_MODEL='mock',KUJO_BACKUP_ENDPOINT=url+'/backup',KUJO_BACKUP_MODEL='mock')
                    self.assertGreater(len(calls),0);self.assertTrue((self.path/OUTPUTS[slug]).exists())
                    if slug!='provider-fallback':self.assertEqual(calls[0]['authorization'],'Bearer test-only-key')
                    self.assertTrue(all(c['body']['max_tokens']==1024 for c in calls))
                self.path=old

    def test_live_timeout_falls_back(self):
        self.setup('provider-fallback')
        with self.server(lambda path,body: None if path=='/primary' else {'label':'account'}) as (url,calls):
            started=time.monotonic()
            self.run_program(KUJO_WORKFLOW_MODE='live',KUJO_PRIMARY_ENDPOINT=url+'/primary',KUJO_PRIMARY_MODEL='mock',KUJO_BACKUP_ENDPOINT=url+'/backup',KUJO_BACKUP_MODEL='mock')
            self.assertLess(time.monotonic()-started,6);self.assertEqual(len(calls),2)
            self.assertEqual(self.read('routing.json')['selected'],'backup')

if __name__=='__main__':unittest.main(verbosity=2)
