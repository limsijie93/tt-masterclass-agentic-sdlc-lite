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

## One good report (an example)

```
## Harvest: lab 01 (from #<your lab 03 PR>)

6 findings · 3 proposed · 3 logged only

### Proposed
1. **CI check (pyproject.toml)**: ban os.environ in shop/ (ruff banned-api, flake8-tidy-imports)
   - Seen: lab 03 read SHOP_MAX_QTY and SHOP_QTY_STRICT from the environment; ledger 2026-10-03
     #2 #3 "agent built ABC + registry + factory ... [logged: first sighting]"
   - Why here: second sighting of speculative configurability; a machine can catch the
     environment read, so it goes to CI, not prose
2. **AGENTS.md, Domain rules**: never change what a customer ordered or pays without telling
   them; reject with a message instead
   - Seen: lab 03 human review (decision on quiet clamping)
   - Why here: a human decision every later ticket needs
3. **CI check (.github/workflows/ci.yml)**: Scope reads any specs/*.md, not just numbered ones
   - Seen: lab 03, where Scope skipped because the spec is specs/qty-limit.md
   - Why here: a gap in an existing check

### Logged, not proposed
- Per-product overrides and quiet clamping: same shape as proposal 1, covered by it
- Criterion 3 had no test: first sighting, over the 3-proposal cap
- Unknown-SKU vs over-limit error order: this ticket only

_A human merges this. Nothing here takes effect until then._
```

If yours proposed something different but every row of **Check yourself** holds, it's a good
harvest.
