# Verified language samples

Source: https://github.com/kujolang/kujo, release v1.9.0. The immutable commit is
recorded in catalog.json. Samples are copied verbatim, or as the exact inclusive
line range recorded there. Keep the upstream MIT license with the downloads.

Executed: 17 offline scripts, including AI request identity, cassette replay,
streaming, and capability denial/grant. Tested: one test-run fixture. Checked
only: module imports, file operations, HTTP listener. Check-only does not mean
those scripts have been executed or that their external dependencies exist.
The module tour deliberately lacks imported files. Packages and agent SDK
integration are linked as separate guides, not mislabeled runnable samples.

Edit catalog.json and public/samples together, then follow the commands in the
root README. Expected output is an assertion reviewed against the source; do not
blindly refresh it after a failed test. The AI cassettes are offline synthetic
fixtures from the same commit, not user or production model conversations.
