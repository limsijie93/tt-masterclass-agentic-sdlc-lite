# Harvest ledger

Append-only. One line per finding that `/harvest` read, **including the ones it did not propose**.
Those are the point: some rules only fire on a second sighting, and one ticket can't see a
repeat. This file is the memory that makes the second sighting countable.

Don't edit or reorder past lines. A ledger someone has tidied can't be counted.

```
<date>      <ticket>  <PR>  <home, or "none">         <finding>
```

---
2026-10-03  #2  #3  none                          CI caught unused `json` import (F401) on fbb0cc1 [logged: CI already catches it]
2026-10-03  #2  #3  none                          CI caught shop/api.py importing shop.repo on fbb0cc1 [logged: CI already catches it]
2026-10-03  #2  #3  none                          CI caught coverage 78% < 90% on fbb0cc1 [logged: CI already catches it]
2026-10-03  #2  #5  none                          CI caught unused `json` import (F401) [logged: CI already catches it]
2026-10-03  #2  #5  none                          CI caught shop/api.py importing shop.repo [logged: CI already catches it]
2026-10-03  #2  #5  none                          CI caught coverage 86.5% < 90% (receipt_line, format_cents untested) [logged: CI already catches it]
2026-10-03  #2  #3  .github/workflows/ci.yml      new file shop/discounts.py not listed under the spec's Touches [proposed]
2026-10-03  #2  #3  AGENTS.md Rules               agent built ABC + registry + factory for one percentage rule, despite the existing rule [logged: first sighting]
2026-10-03  #2  #3  AGENTS.md Rules               agent built several codes per order with stacking, out of scope in the spec [logged: first sighting]
2026-10-03  #2  #3  AGENTS.md Rules               agent built expiry dates + an injectable clock, out of scope in the spec [logged: first sighting]
2026-10-03  #2  #4  AGENTS.md Domain rules        human decided: a fraction of a cent goes to the customer, so a discount rounds up [proposed]
2026-10-03  #2  #4  none                          human decided: promo codes are case-insensitive [logged: a test already enforces it]
2026-10-03  #2  #3  .claude/skills/refine-ticket  spec left rounding and case "Still open"; the builder guessed both wrong [proposed]
2026-10-03  #2  #3  .claude/skills/review-pr      review's "Simpler" code took a side (round down) on an open spec question [logged: first sighting, over the 3-proposal cap]

