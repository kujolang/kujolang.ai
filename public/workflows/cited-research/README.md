# Research assistant with citations

Answer from a supplied document collection and retain exact quotes.

Requires Kujo 1.9.0. Run inside this extracted directory.

## Offline demo

```sh
kujo run main.kujo
```

A handbook states how long backups are retained. The assistant retrieves that passage and cites its source ID.

Output: answer.json. Fixtures are authored test data, not evidence of live model quality.

## How it works

1. Retrieve documents that match the supplied search terms.
2. Ask the model to answer only from those documents.
3. Check citation IDs and exact quotes against retrieved text.

## Failure and recovery

Set input.json.terms to an unmatched word. The application returns insufficient_evidence without calling a model. Restore the terms to recover. An invented citation quote is also rejected.

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

Replace the documents and query terms in input.json. The retriever uses simple lexical matching; replace that step with ranked retrieval when the collection grows.

An exact quote proves that text exists, not that it supports every claim in an answer. The result is marked needs_review; check the claim-to-citation relationship.

## Files

main.kujo contains application policy; common.kujo handles JSON loading, writing and bounded AI requests. input.json and schema.json define the data contract. responses*.json are offline model-response fixtures.

Source: https://github.com/kujolang/kujolang.ai/tree/main/public/workflows/cited-research
Walkthrough: https://kujolang.ai/examples/cited-research/
