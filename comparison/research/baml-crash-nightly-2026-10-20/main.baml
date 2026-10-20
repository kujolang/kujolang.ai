class Answer { value int }
function echo(value: int) -> int { value }
function plus(value: int) -> int { value + 1 }
function items(value: int[]) -> int[] { value }
function optional(value: int?) -> int? { value }
function answer(value: Answer) -> Answer { value }
function field(value: Answer) -> int { value.value }
function construct(value: int) -> Answer { Answer { value: value } }
function Extract() -> Answer {
 client: "openai/gpt-4o-mini"
 prompt: `Return value 42.`
}
