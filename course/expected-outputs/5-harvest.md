<!-- Expected output for the harvest beat: the report /harvest wrote for #3, #4 and #5.
     It is also the description of PR #6. Compare your run against it. -->

## Harvest: #2 (from #3, #4, #5)

14 findings · 3 proposed · 11 logged only

### Proposed
1. **CI check (`.github/workflows/ci.yml`)**: a new **Scope** step. It fails when a PR changes a file the PR's spec doesn't list under **Touches**.
   - Seen: #3 added `shop/discounts.py` (ABC, registry, factory, fixed-amount rule). The spec's Touches line is `shop/api.py · shop/service.py · shop/repo.py · tests/`. The agent review on #3 caught this only as advice.
   - Why here: comparing changed files with a list in the spec is a machine check, so CI can block it. A rule in `AGENTS.md` or a review comment only advises.
2. **`AGENTS.md`, Domain rules**: a fraction of a cent goes to the customer, so a discount rounds up.
   - Seen: #3 rounded the discount down (`shop/discounts.py:19`). The reviewer reversed that, recorded in #4 (`specs/2.md`, "Decided in review of #3").
   - Why here: a human decided a money rule that every later price calculation needs. No check can derive a business decision.
3. **`refine-ticket` skill, Rules**: a guess that changes a test's expected value must be a Phase 1 question, never a "Still open" line.
   - Seen: the spec for #3 left rounding and case "Still open". The builder guessed both wrong, and #4 had to undo both guesses.
   - Why here: the question belonged before any code existed. Fixing it at the source costs less than catching it in review.

### Logged, not proposed
- #3 (first commit) and #5: unused `json` import, `shop/api.py` importing `shop.repo`, coverage under 90%: **CI already catches all three** (six findings). The deterministic layer worked.
- #3: ABC + registry + factory for one percentage rule: first sighting. `AGENTS.md` already says "no base class with one subclass, no registry", and the agent ignored it. A second sighting moves it out of prose.
- #3: several codes per order with stacking, out of scope: first sighting.
- #3: expiry dates and an injectable clock, out of scope: first sighting.
- #4: promo codes are case-insensitive (human decision): a test already enforces it.
- #3: the review's "Simpler" code took a side (round down) on a question the spec left open: first sighting, over the 3-proposal cap.

All 14 findings are appended to [`harvest/ledger.md`](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/blob/harvest/2/harvest/ledger.md), so the next harvest can count a second sighting.

### Checked
The Scope step was run against each PR's merge commit: **#3 fails** on `shop/discounts.py`, **#4 passes**, #5 and this PR are skipped (no spec in the diff).

_A human merges this. Nothing here takes effect until then._
