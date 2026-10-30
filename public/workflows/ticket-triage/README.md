# Support ticket triage

Classify a ticket and draft a reply for a person to review.

Requires Kujo 1.9.0. Run inside this extracted directory.

## Offline demo

```sh
kujo run main.kujo
```

A customer reports a duplicate charge. The output includes a billing category, invoice ID and unsent reply.

Output: triage.json. Fixtures are authored test data, not evidence of live model quality.

## How it works

1. Read the ticket and request a constrained category and priority.
2. Retry an invalid response within a two-request limit.
3. Check that the extracted invoice occurs in the ticket; save an unsent draft.

## Failure and recovery

The first authored response is invalid JSON. The second is valid, so the report records two attempts. Replace both with invalid text to reach failure.json; restore the responses to recover.

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

Replace input.json with a ticket from your own queue and adjust schema.json categories. Review the draft and billing facts before sending anything. The application has no sending integration.

Schema validation cannot guarantee that a reply is appropriate or that its promises are true. The output remains awaiting_human_review.

## Files

main.kujo contains application policy; common.kujo handles JSON loading, writing and bounded AI requests. input.json and schema.json define the data contract. responses*.json are offline model-response fixtures.

Source: https://github.com/kujolang/kujolang.ai/tree/main/public/workflows/ticket-triage
Walkthrough: https://kujolang.ai/examples/ticket-triage/
