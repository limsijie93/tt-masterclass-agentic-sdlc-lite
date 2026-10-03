<!-- Expected output for beat 4: a known-good `/pr-focus` comment on PR #3 (green commit).
     Compare your run against it. Presenters: paste it if a live run misbehaves. -->

## Where to focus your review

**What changed:** Customers can enter promo codes at checkout. One code exists today: `SAVE10`
for 10% off. Unknown codes are rejected with a 400 error.

**Already checked, skip these:**
- CI `hygiene`: ✅ lint, layering, tests, coverage (100%)
- Agent review: ran, 3 findings (stacking, rule engine and expiry are all out of scope). See its comment.

**Needs your judgement:**
1. **Rounding on odd amounts**: `shop/discounts.py:19`
   - The code does: rounds the discount *down* (`subtotal * percent // 100`). 10% off 1205 cents takes off 120, so the customer pays 1085, not 1084.5.
   - You decide: should the half cent go to us or to the customer? The spec left this open.
2. **Is `save10` the same code as `SAVE10`?**: `shop/repo.py:17`
   - The code does: exact match. A customer typing `save10` gets "unknown promo code".
   - You decide: should codes be case-insensitive? The spec left this open, and it is the first support ticket you will get.
3. **The public API takes a list of codes**: `shop/api.py:8`
   - The code does: accepts `promo_codes: [...]`, although the spec says one code per order.
   - You decide: is a list a contract we want front-end clients to build against? Whatever ships here is hard to change later.

**Read in this order:** `specs/2.md` → `shop/service.py` → `shop/api.py`

---
_First pass by an agent. It points; it does not decide. Tick the human-judgement boxes in the
PR description yourself._
