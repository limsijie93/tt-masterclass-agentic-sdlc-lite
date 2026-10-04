# Take-home labs

Four labs, about 15–20 minutes each, one per idea from the masterclass. They use a fresh ticket,
so you meet each step cold rather than replaying the demo.

| Lab | Practises | You end with | Answer key |
|---|---|---|---|
| [01 · Refine a ticket](01-refine/lab.md) | Ask, stop, prune: before any code | A spec with testable criteria and an out-of-scope list | [`expected-spec.md`](01-refine/expected-spec.md) |
| [02 · Make a rule bite](02-make-a-rule-bite/lab.md) | Prose → a check that blocks the merge | A new CI rule, and a red PR that proves it works | [`expected.md`](02-make-a-rule-bite/expected.md) |
| [03 · Review an overbuilt PR](03-review-overbuilt/lab.md) | Judgement against the spec, then human focus | A review that names the excess, and the questions only a human answers | [`expected-review.md`](03-review-overbuilt/expected-review.md), [`expected-focus.md`](03-review-overbuilt/expected-focus.md), model solution: [`labs/03-qty-limit-solution`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/compare/labs/03-qty-limit-overbuilt...labs/03-qty-limit-solution) |
| [04 · Harvest, second sighting](04-harvest/lab.md) | Turn a repeated finding into a permanent rule | A harvest PR that proposes what it only logged last time | [`expected.md`](04-harvest/expected.md) |

Do them in order: lab 03 builds the ticket you refine in lab 01, and lab 04 harvests lab 03.

## Setup (once, about 5 minutes)

Nothing to install beyond your agent. Every lab happens in GitHub (web editor, issues, PRs, CI)
and in Claude Code or Cowork.

1. **Your own copy.** On the [repo page](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite),
   click **Use this template → Create a new repository**, and tick **Include all branches**. Labs
   03 and 04 need the `labs/…` and `harvest/2` branches.
2. **Your agent, connected to your copy.** Follow Steps 0–3 of the setup guide (Claude Code + the
   GitHub MCP server, or Cowork + the GitHub connector). Give your GitHub token read and write
   access to **Issues** and **Pull requests** on your copy, so the skills can post.
3. **Optional: make CI block.** In your copy: **Settings → Rules → Rulesets → New branch
   ruleset**, target `main`, add **Require status checks to pass**, choose `hygiene`.

Each lab ends with **Check yourself** (a short checklist) and an **answer key**, linked in the
table above. Agent output
varies run to run: compare the substance, not the wording.
