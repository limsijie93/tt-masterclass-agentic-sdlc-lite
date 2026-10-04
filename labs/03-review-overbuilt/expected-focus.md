<!-- Lab 03 answer key: a real /pr-focus output on branch labs/03-qty-limit-overbuilt, with the review
     in expected-review.md already on the PR. Line numbers are against that branch. -->

## Where to focus your review

**What changed:** Checkout now rejects any order line with more than 10 of one product, returning a 400 and the message "quantity must be at most 10: <sku>". The PR also adds things the spec ruled out: the cap can be changed through an environment variable, some products can get their own caps, and a switch can make checkout quietly cut quantities to the cap instead of rejecting them.

**Already checked, skip these:**
- CI `hygiene`: ✅ lint, layering, tests, coverage
- Agent review: ran, 3 findings (the env-configurable policy, per-product overrides and quiet clamping are all out of scope; criterion 3 has no test)

**Needs your judgement:**
1. **Charging for less than the customer asked for**: `shop/service.py:25`, `shop/service.py:40-42`
   - The code does: if `SHOP_QTY_STRICT` is set to anything other than `"1"`, an over-limit line is silently reduced to the cap. The customer is charged for the reduced quantity and gets a 200 with no notice.
   - You decide: should any deployment be able to change the order and the amount charged without telling the customer? Or is "the customer must be told" (spec answer 3) a hard rule, so the switch must not exist?
2. **Who can change the cap**: `shop/service.py:23`, `shop/repo.py:5-6`
   - The code does: anyone who controls the environment can change the cap customers see through `SHOP_MAX_QTY`, with no code review. A non-numeric value makes checkout return a 400 with Python's `int()` error text.
   - You decide: Ops' answer 4 says engineering changes the cap in code. Does that still hold, or does Ops actually need to change it without a deploy? If they do, the spec needs updating before this ships.
3. **Which error the customer sees first**: `shop/service.py:38-43`
   - The code does: the quantity cap is checked before the product lookup. An order of 11 of an unknown SKU gets "quantity must be at most 10: <sku>" rather than "unknown product: <sku>".
   - You decide: when a line is both over the limit and for an unknown product, which message should the customer get?

The spec says nothing is "still open for human judgement", yet the code makes these three decisions on its own. Give the spec another pass once items 1 and 2 are settled.

**Read in this order:** `specs/qty-limit.md` → `shop/service.py` → `tests/test_quantity_limit.py`

---
_First pass by an agent. It points; it does not decide. Tick the human-judgement boxes in the
PR description yourself._
