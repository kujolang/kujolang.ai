# Iteration findings and correction

Required gates failed: nested example custom_url values were rejected by the
existing single-slug helper; updated navigation intentionally no longer matched
old dropdown assertions; Howl generation had not yet completed before build.
The full final build must run after social generation. The uppercase branding
scan also matched the pinned executable to_upper assertion; exclude only that
assertion pattern, preserving all prose checks. Browser assertions now wait for
asynchronous copy completion and DOM readiness rather than media network idle.
