# Measure: usage, cost, and whether the process is working

Two sources, for two different questions. Use both.

| | Source | Answers | Needs |
|---|---|---|---|
| **A** | Claude Code's **OpenTelemetry** export | Who uses it, what it costs, what it produced, which skills run | An admin, and an OpenTelemetry collector your company already runs |
| **B** | The **process-metrics** GitHub Action in this repo | Are specs linked, does CI catch things first, is overbuilding going down, is the process improving itself | Nothing: it's already in [`.github/workflows/process-metrics.yml`](../../../.github/workflows/process-metrics.yml) |

**Measure outcomes, not activity.** Lines of code and session counts are the easiest numbers to
collect, and the easiest to game: a team told "more lines" writes more lines. Pair any activity
number with an outcome from B, and never put a usage target on individuals.

## A · Claude Code OpenTelemetry

Claude Code exports OpenTelemetry metrics and events. An admin turns it on for everyone through
**managed settings**, using the env block in
[`managed-settings.example.json`](managed-settings.example.json):

- `CLAUDE_CODE_ENABLE_TELEMETRY` turns it on. The `OTEL_*` exporter variables send metrics and
  events to your collector (Grafana, Datadog, Honeycomb, …).
- `OTEL_RESOURCE_ATTRIBUTES` tags everything with a team, so you can slice by team rather than by
  person.
- `OTEL_LOG_TOOL_DETAILS=1` is what makes **skill names** visible. Without it, every custom skill
  is reported as `custom_skill`. It also records Bash commands and tool inputs, so check it with
  whoever owns your privacy policy before turning it on.

A repository's own `.claude/settings.json` **can't** turn telemetry on or choose where it goes.
That's deliberate: it has to come from managed settings, or from each developer's own settings.
Cowork is configured separately, in the admin console under **Data and privacy → Monitoring**.

| A manager's question | Signal |
|---|---|
| Who's using it, and how much? | `claude_code.session.count`, `claude_code.user_prompt` events |
| What does it cost, per team? | `claude_code.cost.usage`, `claude_code.token.usage`, sliced by `team.id` |
| What did it produce? | `claude_code.commit.count`, `claude_code.pull_request.count`, `claude_code.lines_of_code.count` (activity, so pair it with B) |
| **Is the team following the process?** | `claude_code.skill_activated` events, by `skill.name`: how often `refine-ticket`, `review-pr`, `pr-focus` and `harvest` run, and whether people typed them (`user-slash`) or the agent chose them |

The last row is the one this masterclass cares about. If `review-pr` runs on few PRs, the
agent review isn't happening, whatever the PR count says.

Reference: [Claude Code monitoring docs](https://code.claude.com/docs/en/monitoring-usage), the
source for every variable and signal above.

## B · Process metrics from GitHub

[`process-metrics.yml`](../../../.github/workflows/process-metrics.yml) runs every Monday, and on
demand from **Actions → process-metrics → Run workflow**. It reads the repo's own pull requests,
CI runs and harvest ledger, writes a report to the run summary, and (on the schedule, or if you
tick the box) opens it as an issue.

| Metric | What it tells you | Moving the right way |
|---|---|---|
| PRs that name a spec (`Spec: specs/…`) | Is refinement happening before code? | Up |
| PRs red on their **first** CI run | Is CI catching problems before any human looks? | Healthy if it's caught there, not in review |
| Agent review findings per reviewed PR | Is overbuilding going down? | Down |
| Rework PRs (`Supersedes #`) | How often a PR had to be redone | Down |
| Median hours from PR opened to merged | Is review getting faster? | Down |
| Harvest PRs opened and merged, ledger lines | Is the process improving itself? | Steady |

Each metric is counted from text the skills and templates already write, so nothing extra has to
be logged by hand.
