# Agentic SDLC: lite

A 90-minute masterclass on where agents belong in the software development lifecycle, and where
they don't. One vague ticket goes from issue to reviewed pull request in four beats:

| # | Beat | Who | Verdict | Lives in |
|---|---|---|---|---|
| 1 | **Refine the ticket**: ask, stop, then write a pruned spec | Agent | Spec on the issue | [`refine-ticket`](.claude/skills/refine-ticket/SKILL.md) |
| 2 | **Hygiene**: lint, format, layering, tests, coverage | CI | **Blocks** | [`ci.yml`](.github/workflows/ci.yml), [`pyproject.toml`](pyproject.toml) |
| 3 | **Judgement**: is this the *right* thing, or overbuilt? | Agent, fresh session | **Comments** | [`review-pr`](.claude/skills/review-pr/SKILL.md) |
| 4 | **Focus**: first pass, and where a human must look | Agent | **Points** | [`pr-focus`](.claude/skills/pr-focus/SKILL.md) |
| — | **Decide** | Human | **Decides** | [PR template](.github/pull_request_template.md) |

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

**CI green is not the same as the right thing.**

## Learn on your own

There is no separate learner branch. The lesson is spread across `main`, the issue and the PRs,
so read them in this order:

1. **[PR #1](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/1)**, *Files changed* tab: how a CI gate is added, in one reviewable PR.
2. **[Issue #2](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/issues/2)**: the vague ticket, then the agent's questions, the answers, and
   the pruned spec in the comments.
3. **[PR #3](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/3)**, *Commits* tab: the red CI run on the first commit, then green on the
   second.
4. **PR #3**, *Conversation* tab: the agent review (overbuilt against the spec), then the
   human-focus comment.
5. **Try it yourself.** In Claude Code or Cowork with the GitHub MCP server, run
   `/review-pr <PR #3 URL>` and compare your result with
   [`course/fallback/3-review.md`](course/fallback/3-review.md). On a repo you don't own, read
   the draft and **don't post it**.

Want your own CI runs? **Use this template → Include all branches**, then open a PR from
`demo/promo-codes` in your copy.

## Files

```
shop/                 the app: api -> service -> repo, ~30 lines
tests/
.claude/skills/       the three agent skills, each a single SKILL.md
.github/              CI and the PR template
specs/                specs live here once written
course/
  run-of-show.md      the 90 minutes, beat by beat, plus setup
  seed-issue.md       Issue #2
  seed-pr.md          PR #3 body
  fallback/           known-good output for every beat
```

**Presenting?** Start with [`course/run-of-show.md`](course/run-of-show.md).

**Using the skills elsewhere?** Each one is a single file. Copy the folder into your repo's
`.claude/skills/`, or upload it as a skill in Cowork.

The full-length version of this material, with more skills, guards, evals and labs, is in
[`tt-masterclass-agentic-sdlc`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc).

## Licence

MIT. See [LICENSE](LICENSE).
