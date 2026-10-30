# Pack context within a budget

Select whole passages within a byte budget and reject citations to omitted sources.

Requires Kujo 1.9.0. Run inside this extracted directory.

## Offline demo

```sh
kujo run main.kujo
```

Two short passages fit the context budget. A longer appendix is skipped, and the answer can cite only the selected passages.

Output: context-answer.json. Fixtures are authored test data, not evidence of live model quality.

## How it works

1. Read passages in caller-supplied priority order and reject duplicate IDs.
2. Measure the serialized passage array in UTF-8 bytes before adding each passage.
3. Send the selected context and check every returned citation ID.

## Failure and recovery

Set budget_bytes to 2. No passage fits, so the application writes insufficient_context without a model call. Restore the budget to recover. A citation to the omitted appendix is also rejected.

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

Rank your passages before running the application. This example budgets the serialized context array only; reserve space for the question, instructions, schema and answer separately.

Bytes are not model tokens. This is a predictable context-size limit, not a provider token-limit guarantee. Citation IDs establish source membership, not whether a claim is supported.

## Files

main.kujo contains application policy; common.kujo handles JSON loading, writing and bounded AI requests. input.json and schema.json define the data contract. responses*.json are offline model-response fixtures.

Source: https://github.com/kujolang/kujolang.ai/tree/main/public/workflows/context-packing
Walkthrough: https://kujolang.ai/examples/context-packing/
