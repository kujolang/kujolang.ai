# Safe tool-using assistant

Preview a proposed file edit and apply only the approved contents.

Requires Kujo 1.9.0. Run inside this extracted directory.

## Offline demo

```sh
kujo run main.kujo
```

The assistant proposes a clearer heading for a local draft. Its first run writes a preview and leaves the draft untouched.

Output: proposal.json. Fixtures are authored test data, not evidence of live model quality.

## How it works

1. Ask for complete before and after text for the allowed file.
2. Validate the path and original contents, then save a proposal and preview.
3. Require the printed proposal hash and unchanged source before applying.

## Failure and recovery

Run the printed apply command with a wrong hash, or edit draft.txt after preview. The application refuses to apply. Generate a new preview and review it before approving its new hash.

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

Start in the extracted bundle directory, which includes a disposable draft.txt. Adapt the allowed path and content checks deliberately. Never pass the model output to a shell. preview.diff is a human before/after display, not an apply-ready patch.

Approval is a content check, not an operating-system sandbox. Use a trusted local directory with a regular draft.txt and no concurrent writers. For hostile workspaces, use filesystem isolation and race-resistant file operations.

## Files

main.kujo contains application policy; common.kujo handles JSON loading, writing and bounded AI requests. input.json and schema.json define the data contract. responses*.json are offline model-response fixtures.

Source: https://github.com/kujolang/kujolang.ai/tree/main/public/workflows/safe-editor
Walkthrough: https://kujolang.ai/examples/safe-editor/
