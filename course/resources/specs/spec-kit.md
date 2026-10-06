# GitHub Spec Kit

[github.com/github/spec-kit](https://github.com/github/spec-kit): an open-source toolkit from
GitHub for spec-driven development. It installs a set of slash commands into your coding agent
(Claude Code, Copilot and others), and each command writes a file you review before the next step.

```
uv tool install specify-cli
specify init my-project
```

| Step | Command | Writes |
|---|---|---|
| Once per project | `/speckit-constitution` | The team's non-negotiable rules, e.g. "every feature has tests" |
| What and why | `/speckit-specify <the request>` | The spec: user stories, acceptance criteria, open questions |
| How | `/speckit-plan <tech choices>` | The technical plan: design, data model, files that change |
| Break it down | `/speckit-tasks` | Small, ordered, testable tasks |
| Build | `/speckit-implement` | The code, task by task |
| Check | `/speckit-converge` | Whether the build matches the spec, repeated until it does |

## Compared with `/refine-ticket`

| | `/refine-ticket` (today) | Spec Kit |
|---|---|---|
| Covers | Questions → spec, with out of scope | Rules → spec → plan → tasks → build → check |
| Files to review per ticket | One spec comment | Several |
| Good for | Tickets of any size | Features big enough to plan |
| Cost | Minutes | An hour or more per feature |

For the promo-code ticket, Spec Kit would produce a spec, a plan and a task list before any code,
which is thorough and heavy for a 30-line change. Worth stealing either way: the **constitution**,
a short file of rules every spec inherits.

Command names are from the Spec Kit README; check it for the current list.
