## Spec: Promo codes at checkout

**Goal:** A customer can enter one promo code at checkout and get a percentage off the order
total.

**Acceptance criteria** (each one is a test someone could write)
1. Given promo code `SAVE10` (10%) and an order totalling 5200 cents, when the customer checks
   out with that code, then the total is 4680 cents.
2. Given a code that does not exist, when the customer checks out with it, then checkout returns
   status 400 with the error `unknown promo code: <code>`.
3. Given no promo code, when the customer checks out, then the total is unchanged.
4. Codes and their percentages are defined in `shop/repo.py`.

**Out of scope** (pruned, and why)
- Fixed-amount, buy-one-get-one, free shipping: the next campaign only uses percentage off (answer 1).
- More than one code per order: one code per order (answer 2).
- Expiry dates and usage limits: codes are removed by hand when a campaign ends (answer 3).
- Admin API for creating codes: engineering adds about three a quarter (answer 5).

**Touches:** `shop/api.py` · `shop/service.py` · `shop/repo.py` · `tests/`

**Still open for human judgement:**
- Rounding: 10% of an odd number of cents. Who keeps the half cent, us or the customer?
- Is `save10` the same code as `SAVE10`?
