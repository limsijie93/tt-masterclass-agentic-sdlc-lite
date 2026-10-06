# Resources: other ways to build each layer

Each discussion slide in the masterclass shows a few ways to build a layer. Option 1 is the one the
demo uses. This page links every option to a template, an example, or the tool's own docs, in the
same order as the slides.

## Specs (slide 17)

| # | Option | What it is | Resource |
|---|---|---|---|
| 1 | **Agent skill** (today) | `/refine-ticket` asks up to five questions, stops, then writes a pruned spec | [`refine-ticket/SKILL.md`](../../.claude/skills/refine-ticket/SKILL.md) |
| 2 | **Ticket template** | The requester fills in required fields in a Jira ticket or a GitHub issue form. It can't be submitted without a goal, criteria and out of scope | [Jira template](specs/jira-ticket-template.md) · [GitHub issue form](../../.github/ISSUE_TEMPLATE/feature.yml) (live in this repo: try **New issue**) |
| 3 | **Spec-driven toolkit** | GitHub Spec Kit: `/speckit-specify` → `plan` → `tasks` → `implement`, each a file you review | [Spec Kit summary](specs/spec-kit.md) · [github.com/github/spec-kit](https://github.com/github/spec-kit) |
| 4 | **Refinement meeting** | Product, dev and QA talk the ticket through together | Write the outcome into the template in option 2, or it's lost |

These stack: a template makes sure the fields exist, and the agent checks what's in them.

## Quality (slide 24)

The same checks can run in three places. The further left, the faster the feedback and the easier
it is to skip, so the one nobody can skip is the one that blocks.

| # | Where it runs | When | Covers | Skippable? | Resource |
|---|---|---|---|---|---|
| 1 | **Required CI check** (today) | On every PR, in GitHub Actions | Everyone | No: it blocks the merge | [`ci.yml`](../../.github/workflows/ci.yml) + the *CI hygiene must pass* ruleset |
| 2 | **Pre-commit hooks** | On `git commit`, on the developer's laptop | Anyone who installed them | Yes: `git commit --no-verify` | [`pre-commit-config.example.yaml`](quality/pre-commit-config.example.yaml) · [pre-commit.com](https://pre-commit.com) |
| 3 | **Agent hooks** | After every file the agent edits | Only that agent's edits | Yes: edit the settings | [`claude-settings.example.json`](quality/claude-settings.example.json) · [Claude Code hooks](https://code.claude.com/docs/en/hooks) |

**How the agent hook works.** Put the example's contents in `.claude/settings.json`. After every
`Edit` or `Write`, Claude Code runs `ruff check` and `lint-imports`. If either fails, the hook exits
with code 2, and Claude Code shows the message to the agent, which fixes the problem before you
ever see it. It needs both tools installed where Claude Code runs.

**When a review finding becomes a check.** If a machine can check what the agent review keeps
finding, it moves out of Review and into this layer. `/harvest` did exactly that in
[PR #6](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/6): a **Scope** step in
`ci.yml` fails any PR that changes files its spec doesn't list under *Touches*.

## Review: agent (slide 32)

| # | Option | What it is | Resource |
|---|---|---|---|
| 1 | **On-demand skill, fresh session** (today) | `/review-pr` when you choose, judged against the spec | [`review-pr/SKILL.md`](../../.claude/skills/review-pr/SKILL.md) |
| 2 | **Review bot on every PR** | An agent comments automatically in CI. Keep it advisory, never a required check | [claude-code-action](https://github.com/anthropics/claude-code-action) · [Copilot code review](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review) |
| 3 | **A different model as reviewer** | The writer and the reviewer come from different vendors, so their blind spots are less likely to overlap | Run option 1 or 2 with a different model |

## Review: human (slide 37)

| # | Option | What it is | Resource |
|---|---|---|---|
| 1 | **Agent first pass** (today) | `/pr-focus` names two or three questions, each with a file and line | [`pr-focus/SKILL.md`](../../.claude/skills/pr-focus/SKILL.md) |
| 2 | **Human-only checklist** | Boxes in the PR template that only the reviewer ticks | [`pull_request_template.md`](../../.github/pull_request_template.md) |
| 3 | **CODEOWNERS** | Changes to domain files automatically request review from the people who own those rules | [`CODEOWNERS.example`](review/CODEOWNERS.example) · [GitHub docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) |
| 4 | **Risk labels** | PRs touching money, auth or data paths get a label, and the label requires an extra reviewer | [actions/labeler](https://github.com/actions/labeler) |

## Measure (for managers)

Is it being used, what does it cost, and is the process working? See
[`measure/README.md`](measure/README.md):

- **Usage and cost:** Claude Code's OpenTelemetry export, switched on through managed settings
  ([`managed-settings.example.json`](measure/managed-settings.example.json)). The
  `claude_code.skill_activated` event shows whether the four skills actually run.
- **Process outcomes:** [`process-metrics.yml`](../../.github/workflows/process-metrics.yml), a
  weekly GitHub Action that reports PRs with a spec, first-run CI failures, review findings per PR,
  rework, time to merge and harvest activity.

## Harvest

Not a layer but the loop around them: [`harvest/SKILL.md`](../../.claude/skills/harvest/SKILL.md),
[`harvest/ledger.md`](../../harvest/ledger.md), and the worked example in
[PR #6](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/6).
