# Route requests through an allowlist

Map a model decision to a fixed local handler and send uncertain requests to review.

Requires Kujo 1.9.0. Run inside this extracted directory.

## Offline demo

```sh
kujo run main.kujo
```

A password-reset request is routed to the account-help queue. The model cannot choose a URL, shell command or arbitrary handler.

Output: route.json. Fixtures are authored test data, not evidence of live model quality.

## How it works

1. Request one of three allowed intents and a confidence value.
2. Apply a local confidence threshold before selecting a handler.
3. Write a routing decision for review without dispatching an external action.

## Failure and recovery

Lower the fixture confidence to 0.4. The request goes to human_review. Restore 0.95 to recover. An intent outside the enum exhausts the bounded retries without creating a route.

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

Change the schema enum and local handler map together. Calibrate a review threshold against labeled requests before using routing decisions in a real queue.

Model-reported confidence is not a calibrated probability. This example illustrates the policy boundary; it does not establish routing accuracy or send a message.

## Files

main.kujo contains application policy; common.kujo handles JSON loading, writing and bounded AI requests. input.json and schema.json define the data contract. responses*.json are offline model-response fixtures.

Source: https://github.com/kujolang/kujolang.ai/tree/main/public/workflows/intent-routing
Walkthrough: https://kujolang.ai/examples/intent-routing/
