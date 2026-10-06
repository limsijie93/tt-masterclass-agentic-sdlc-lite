# Lab 04 · Answer key

Harvest output depends on your lab 03 review and your decisions, so there's no single right
report. A good one gets these right:

| Finding from lab 03 | Good routing | Why |
|---|---|---|
| Overbuilding: a policy class, environment config, per-product overrides, quiet clamping | **Proposed**, citing the ledger's `#2 … first sighting` lines from the demo | Second sighting of "the agent builds for flexibility nobody asked for". The twice rule fires. |
| ↳ where it goes | A **check** if one fits (e.g. ruff `banned-api` for `os.environ` inside `shop/`), otherwise a sharper line in `AGENTS.md` **Rules** that says which line it replaces | Prefer the machine. The existing prose rule was ignored twice. |
| Criterion 3 had no test | A **check** or the **`review-pr` skill**, e.g. "every acceptance criterion names its test" | The review caught it, but only as advice |
| The Scope check skipped this PR (its spec is `specs/qty-limit.md`, not `specs/<number>.md`) | **Proposed** as a machine check: widen Scope to any `specs/*.md` | It's a gap in a check, found by using it |
| Your decision: "never change a customer's order without telling them" | `AGENTS.md` **Domain rules** | A human decision the next ticket needs |
| Your decision on which error comes first | `AGENTS.md` **Domain rules**, or logged if it only matters here | Depends on whether it generalises |
| Anything CI caught | **Logged**, not proposed | Nothing: lab 03 was green |

At most three of these are **proposed**. The rest are **logged**, and the ledger grows by every
row.

## One good report (a real run)

A real `/harvest` run by Claude Opus 5.5 (medium effort), on 2026-10-06. Its input was the lab 03
branch with the reviews in [`expected-review.md`](../03-review-overbuilt/expected-review.md) and
[`expected-focus.md`](../03-review-overbuilt/expected-focus.md), the demo's ledger from `harvest/2`,
and this human review (*Request changes*):

```
1. Never change a customer's order without telling them: remove the non-strict mode, always reject.
2. The cap changes in code only. Ops confirmed answer 4 still holds, so drop the environment variables.
3. When a line is both over the limit and an unknown product, report the unknown product first.
4. One cap for every product, as the spec says: drop the per-product overrides.
```

Your decisions will differ, so your report will too. The PR description it drafted:

````markdown
## Harvest: lab01 qty-limit (from `labs/03-qty-limit-overbuilt`)

10 findings · 3 proposed (covering 4 findings) · 6 logged only

### Proposed
1. **CI check (`pyproject.toml`)**: ban `os.environ` / `os.getenv` with ruff `banned-api` (TID251), so a fixed value can't become environment config.
   - Seen: `labs/03-qty-limit-overbuilt`, `shop/service.py:21-26` (`QuantityPolicy.from_env` reads `SHOP_MAX_QTY`, `SHOP_QTY_STRICT`). Agent review finding 1; human review point 2 ("The cap changes in code only").
   - Why here: `AGENTS.md` already says "no config for a value that never changes", and the agent ignored it. A machine can see an environment read, so this belongs in CI, not in more prose. Nothing in `shop/` reads the environment today.
2. **`AGENTS.md` Rules**: make the "build only the spec" rule check the spec's **Out of scope** list against the diff.
   - Seen: `labs/03-qty-limit-overbuilt`, per-product overrides (`shop/repo.py:6`, `shop/service.py:17-18`) and quiet clamping (`shop/service.py:40-42`). Both are on the spec's Out of scope list and were built anyway. Agent review findings 2 and 3; human review points 1 and 4.
   - Why here: **second sighting.** The ledger has `2026-10-03 #2 #3 AGENTS.md Rules agent built several codes per order with stacking, out of scope in the spec [logged: first sighting]` and `… expiry dates + an injectable clock, out of scope in the spec [logged: first sighting]`. No machine can read an Out of scope line, so the existing rule gets a concrete step instead.
3. **`AGENTS.md` Domain rules**: never change a customer's order without telling them.
   - Seen: `labs/03-qty-limit-overbuilt`, human review point 1, on the non-strict mode at `shop/service.py:40-42`.
   - Why here: a human made a business decision that applies beyond this cap (any future limit, stock check or substitution), so the next ticket shouldn't have to ask again. No check can catch "quietly" in general.

**1. `pyproject.toml`**

Replaces the `select` line under `[tool.ruff.lint]`:
```toml
select = ["E", "F", "I", "B", "UP", "SIM", "TID251"]
```
New section, added after `[tool.ruff.lint]` (replaces none):
```toml
# Added by /harvest (lab01): labs/03 read the quantity cap from SHOP_MAX_QTY / SHOP_QTY_STRICT.
# Values change in code, reviewed, never from the environment.
[tool.ruff.lint.flake8-tidy-imports.banned-api]
"os.environ".msg = "Configuration lives in code (shop/repo.py), not the environment. See AGENTS.md Rules."
"os.getenv".msg = "Configuration lives in code (shop/repo.py), not the environment. See AGENTS.md Rules."
```

**2. `AGENTS.md`, under `## Rules`**

Replaces the line `- Build what the spec asks for and nothing else. If a spec exists in \`specs/\`, every change must trace to an acceptance criterion.` with:
```markdown
- Build what the spec asks for and nothing else. If a spec exists in `specs/`, every change
  must trace to an acceptance criterion. Before you open the PR, read each **Out of scope**
  line of the spec against your diff and delete anything that builds it, including as an
  option, a flag, an empty override table or a default-off mode. Seen twice: #3 (#2) built
  stacking and expiry; labs/03 built per-product caps and quiet clamping.
```

**3. `AGENTS.md`, under `## Domain rules`**

Replaces none (appended after the rounding rule):
```markdown
- Never change a customer's order without telling them. If a line can't be filled as ordered,
  reject the checkout with an error that names the sku. Never reduce, drop or substitute
  quietly, not even behind a flag. Decided in review of labs/03-qty-limit-overbuilt (lab01).
```

### Logged, not proposed
- Criterion 3 ("same limit for every product") has no test: this ticket only. The agent review caught it, and the fix belongs in the next PR on the ticket.
- Human decided an unknown product is reported before over-limit (`shop/service.py:38-43`): first sighting, over the 3-proposal cap. Next harvest: `AGENTS.md` Domain rules.
- Human confirmed the cap changes in code only (answer 4): this ticket only. The spec already says it, and proposal 1 enforces it.
- Human confirmed one cap for every product (answer 2): this ticket only. The spec already says it.
- A bad `SHOP_MAX_QTY` returns Python's `int()` error text to the customer (found by pr-focus): this ticket only. It goes away when the environment config is removed.
- CI Scope step was skipped because the spec is `specs/qty-limit.md`, not `specs/<N>.md`: this ticket only. The lab ticket has no issue number, and every changed file was under Touches anyway.

_A human merges this. Nothing here takes effect until then._
````

And the lines it appends to `harvest/ledger.md`:

```
2026-10-06  lab01  labs/03  pyproject.toml                env config for the cap (QuantityPolicy.from_env, SHOP_MAX_QTY, SHOP_QTY_STRICT), out of scope [proposed]
2026-10-06  lab01  labs/03  AGENTS.md Rules               agent built per-product limit overrides, out of scope in the spec [proposed: second sighting, see #2 #3]
2026-10-06  lab01  labs/03  AGENTS.md Rules               agent built a non-strict mode that quietly clamps quantity, out of scope in the spec [proposed: same Rules line]
2026-10-06  lab01  labs/03  AGENTS.md Domain rules        human decided: never change a customer's order without telling them, always reject [proposed]
2026-10-06  lab01  labs/03  AGENTS.md Domain rules        human decided: unknown product is reported before over-limit [logged: first sighting, over the 3-proposal cap]
2026-10-06  lab01  labs/03  none                          criterion 3 (same limit for every product) untested; agent review caught it [logged: this ticket only]
2026-10-06  lab01  labs/03  none                          human confirmed the cap changes in code only (answer 4) [logged: this ticket only, already in spec]
2026-10-06  lab01  labs/03  none                          human confirmed one cap for every product (answer 2) [logged: this ticket only, already in spec]
2026-10-06  lab01  labs/03  none                          bad SHOP_MAX_QTY leaks Python int() error to the customer (pr-focus) [logged: this ticket only]
2026-10-06  lab01  labs/03  none                          CI Scope step skipped: spec named specs/qty-limit.md, not specs/<N>.md [logged: this ticket only]
```

If yours proposed something different but every row of **Check yourself** holds, it's a good
harvest.
