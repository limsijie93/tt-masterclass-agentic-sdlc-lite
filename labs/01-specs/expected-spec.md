<!-- Lab 01 answer key: a good spec from /refine-ticket after Sam's answers. Lab 03 builds exactly this spec
     (branch labs/03-qty-limit-overbuilt, specs/qty-limit.md). Compare substance, not wording. -->

## Spec: Cap the quantity per item

**Goal:** Stop accidental huge orders: a customer can order at most 10 of any one product.

**Acceptance criteria** (each one is a test someone could write)
1. Given a quantity of 10 for a product, when the customer checks out, then the order is accepted.
2. Given a quantity of 11 for a product, when the customer checks out, then checkout returns
   status 400 with the error `quantity must be at most 10: <sku>`.
3. The limit is the same for every product.

**Out of scope** (pruned, and why)
- Different limits per product: Ops wants one simple cap for now (answer 2).
- Configuring the limit from the environment or an admin screen: engineering changes it in code, rarely (answer 4).
- Quietly reducing an over-limit quantity: the customer must be told (answer 3).
- Limits per customer or across orders: not the problem Ops reported (answer 1).

**Touches:** `shop/service.py` · `shop/repo.py` · `tests/`

**Still open for human judgement:** none.
