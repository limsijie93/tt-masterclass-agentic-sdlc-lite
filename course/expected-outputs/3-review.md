<!-- Expected output for beat 3: a known-good `/review-pr` comment on PR #3 (green commit).
     Compare your run against it. Presenters: paste it if a live run misbehaves.
     Line numbers are against branch demo/promo-codes. -->

## Agent review: does this build the spec?

**Criteria:** 1 ✅ `shop/service.py:30` / test `tests/test_discounts.py:10` · 2 ✅ `shop/service.py:37` / test `tests/test_discounts.py:18` · 3 ✅ `shop/service.py:22` / test `tests/test_discounts.py:14` · 4 ✅ `shop/repo.py:5`

**Findings** (max 3, most costly first)
1. **Multiple codes per order, including stacking rules**: `shop/service.py:22-24`, `shop/discounts.py:46`, and the API accepts a list (`shop/api.py:8`)
   - Spec says: "More than one code per order: one code per order (answer 2)." (Out of scope)
   - Simpler: take a single `promo_code: str | None`. No stacking check, no `stackable` flag, and the public API does not promise a list.
2. **A pluggable rule engine for one kind of rule**: `shop/discounts.py:8-38` (`DiscountRule` ABC, `FixedAmountOff`, `RULE_TYPES` registry, `register_rule`)
   - Spec says: "Fixed-amount, buy-one-get-one, free shipping: the next campaign only uses percentage off (answer 1)." (Out of scope)
   - Simpler: store the percentage directly, `PROMO_CODES = {"SAVE10": 10}` in `shop/repo.py`, and apply `total -= total * percent // 100` in `service.order_total`. `shop/discounts.py` goes away (54 lines).
3. **Expiry dates and a clock dependency**: `shop/discounts.py:45-49`, `shop/service.py:11,25-28`
   - Spec says: "Expiry dates and usage limits: codes are removed by hand when a campaign ends (answer 3)." (Out of scope)
   - Simpler: delete it. Removing the entry from `PROMO_CODES` is the expiry mechanism the spec chose.

1 further observation withheld: ask for the full list.

---
_Advisory. CI already covers lint, layering, tests and coverage, so they are not repeated
here. This review cannot judge business rules or whether the feature should exist. A human
decides._

<!-- The withheld observation: tests/test_discounts.py:64 registers a rule into the global
     RULE_TYPES and never removes it, so it leaks into every later test. It disappears along
     with finding 2. -->
