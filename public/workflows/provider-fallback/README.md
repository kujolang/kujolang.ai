# Provider fallback workflow

Try a second provider within a bounded request budget.

Requires Kujo 1.9.0. Run inside this extracted directory.

## Offline demo

```sh
kujo run main.kujo
```

The primary response fails validation. The backup returns a usable classification and the report records both attempts.

Output: routing.json. Fixtures are authored test data, not evidence of live model quality.

## How it works

1. Try the configured primary once with a two-second timeout.
2. Treat transport errors and schema failures as unsuccessful attempts.
3. Try the backup once, then stop and save the routing trace.

## Failure and recovery

The primary fixture is invalid by design. Make the backup invalid too to exhaust the two-request budget and exit 2. Restore the backup fixture to recover. Tests also exercise a real local HTTP timeout.

Extract a fresh copy to restore the fixtures. Check the command exit status before reading output; a previous output may remain after a failed run.

## Live mode

Live requests send input to your provider and may cost money.

```sh
export KUJO_WORKFLOW_MODE=live
export KUJO_PRIMARY_ENDPOINT=https://your-primary.example/v1/chat/completions
export KUJO_PRIMARY_MODEL=your-primary-model
export KUJO_BACKUP_ENDPOINT=https://your-backup.example/v1/chat/completions
export KUJO_BACKUP_MODEL=your-backup-model
# Set KUJO_PRIMARY_KEY and KUJO_BACKUP_KEY securely in your environment.
kujo run main.kujo
```

The examples use the OpenAI-compatible chat format. Normal requests allow two attempts, a two-second timeout per attempt and max_tokens=1024. Fallback permits one attempt per provider and two total. Tests exercise live transport with a local mock HTTP provider, not a paid model.

## Adaptation

Configure primary and backup endpoint, model and key variables independently. Use providers that accept the OpenAI-compatible chat format. Tune timeout and output-token limits in common.kujo for your workload.

The budget limits request count and per-request output tokens, not dollar spend. A timed-out provider may still complete and charge for a request. No unbounded retries or automatic provider discovery are performed.

## Files

main.kujo contains application policy; common.kujo handles JSON loading, writing and bounded AI requests. input.json and schema.json define the data contract. responses*.json are offline model-response fixtures.

Source: https://github.com/kujolang/kujolang.ai/tree/main/public/workflows/provider-fallback
Walkthrough: https://kujolang.ai/examples/provider-fallback/
