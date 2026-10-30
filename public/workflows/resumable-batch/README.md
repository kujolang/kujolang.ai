# Resumable batch processor

Classify records, save checkpoints and continue after interruption.

Requires Kujo 1.9.0. Run inside this extracted directory.

## Offline demo

```sh
kujo run main.kujo
```

Three support records produce billing, account and technical labels. Completed record IDs survive a stopped process.

Output: batch-results.json. Fixtures are authored test data, not evidence of live model quality.

## How it works

1. Check that IDs are unique and the input matches any saved checkpoint.
2. Request and validate one unfinished record at a time.
3. Write a complete checkpoint and rename it before moving to the next record.

## Failure and recovery

Run KUJO_STOP_AFTER=1 kujo run main.kujo. Exit code 3 means the first result was saved. Run again without that variable to finish; the first request is skipped.

Extract a fresh copy to restore the fixtures. Check the command exit status before reading output; a previous output may remain after a failed run.

## Live mode

Live requests send input to your provider and may cost money.

```sh
export KUJO_WORKFLOW_MODE=live
export KUJO_AI_ENDPOINT=https://your-provider.example/v1/chat/completions
export KUJO_AI_MODEL=your-model
# Set KUJO_AI_KEY securely in your environment.
kujo run main.kujo
```

The examples use the OpenAI-compatible chat format. Normal requests allow two attempts, a two-second timeout per attempt and max_tokens=1024. Fallback permits one attempt per provider and two total. Tests exercise live transport with a local mock HTTP provider, not a paid model.

## Adaptation

Replace input.json.records with your batch. Live mode can process additional IDs without fixture files. Use a fresh directory when changing the input, schema or prompt. Run one worker per checkpoint directory.

This is a single-process checkpoint pattern, not a distributed queue or a power-loss durability guarantee. A request interrupted before its checkpoint may be repeated.

## Files

main.kujo contains application policy; common.kujo handles JSON loading, writing and bounded AI requests. input.json and schema.json define the data contract. responses*.json are offline model-response fixtures.

Source: https://github.com/kujolang/kujolang.ai/tree/main/public/workflows/resumable-batch
Walkthrough: https://kujolang.ai/examples/resumable-batch/
