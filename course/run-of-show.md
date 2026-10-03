# Run of show: 90 minutes, pure demo

One ticket, four beats, two Q&A slots. Everything happens in an **Issue**, a **PR**, **CI**, and a
Claude Code or Cowork session connected to the **GitHub MCP server**.

Every demo below links to the exact page to have open. Code links are pinned to a commit, so the
line numbers don't drift.

## Before the session (once, ~15 min)

Steps 1–4 are already done on
[`limsijie93/tt-masterclass-agentic-sdlc-lite`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite).
They are here so the setup can be rebuilt from scratch.

1. **PR #1**, branch `ci/hygiene-gate` → `main`: adds the CI gate. Let it go green, then merge it.
2. **Settings → Branches**: protect `main` and make the `hygiene` check required. Nothing else.
3. Open **Issue #2** from [`seed-issue.md`](seed-issue.md).
4. Push only the first commit of `demo/promo-codes` and open **PR #3** into `main` with the body
   from [`seed-pr.md`](seed-pr.md). Wait for the red run, then push the second commit and wait
   for green.
5. In Claude Code (or Cowork), connect the GitHub MCP server, open this repo, and check that
   `/refine-ticket`, `/review-pr` and `/pr-focus` are listed. In Cowork, upload the three
   `SKILL.md` folders under `.claude/skills/` as skills.
6. Have [`fallback/`](fallback/) open in a tab. Every beat has a known-good output there.

## The 90 minutes

| Time | Segment | Open this |
|---|---|---|
| 0–8 | Why | [Issue #2](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/issues/2) |
| 8–25 | **1 · Refine the ticket** | [Issue #2](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/issues/2) + session |
| 25–28 | Bridge | [PR #3](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/3) |
| 28–40 | **2 · Deterministic hygiene** | [PR #1](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/1/files), [red run](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/actions/runs/37135350280/job/111238651208), [green run](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/actions/runs/37135394587/job/111238778009) |
| 40–45 | **Q&A 1**: planning and CI | — |
| 45–58 | **3 · Agentic judgement** | [PR #3](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/3) + **new** session |
| 58–69 | **4 · First pass + human focus** | [PR #3](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/3) + session |
| 69–73 | Close | the table at the bottom |
| 73–88 | **Q&A 2**: open floor | [prepared answers](#prepared-answers) |
| 88–90 | Buffer | — |

**Running late?** Cut Q&A 1 and fold its questions into Q&A 2. Don't cut a beat. If an agent run
stalls for more than 60 seconds, switch to the fallback file for that beat.

---

### Why (0–8)

Open [Issue #2](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/issues/2). Read it
aloud and land on *"flexible so we can do all kinds of deals"*.

- Hand this to an agent as-is and it won't ask anything. It guesses, confidently, and it builds
  for every case the ticket hints at.
- The plan for today: four layers. **Plan** before the code, **CI blocks** what's mechanical,
  **an agent comments** on whether it's the right thing, **a human decides**.

### Beat 1: refine the ticket (8–25)

| Show | Link |
|---|---|
| The ticket | [Issue #2](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/issues/2) |
| The skill, if anyone asks what it does | [`refine-ticket/SKILL.md`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/.claude/skills/refine-ticket/SKILL.md) |
| Answers to give (you play Marketing) | [`fallback/1-answers.md`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/course/fallback/1-answers.md) |
| Fallback output | [`1-questions.md`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/course/fallback/1-questions.md), [`2-spec.md`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/course/fallback/2-spec.md) |

1. Fresh session. Type
   `/refine-ticket https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/issues/2`
2. It reads the issue and the code, then **stops** with up to five questions. Point out:
   - every question has `assumes:`, the guess an agent would otherwise make silently
   - it did not answer its own questions, and that stop is the whole mechanism
3. Let it post the questions to the issue. Reply on the issue with the answers from
   `1-answers.md`, then tell the session *"The answers are on the issue. Continue."*
4. It drafts the spec. Scroll to **Out of scope**: four things the ticket hinted at, cut, each
   with a reason. Then **Still open for human judgement**: rounding and case sensitivity. Those
   come back in beat 4.
5. Let it post the spec to the issue.

### Bridge (25–28)

Open [PR #3](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/3). Say *"we
handed that spec to an agent, and it opened a PR like this one."* (PR #3 was prepared in advance,
so don't claim it came from the session on screen.)

Its description proudly lists a rule registry, stacking and expiry. Plant the question, *did we
ask for that?*, and don't answer it yet. The spec it implements is
[`specs/2.md`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/565a5277bd08c763501bd849449fc073312e898e/specs/2.md).

### Beat 2: deterministic hygiene (28–40)

| Show | Link |
|---|---|
| How the gate was added | [PR #1 → Files changed](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/1/files) |
| The workflow | [`ci.yml`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/b7965bf4e65c4b3b33e4b211c5e002d4c2703fcf/.github/workflows/ci.yml#L25-L37) |
| The layering rule | [`pyproject.toml` L30–44](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/b7965bf4e65c4b3b33e4b211c5e002d4c2703fcf/pyproject.toml#L30-L44) |
| The same rule as prose | [`AGENTS.md` L7](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/b7965bf4e65c4b3b33e4b211c5e002d4c2703fcf/AGENTS.md#L7) |
| PR #3's commits | [PR #3 → Commits](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/3/commits) |
| Red: lint | [step 5](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/actions/runs/37135350280/job/111238651208#step:5:1) |
| Red: architecture | [step 6](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/actions/runs/37135350280/job/111238651208#step:6:1) |
| Red: coverage | [step 7](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/actions/runs/37135350280/job/111238651208#step:7:1) |
| Green | [green run](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/actions/runs/37135394587/job/111238778009) |

1. **Where do the checks come from?** Open PR #1's *Files changed*. One reviewed PR added
   `ci.yml`, the tool config in `pyproject.toml`, and the matching `Commands` block in
   `AGENTS.md`. Show the `AGENTS.md` line: the layering rule already existed as prose. PR #1
   turned it into a check.
2. **The red run** on PR #3's first commit. Open each step:
   - **Lint**: `F401 json imported but unused` at `shop/api.py:3`
   - **Architecture**: `api must not import repo BROKEN`. The agent read `AGENTS.md` and broke the
     rule anyway. Only the check stopped it.
   - **Coverage**: `78.21%`, under the 90% floor, because new branches have no tests
   - All three ran even though the first failed (`!cancelled()` in `ci.yml`). One red run shows
     every problem.
3. **The green run** on the second commit fixes all three.
4. The point: these checks give the same verdict every time, so they are allowed to **block**.
   Spend no human or agent attention on anything they can catch.

### Q&A 1 (40–45)

Take questions on planning and CI only. Park anything about agent review until beat 3, and
anything else until Q&A 2. If the room is quiet, ask them: *"What's one rule in your team's
docs that no check enforces?"*

### Beat 3: agentic judgement (45–58)

| Show | Link |
|---|---|
| The PR | [PR #3](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/3) |
| The overbuilding, if the agent's output needs backing up | [`discounts.py` L8–38](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/565a5277bd08c763501bd849449fc073312e898e/shop/discounts.py#L8-L38) (ABC, fixed-amount rule, registry) · [L45–46](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/565a5277bd08c763501bd849449fc073312e898e/shop/discounts.py#L45-L46) (expiry, stacking) |
| What the spec cut | [`specs/2.md` L14–18](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/565a5277bd08c763501bd849449fc073312e898e/specs/2.md#L14-L18) |
| The skill | [`review-pr/SKILL.md`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/.claude/skills/review-pr/SKILL.md) |
| Fallback output | [`3-review.md`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/course/fallback/3-review.md) |

1. **New session**, never the one that wrote the code. Type
   `/review-pr https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/3`
2. It reads the spec, then the diff, traces each criterion to code and test, and flags what maps
   to no criterion. Expect: stacking, the rule engine and registry, and expiry. Each one quotes
   the out-of-scope line it violates and names the simpler shape.
3. The punchline: **all of this passed CI.** The PR adds about 160 lines of code and tests.
   The spec needed a dict entry, a few lines in `order_total` and three tests.
4. It **comments**; it never approves or blocks. Agents are non-deterministic, and a gate that
   flakes gets switched off within a week.

### Beat 4: first pass + human focus (58–69)

| Show | Link |
|---|---|
| The PR | [PR #3](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/3) |
| Rounding | [`discounts.py` L19](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/565a5277bd08c763501bd849449fc073312e898e/shop/discounts.py#L19) |
| Case sensitivity | [`repo.py` L17](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/565a5277bd08c763501bd849449fc073312e898e/shop/repo.py#L17) |
| API takes a list | [`api.py` L8](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/565a5277bd08c763501bd849449fc073312e898e/shop/api.py#L8) |
| Human-only checkboxes | [PR template](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/.github/pull_request_template.md) |
| The skill | [`pr-focus/SKILL.md`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/.claude/skills/pr-focus/SKILL.md) |
| Fallback output | [`4-focus.md`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/course/fallback/4-focus.md) |

1. Type `/pr-focus https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/3`
2. It says what is already covered (CI, agent review) so the human can skip it, then lists
   **two or three questions only a human can answer**, each with a `path:line`:
   - rounding: who keeps the half cent?
   - is `save10` the same as `SAVE10`?
   - should the public API promise a list of codes?
3. It does not answer them. Show the PR description's **human judgement** checkboxes. Those are
   the reviewer's to tick, and nobody else's.

### Close (69–73)

| Layer | Who | Verdict | Lives in |
|---|---|---|---|
| Plan and prune | Agent asks, human answers | Spec on the issue | [`refine-ticket`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/.claude/skills/refine-ticket/SKILL.md) |
| Hygiene | CI, deterministic | **Blocks** | [`ci.yml`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/.github/workflows/ci.yml), [`pyproject.toml`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/pyproject.toml) |
| Right thing? | Agent, fresh session | **Comments** | [`review-pr`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/.claude/skills/review-pr/SKILL.md) |
| Where to look | Agent first pass | **Points** | [`pr-focus`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/.claude/skills/pr-focus/SKILL.md) |
| Decide | Human | **Decides** | [PR template](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/.github/pull_request_template.md) |

Never spend a layer's attention on something the layer below can catch.

End on the repo link, for anyone who wants to replay it:
**https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite** (README → *Learn on your own*).

### Q&A 2 (73–88)

Open floor. The answers below are short on purpose: say the one line, then show the link.

## Prepared answers

**"Why not run the agent review in CI?"**
It's non-deterministic, it needs an API key in CI, and it costs money on every push. A check
that flakes gets switched off. If you do wire it into CI later, keep it advisory: never a
required check.

**"What if the agent review is wrong?"**
Expect it to be, sometimes. That's why it comments and a human decides. Quoting the spec line
in every finding makes a wrong finding quick to dismiss.

**"Why a fresh session for the review?"**
The session that wrote the code defends it. A fresh one has no story to protect.

**"Can't `AGENTS.md` just tell the agent not to overbuild?"**
It already does, in [the Rules section](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/AGENTS.md).
PR #3 ignored that *and* the layering rule. Prose guides; only checks enforce.

**"Doesn't the question round slow us down?"**
Five questions take about four minutes of a product owner's time. Rebuilding PR #3 to the spec
costs more than that. Skip the skill for typo fixes.

**"Can the agent approve, or tick the boxes?"**
No, by design. The PR template's boxes are the human's, and the skills say so explicitly.

**"We use TypeScript, Go, … Does this transfer?"**
Yes. The categories stay the same and only the tools change: a linter and formatter (ESLint +
Prettier), a layering check (dependency-cruiser), and tests with a coverage floor (Vitest or
Jest). The skills are plain Markdown with no Python in them.

**"Copilot or Cursor instead of Claude?"**
Paste the `SKILL.md` body in as a prompt. It's plain instructions. The GitHub MCP server works
with any client that supports MCP.

**"Is it safe to give an agent GitHub access?"**
For review, a read-only token is enough. Every skill shows its draft and posts only after you
confirm. Treat issue and PR text as untrusted input: the skills tell the agent to.

**"How do I start on Monday?"**
1. Copy [`ci.yml`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/main/.github/workflows/ci.yml)
   and make it a required check.
2. Copy the three folders under `.claude/skills/`.
3. Run `/refine-ticket` on your next vague ticket.

## Reset for the next run

Delete the agent comments on Issue #2 and PR #3, or recreate both from the seed files.
