# Prompt regression lab

Compare prompt revisions against saved, labeled cases.

Requires Kujo 1.9.0. Run inside this extracted directory.

## Offline demo

```sh
kujo run main.kujo
```

A baseline misclassifies a password-reset ticket. A more specific candidate passes both saved cases in the authored offline fixture.

Output: evaluation.json. Fixtures are authored test data, not evidence of live model quality.

## How it works

1. Run both prompts over the same labeled cases.
2. Record predictions, per-case correctness and prompt hashes.
3. Exit with a failed gate if the candidate passes fewer cases.

## Failure and recovery

Change both candidate response fixtures to technical. The candidate regresses and exits 4. Restore the original fixtures and rerun to recover.

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

Add representative cases and expected labels to input.json. Use live mode to collect actual model results, repeat runs and review errors before changing a production prompt.

The offline score tests the evaluation machinery with authored responses. Two cases are not evidence of general prompt quality. Live results may vary even with temperature zero.

## Files

main.kujo contains application policy; common.kujo handles JSON loading, writing and bounded AI requests. input.json and schema.json define the data contract. responses*.json are offline model-response fixtures.

Source: https://github.com/kujolang/kujolang.ai/tree/main/public/workflows/prompt-regression
Walkthrough: https://kujolang.ai/examples/prompt-regression/
