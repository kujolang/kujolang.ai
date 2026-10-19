function total() -> int { 6 * 7 }

testset "review" {
 test ("correct total") { assert.equal(total(), 42); }
}
