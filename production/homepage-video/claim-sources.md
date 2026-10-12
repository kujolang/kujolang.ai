# Source review · 2026-10-12

The prior August film showed 83 skills, 56 roles, 26 workflows, and Kujo 1.0.2, plus constructed “verified” terminal output. This revision removes those fragile counts and simulated verification claims. Current source identifies Kujo 1.8.0, but the introduction deliberately explains capabilities rather than reciting release numbers.

| Scene | Supported claim | Editable source in this repository |
| --- | --- | --- |
| Language | AI-native language, local-first toolchain, clear/controlled/verifiable work | templates/page-home.html; content/ecosystem/01-kujo.md |
| Evidence | Task scope, context, evaluation, run receipts | content/ecosystem/12-spec.md; 13-eval.md; 21-runledger.md; Scout and Scent ecosystem entries |
| Build | AI and agent SDKs, portable Ability operations and MCP projections | content/ecosystem/10-ai-sdk.md; 11-agents-sdk.md; 16-ability.md; 16-mcp.md |
| Applications | Websites, content management, agent orchestration | content/ecosystem/43-ssg.md; 41-cms.md; 14-dispatch.md |
| Guidance | Skills, specialist roles, workflow kits | content/skills/; content/workflows/; current agent-onboarding prompt |
| Setup | Ecosystem exploration, Quick Install and agent onboarding; default core + operating | templates/layout.html; public/install.sh; assets/prompts/kujo-agent-onboarding.txt |
| Close | Trust at the speed of AI | templates/page-home.html |

No sandbox, exactly-once, universal rollback, blanket safety, or hosted autonomous-service claim. Application owners retain authority. Experimental assurance and participant SDK work is not presented as stable. Illustrations explain capabilities; they are not test evidence. Source hashes are in source-manifest.json.
