"""Seed an EMPTY, separately initialized Watchdog demo DB; never reads live telemetry.
Usage: python3 scripts/seed-watchdog-showcase.py DEMO_DB WATCHDOG_REPO
Start Watchdog with all WDG_* paths isolated before running. See screenshot README.
"""
import json, math, random, sqlite3, sys, time
from pathlib import Path
path = Path(sys.argv[1]).resolve()
assert path.name == 'demo.db' and 'showcase' in str(path.parent), 'Use an isolated showcase/demo.db'
catalog = json.loads((Path(sys.argv[2]) / 'config/provider_pricing_catalog.json').read_text())
db = sqlite3.connect(path)
assert db.execute('select count(*) from requests').fetchone()[0] == 0, 'Refusing to overwrite data'
rng = random.Random(261026)
end = int(time.time() * 1000) - 60000
start = end - 30 * 86400000
models = ['gpt-4.1', 'gpt-4.1-mini', 'gpt-4.1-nano']
workflows = ['Code review', 'Research synthesis', 'Document extraction', 'Support triage']
counts = [4600, 5900, 5100, 7200, 6500, 3200, 2800, 6100, 7500, 6800, 8900, 7200, 4100, 3500, 6700, 8100, 7400, 9600, 8200, 4600, 3900, 7800, 9200, 8400, 10400, 9100, 5200, 4400, 8600, 9800]
def insert(table, row):
    keys = ','.join(row)
    return db.execute(f'insert into {table} ({keys}) values ({",".join("?" for _ in row)})', list(row.values())).lastrowid
for day, count in enumerate(counts):
    for i in range(count):
        model = models[(i + day) % 3]; rate = catalog['models'][model]
        error = rng.random() < (0.045 if day in [8, 17, 24] else 0.012)
        inp = 0 if error else rng.randint(70000, 170000)
        out = 0 if error else rng.randint(900, 4800)
        ts = start + day * 86400000 + int((i + .5) * 86400000 / count)
        session = f'demo-{day+1:02d}-{i//12:04d}'
        latency = rng.randint(5500, 24000) if not error else rng.randint(300, 1500)
        ic = inp * rate['input_rate_per_million'] / 1e6
        oc = out * rate['output_rate_per_million'] / 1e6
        row = dict(session_id=session, user_id=f'demo-worker-{(i//12)%24+1:02d}', project_id='sample-workspace', workflow_id=workflows[i%4], provider='openai', model=model, request_id=f'demo-{day:02d}-{i:05d}', status='error' if error else 'success', input_tokens=inp, output_tokens=out, total_tokens=inp+out, cost_usd=ic+oc, input_cost_usd=ic, output_cost_usd=oc, input_rate_per_million=rate['input_rate_per_million'], output_rate_per_million=rate['output_rate_per_million'], pricing_source=rate['pricing_source'], pricing_kind='direct', priced_model=model, latency_ms=latency, finish_reason='' if error else 'stop', error_code='rate_limit' if error else '', error_message='Sample provider rate limit; retry scheduled.' if error else '', prompt_summary='Synthetic demo: review the supplied project documents and cite relevant sections.', response_summary='' if error else 'Synthetic demo: extracted findings with references to the supplied documents.', source_app='watchdog-showcase', data_class='fixture', created_at=str(ts))
        rid = insert('requests', row)
        if i % 3 == 0 and not error:
            insert('tool_calls', dict(request_dbid=rid, session_id=session, tool_call_id=f'demo-tool-{rid}', tool_name=['read_file','search_documents','query_database'][i//3%3], tool_args='{"query":"sample project documentation"}', tool_result='Found 8 relevant sections in the sample documents.', latency_ms=rng.randint(40,800), source_app='watchdog-showcase', data_class='fixture', created_at=str(ts)))
        if i % 4 == 0:
            insert('agent_steps', dict(session_id=session, agent_id='document-reviewer', step_number=i%12+1, step_type='reasoning', content='Compare retrieved sections and prepare a cited summary.', source_app='watchdog-showcase', data_class='fixture', created_at=str(ts)))
db.commit()
summary = dict(zip(['requests','tokens','estimated_cost_usd','errors','sessions'], db.execute("select count(*),sum(total_tokens),sum(cost_usd),sum(status='error'),count(distinct session_id) from requests").fetchone()))
assert summary['tokens'] > 20_000_000_000
assert db.execute('select count(*) from requests where total_tokens != input_tokens + output_tokens or abs(cost_usd-input_cost_usd-output_cost_usd)>0.000001').fetchone()[0] == 0
summary.update(days=30, synthetic=True, seed=261026, start_ms=start, end_ms=end, pricing_catalog=catalog['catalog_id'])
(path.parent / 'receipt.json').write_text(json.dumps(summary, indent=2)+'\n')
print(json.dumps(summary, indent=2))
