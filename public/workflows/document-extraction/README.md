# Document extraction pipeline

Turn invoice text into a validated record with source evidence.

Requires Kujo 1.9.0. Run inside this extracted directory.

## Offline demo

```sh
kujo run main.kujo
```

An invoice includes an amount and currency but no due date. The result preserves the missing field instead of filling it in.

Output: record.json. Fixtures are authored test data, not evidence of live model quality.

## How it works

1. Extract a record under a JSON schema.
2. Require the invoice ID and amount evidence to occur in the source text.
3. Report missing fields for a person to resolve.

## Failure and recovery

Change the returned amount to 999 while leaving its evidence unchanged. The grounding check stops the run. Restore the fixture and rerun; the result again reports the absent due date.

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

Replace input.json.text with extracted document text and change the schema and grounding checks together. This example starts with text; PDF OCR and image extraction are separate steps.

Substring evidence checks are intentionally small and inspectable. Repeated amounts and ambiguous invoices need stronger field-to-span validation and human review.

## Files

main.kujo contains application policy; common.kujo handles JSON loading, writing and bounded AI requests. input.json and schema.json define the data contract. responses*.json are offline model-response fixtures.

Source: https://github.com/kujolang/kujolang.ai/tree/main/public/workflows/document-extraction
Walkthrough: https://kujolang.ai/examples/document-extraction/
