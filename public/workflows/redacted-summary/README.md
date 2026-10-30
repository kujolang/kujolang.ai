# Redact before summarizing

Remove known private values before sending a support note to a model.

Requires Kujo 1.9.0. Run inside this extracted directory.

## Offline demo

```sh
kujo run main.kujo
```

A support note repeats a customer email and account ID. Both values stay local while the model receives a redacted copy.

Output: summary.json. Fixtures are authored test data, not evidence of live model quality.

## How it works

1. Replace every occurrence of the configured private values locally.
2. Send only the redacted message, without the private-value list.
3. Reject an output containing a known private value and save a reviewable summary.

## Failure and recovery

Put the original email into the response fixture. The output check rejects it. Restore the redacted fixture and rerun to recover.

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

Replace the message and private_values together. Include every value that must stay local, with longer overlapping values first. Inspect the redacted request before adapting this to real customer data.

This exact-value filter is not a general detector of personal information. Unlisted, encoded or inferred details can pass through. The original input remains on disk; use appropriate local access controls.

## Files

main.kujo contains application policy; common.kujo handles JSON loading, writing and bounded AI requests. input.json and schema.json define the data contract. responses*.json are offline model-response fixtures.

Source: https://github.com/kujolang/kujolang.ai/tree/main/public/workflows/redacted-summary
Walkthrough: https://kujolang.ai/examples/redacted-summary/
