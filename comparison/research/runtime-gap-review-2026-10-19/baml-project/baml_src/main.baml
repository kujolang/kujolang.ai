class Answer {
    value int
}
function total() -> int { 6 * 7 }
function echo(value: int) -> int { value }
function fail() -> int throws string { throw "review failure"; }
function context() -> trace.Context { trace.current_context() }
function Extract() -> Answer {
    client: "openai/gpt-4o-mini"
    prompt: `Return a JSON object with value 42.`
}
function local_provider(url: string) -> Answer {
    let cl = openai.ChatClient.new(model = "review-fixture", api_key = "local-fixture-only", base_url = url);
    ai.Agent.new(client = cl, schema_attempts = 1).run(Extract@spec()).value
}
