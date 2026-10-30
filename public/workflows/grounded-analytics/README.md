# Explain computed metrics

Compute sales totals in code and check the numbers returned by the model.

Requires Kujo 1.9.0. Run inside this extracted directory.

## Offline demo

```sh
kujo run main.kujo
```

Three orders total 9,000 cents. Code calculates the total; the model writes an explanation that must repeat the same count and amount.

Output: analysis.json. Fixtures are authored test data, not evidence of live model quality.

## How it works

1. Validate unique order IDs and nonnegative integer amounts.
2. Compute the order count and total locally, then send only those metrics.
3. Reject model numbers that disagree with the calculation.

## Failure and recovery

Change total_cents in the response fixture to 9999. The comparison rejects it. Restore 9000 and rerun to recover.

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

Replace the orders with your own records and keep money in integer minor units. Add deterministic calculations for new metrics before asking the model to explain them.

The numeric fields are checked, but the prose may still mislead. Review the explanation before sharing it. This example does not generate or execute SQL.

## Files

main.kujo contains application policy; common.kujo handles JSON loading, writing and bounded AI requests. input.json and schema.json define the data contract. responses*.json are offline model-response fixtures.

Source: https://github.com/kujolang/kujolang.ai/tree/main/public/workflows/grounded-analytics
Walkthrough: https://kujolang.ai/examples/grounded-analytics/
