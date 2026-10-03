# Run of show: 90 minutes, pure demo

One ticket, four beats. Everything happens in an **Issue**, a **PR**, **CI**, and a Claude Code or
Cowork session connected to the **GitHub MCP server**.

## Before the session (once, ~15 min)

Steps 1–4 are already done on `limsijie93/tt-masterclass-agentic-sdlc-lite`. They are here so
the setup can be rebuilt from scratch.

1. **PR #1**, branch `ci/hygiene-gate` → `main`: adds the CI gate. Let it go green, then merge it.
2. **Settings → Branches**: protect `main` and make the `hygiene` check required. Nothing else.
3. Open **Issue #2** from [`seed-issue.md`](seed-issue.md).
4. Push only the first commit of `demo/promo-codes` and open **PR #3** into `main` with the body
   from [`seed-pr.md`](seed-pr.md). Wait for the red run, then push the second commit and wait
   for green. If you want to show red live, push the second commit during beat 2 instead.
5. In Claude Code (or Cowork), connect the GitHub MCP server, open this repo, and check that
   `/refine-ticket`, `/review-pr` and `/pr-focus` are listed. In Cowork, upload the three
   `SKILL.md` folders under `.claude/skills/` as skills.
6. Have [`fallback/`](fallback/) open in a tab. Every beat has a known-good output there.

## The 90 minutes

| Time | Beat | On screen | The point |
|---|---|---|---|
| 0–10 | Why | Issue #2 | Agents don't ask, they guess. And they build for every case a ticket hints at. "Flexible, all kinds of deals" is an invitation. |
| 10–30 | **1 · Refine** | Session + Issue #2 | Planning and pruning happen *before* code. |
| 30–35 | Bridge | PR #3 | "Claude Code implemented the spec." Coding itself is not the lesson today. |
| 35–50 | **2 · Hygiene** | PR #3 checks tab | Deterministic checks block. Same input, same verdict. |
| 50–70 | **3 · Judgement** | Session + PR #3 | CI green does not mean the right thing was built. |
| 70–85 | **4 · Focus** | Session + PR #3 | The agent points, the human decides. |
| 85–90 | Close | The table below | What goes where. |

### Beat 1: refine the ticket (10–30)

1. Fresh session. Type `/refine-ticket <Issue #2 URL>`.
2. It reads the issue and the code, then **stops** with up to five questions. Point out:
   - every question has `assumes:`, the guess an agent would otherwise make silently
   - it did not answer its own questions, and that stop is the whole mechanism
3. Let it post the questions to the issue. Then answer them, playing Marketing, using
   [`fallback/1-answers.md`](fallback/1-answers.md).
4. It drafts the spec. Scroll to **Out of scope**: four things the ticket hinted at, cut, each
   with a reason. Then **Still open for human judgement**: rounding and case sensitivity. Those
   come back in beat 4.
5. Let it post the spec to the issue.

Fallback: [`1-questions.md`](fallback/1-questions.md), [`2-spec.md`](fallback/2-spec.md).

### Bridge (30–35)

Open PR #3. "We handed that spec to Claude Code and it opened this PR." Show the description: it
proudly lists a rule registry, stacking and expiry. Plant the question, *did we ask for that?*,
and don't answer it yet.

### Beat 2: deterministic hygiene (35–50)

1. PR #3 → **Commits** → the first commit → its CI run. Three red steps:
   - **Lint**: `json` imported and never used (`shop/api.py:3`)
   - **Architecture**: `shop.api` imports `shop.repo` directly, skipping the service layer
   - **Coverage**: 78%, below the 90% floor, because new branches have no tests
2. Where did those checks come from? Open **PR #1**, *Add CI hygiene gate*. One reviewed PR
   added `ci.yml`, the tool config in `pyproject.toml`, and the matching `Commands` block in
   `AGENTS.md`. Note the layering rule: it was already prose in `AGENTS.md`
   ("never imports `repo`"), and the agent ignored it anyway. PR #1 turned the prose into a
   check, and only the check stopped it.
3. The second commit fixes all three, and CI goes green.
4. The point: these checks have the same verdict every time, so they are allowed to **block**.
   Spend no human or agent attention on anything they can catch.

### Beat 3: agentic judgement (50–70)

1. **New session**, never the one that wrote the code. Type `/review-pr <PR #3 URL>`.
2. It reads the spec, then the diff, traces each criterion to code and test, and flags what maps
   to no criterion. Expect: stacking, the rule engine and registry, and expiry. Each one quotes
   the out-of-scope line it violates and names the simpler shape.
3. The punchline: **all of this passed CI.** The PR adds about 160 lines of code and tests.
   The spec needed a dict entry, a few lines in `order_total` and three tests.
4. It **comments**; it never approves or blocks. Agents are non-deterministic, and a gate that
   flakes gets switched off within a week.

Fallback: [`3-review.md`](fallback/3-review.md).

### Beat 4: first pass + human focus (70–85)

1. Type `/pr-focus <PR #3 URL>`.
2. It says what is already covered (CI, agent review) so the human can skip it, then lists
   **two or three questions only a human can answer**, each with a `path:line`:
   - rounding: who keeps the half cent?
   - is `save10` the same as `SAVE10`?
   - should the public API promise a list of codes?
3. It does not answer them. Show the PR template's **human judgement** checkboxes. Those are the
   reviewer's to tick, and nobody else's.

Fallback: [`4-focus.md`](fallback/4-focus.md).

### Close (85–90)

| Layer | Who | Verdict | Lives in |
|---|---|---|---|
| Plan and prune | Agent asks, human answers | Spec on the issue | `refine-ticket` |
| Hygiene | CI, deterministic | **Blocks** | `ci.yml`, `pyproject.toml` |
| Right thing? | Agent, fresh session | **Comments** | `review-pr` |
| Where to look | Agent first pass | **Points** | `pr-focus` |
| Decide | Human | **Decides** | PR template checkboxes |

Never spend a layer's attention on something the layer below can catch.

## Reset for the next run

Delete the agent comments on Issue #2 and PR #3, or recreate both from the seed files.
