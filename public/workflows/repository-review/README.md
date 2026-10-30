# Repository change reviewer

Review a Git diff and keep findings tied to added lines.

Requires Kujo 1.9.0. Run inside this extracted directory.

## Offline demo

```sh
kujo run main.kujo
```

A checkout calculation changes multiplication to addition. The reviewer flags the changed line and suggests a correction.

Output: review.json. Fixtures are authored test data, not evidence of live model quality.

## How it works

1. Parse added-line locations from a unified Git diff.
2. Ask for structured findings with reasons and suggested fixes.
3. Separate findings with valid locations from invented locations.

## Failure and recovery

Change the fixture finding to an unknown path or line. It moves to rejected_locations rather than appearing as an accepted finding. Restore the original response to recover.

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

Replace input.json.diff with the output of git diff --no-ext-diff --unified=3. Keep the review local until a person checks it. This parser covers ordinary text diffs, not combined merge diffs or binary patches.

Location checks establish where a finding points. A person must still judge whether the bug and suggested fix are correct.

## Files

main.kujo contains application policy; common.kujo handles JSON loading, writing and bounded AI requests. input.json and schema.json define the data contract. responses*.json are offline model-response fixtures.

Source: https://github.com/kujolang/kujolang.ai/tree/main/public/workflows/repository-review
Walkthrough: https://kujolang.ai/examples/repository-review/
