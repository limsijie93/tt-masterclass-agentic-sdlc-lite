# Agentic SDLC: lite

A 90-minute masterclass on where agents belong in the software development lifecycle, and where
they don't. One vague ticket goes from issue to reviewed pull request in four beats, then a
harvest turns what the reviews found into checks that make the next pull request easier:

| # | Beat | Who | Verdict | Lives in |
|---|---|---|---|---|
| 1 | **Refine the ticket**: ask, stop, then write a pruned spec | Agent | Spec on the issue | [`refine-ticket`](.claude/skills/refine-ticket/SKILL.md) |
| 2 | **Hygiene**: lint, format, layering, tests, coverage | CI | **Blocks** | [`ci.yml`](.github/workflows/ci.yml), [`pyproject.toml`](pyproject.toml) |
| 3 | **Judgement**: is this the *right* thing, or overbuilt? | Agent, fresh session | **Comments** | [`review-pr`](.claude/skills/review-pr/SKILL.md) |
| 4 | **Focus**: first pass, and where a human must look | Agent | **Points** | [`pr-focus`](.claude/skills/pr-focus/SKILL.md) |
| — | **Decide** | Human | **Decides** | [PR template](.github/pull_request_template.md) |
| ↺ | **Harvest**: each finding becomes a check, a rule, or a better skill | Agent proposes, human merges | **A PR** | [`harvest`](.claude/skills/harvest/SKILL.md), [`harvest/ledger.md`](harvest/ledger.md) |

Everything lives in the repo, the issue, the PR and CI. The agents run in **Claude Code** or
**Claude Cowork**, connected to the **GitHub MCP server**, and are given an issue or PR URL.
Nothing to install, no scripts to run.

## The story

- **[PR #1](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/1)** adds the CI gate. The layering rule was already prose in
  `AGENTS.md`. This PR makes it a check.
- **[Issue #2](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/issues/2)**: "Promo codes at checkout… flexible so we can do all kinds of
  deals."
- **`/refine-ticket`** asks five questions and stops. The answers prune it to one percentage
  code per order, and the spec says what was cut and why.
- **[PR #3](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/3)** (branch `demo/promo-codes`) is the agent's implementation. Its first
  commit fails CI three ways. Its second commit is green, and it ships a rule engine, a registry,
  stacking and expiry. None of that was asked for.
- **`/review-pr`** catches the overbuilding against the spec. **`/pr-focus`** points the human at
  the questions only they can answer: rounding, case sensitivity, API shape.
- **[PR #4](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/4)** is the same feature after review: cut to the spec, with the
  reviewer's decisions applied. 46 lines of code and tests instead of 162, and CI is green.
- **[PR #5](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/5)** stays red on purpose: a small follow-up that fails all three CI checks,
  so you can see what a blocked pull request looks like. Don't merge it.
- **`/harvest`** reads all three PRs and opens **[PR #6](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/6)** with three proposals: a CI
  **Scope** check that fails a PR changing files its spec doesn't list (it would have blocked
  PR #3's `discounts.py`), the rounding decision as a rule in `AGENTS.md`, and a sharper
  `refine-ticket`. The other 11 findings are logged, not proposed: six because CI already catches
  them. A human merges it, and the next ticket starts easier.

**Take-home labs:** [`labs/`](labs/README.md) has four, one per idea, on a fresh ticket.

**CI green is not the same as the right thing. And every review should leave the repo a little
harder to get wrong.**

## Learn on your own

There is no separate learner branch. The lesson is spread across `main`, the issue and the PRs,
so read them in this order:

0. **[`course/why.md`](course/why.md)**: why there are four layers, and the hole each one covers.
1. **[PR #1](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/1)**, *Files changed* tab: how a CI gate is added, in one reviewable PR.
2. **[Issue #2](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/issues/2)**: the vague ticket, then the agent's questions, the Product
   Owner's answers ([`course/product-owner/answers.md`](course/product-owner/answers.md)), and the
   pruned spec in the comments.
3. **[PR #3](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/3)**, *Commits* tab: the red CI run on the first commit, then green on the
   second.
4. **PR #3**, *Conversation* tab: the agent review (overbuilt against the spec), then the
   human-focus comment.
5. **[PR #4](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/4)**, *Files changed* tab: what PR #3 should have been. Compare the
   two diffs: the rule engine, stacking and expiry are gone, and the reviewer's two decisions
   (case-insensitive codes, round in the customer's favour) are in the code and in `specs/2.md`.
6. **[PR #5](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/5)**, *Checks* tab: a pull request CI is blocking right now. Open each failed
   step and find the line that broke it.
7. **[PR #6](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/6)**, *Description* and *Files changed*: the harvest. Read what it
   proposed and, just as important, what it only logged. Then open
   [`harvest/ledger.md`](harvest/ledger.md) on its branch: the memory the next harvest reads.
8. **Go further: [`course/resources/`](course/resources/README.md).** Every option on the
   discussion slides, with a template, an example or a link: a Jira ticket template and a GitHub
   issue form, GitHub Spec Kit, pre-commit and agent hooks, review bots, CODEOWNERS.
9. **Practise: [`labs/`](labs/README.md).** Four take-home labs on a fresh ticket: refine it,
   make a rule bite, review an overbuilt PR, and harvest a second sighting.
10. **Try it yourself.** In Claude Code or Cowork with the GitHub MCP server:
   - Run `/refine-ticket <Issue #2 URL>`. It stops after its questions, waiting for a human.
     **That human is the Product Owner, and their answers are in
     [`course/product-owner/answers.md`](course/product-owner/answers.md).** Give them in the session
     and say *"Continue."* Compare the spec you get with
     [`course/expected-outputs/2-spec.md`](course/expected-outputs/2-spec.md).
   - Run `/review-pr <PR #3 URL>` and compare your result with
     [`course/expected-outputs/3-review.md`](course/expected-outputs/3-review.md).

   On a repo you don't own, read each draft and **don't post it**.

Want your own CI runs? **Use this template → Include all branches**. In your copy, open an issue
from [`course/product-owner/ticket.md`](course/product-owner/ticket.md), run `/refine-ticket` on it and answer with
[`answers.md`](course/product-owner/answers.md), then open a PR from `demo/promo-codes`.

## Answer keys and model solutions

Agent output varies run to run. Compare the substance, not the wording.

**The demo** (Issue #2 → PR #3)

| Step | What to compare against |
|---|---|
| `/refine-ticket`: the questions | [`1-questions.md`](course/expected-outputs/1-questions.md) |
| The Product Owner's answers | [`answers.md`](course/product-owner/answers.md) |
| `/refine-ticket`: the spec | [`2-spec.md`](course/expected-outputs/2-spec.md) |
| `/review-pr` on PR #3 | [`3-review.md`](course/expected-outputs/3-review.md) |
| `/pr-focus` on PR #3 | [`4-focus.md`](course/expected-outputs/4-focus.md) |
| **Model solution** for PR #3 | [PR #4](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/4), cut to the spec ([compare with PR #3](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/compare/demo/promo-codes...demo/promo-codes-to-spec)) |
| `/harvest` on #3, #4, #5 | [`5-harvest.md`](course/expected-outputs/5-harvest.md), and the PR it opened: [PR #6](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/6) |

**The labs** ([`labs/`](labs/README.md))

| Lab | Answer key | Model solution |
|---|---|---|
| [01 · Refine a ticket](labs/01-refine/lab.md) | [`expected-spec.md`](labs/01-refine/expected-spec.md) | the spec itself |
| [02 · Make a rule bite](labs/02-make-a-rule-bite/lab.md) | [`expected.md`](labs/02-make-a-rule-bite/expected.md) | one line in `pyproject.toml`, shown in the answer key |
| [03 · Review an overbuilt PR](labs/03-review-overbuilt/lab.md) | [`expected-review.md`](labs/03-review-overbuilt/expected-review.md), [`expected-focus.md`](labs/03-review-overbuilt/expected-focus.md) | [`labs/03-qty-limit-solution`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/tree/labs/03-qty-limit-solution) ([compare with the overbuilt version](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/compare/labs/03-qty-limit-overbuilt...labs/03-qty-limit-solution)) |
| [04 · Harvest, second sighting](labs/04-harvest/lab.md) | [`expected.md`](labs/04-harvest/expected.md) | depends on your own review: judged by the checklist |

## Files

```
shop/                 the app: api -> service -> repo, ~30 lines
tests/
.claude/skills/       the four agent skills, each a single SKILL.md
harvest/ledger.md     every finding /harvest has read, proposed or not
.github/ISSUE_TEMPLATE/  a GitHub issue form: requesters fill required fields
.github/              CI and the PR template
specs/                specs live here once written
course/
  why.md              why four layers: the Swiss cheese model, with sources
  run-of-show.md      the 90 minutes, beat by beat, plus setup
  seed-pr.md          PR #3 body
  product-owner/      the Product Owner's ticket (Issue #2) and answers to the agent's questions
  expected-outputs/   what each agent should produce, to compare your run against
  resources/          every option on the discussion slides: templates, examples, links
labs/                 four take-home labs, each with steps, a checklist and an answer key
```

**Presenting?** Start with [`course/run-of-show.md`](course/run-of-show.md).

**Using the skills elsewhere?** Each one is a single file. Copy the folder into your repo's
`.claude/skills/`, or upload it as a skill in Cowork.

The full-length version of this material, with more skills, guards, evals and labs, is in
[`tt-masterclass-agentic-sdlc`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc).

## Licence

MIT. See [LICENSE](LICENSE).
