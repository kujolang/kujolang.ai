# Cache validated responses

Reuse a checked result only when its input, prompt, schema and provider identity match.

Requires Kujo 1.9.0. Run inside this extracted directory.

## Offline demo

```sh
kujo run main.kujo
```

A repeated classification uses a local cached response. Changing the prompt revision or request content forces a new request.

Output: cached-result.json. Fixtures are authored test data, not evidence of live model quality.

## How it works

1. Hash the input, prompt, schema, mode, provider identity and request code.
2. Validate a matching cache entry before using it.
3. Write a complete replacement cache after a successful request.

## Failure and recovery

Run twice, deleting responses.json after the first run. The second run succeeds from cache. Change prompt_revision in input.json and it must request again; restore responses.json from the ZIP to recover.

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

Change prompt_revision when policy changes. The key also covers the prompt and request code automatically. Use one trusted writer per directory and delete cache.json when you want a fresh result.

This local cache has no expiry or cross-process lock. It excludes credentials from the key, so use separate directories for different accounts or tenants. Model behavior can change under the same model name; invalidate the cache when that matters.

## Files

main.kujo contains application policy; common.kujo handles JSON loading, writing and bounded AI requests. input.json and schema.json define the data contract. responses*.json are offline model-response fixtures.

Source: https://github.com/kujolang/kujolang.ai/tree/main/public/workflows/response-cache
Walkthrough: https://kujolang.ai/examples/response-cache/
