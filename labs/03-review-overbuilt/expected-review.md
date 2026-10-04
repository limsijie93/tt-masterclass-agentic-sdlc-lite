<!-- Lab 03 answer key: a real /review-pr output on branch labs/03-qty-limit-overbuilt, from a fresh
     session that had not seen the code. Line numbers are against that branch. -->

## Agent review: does this build the spec?

**Criteria:** 1 ✅ `shop/service.py:38-43` / test `tests/test_quantity_limit.py:6` · 2 ✅ `shop/service.py:41` → `shop/api.py:11-12` / test `tests/test_quantity_limit.py:10` · 3 ❌ no test proves the limit is the same for every product, and `shop/service.py:18` with `shop/repo.py:6` lets limits differ per product

**Findings** (max 3, most costly first)
1. **`QuantityPolicy` class that reads the limit from the environment ("Tunable without a deploy")**: `shop/service.py:9-26`, `shop/service.py:29`, `shop/service.py:33`
   - Spec says: "Configuring the limit from the environment or an admin screen: engineering changes it in code, rarely (answer 4)."
   - Simpler: drop the class, the `policy` parameter, the `os` and `dataclass` imports, and the `SHOP_MAX_QTY`/`SHOP_QTY_STRICT` env reads. Use `MAX_QTY = 10` in `shop/repo.py` and `if qty > repo.MAX_QTY: raise ValueError(f"quantity must be at most {repo.MAX_QTY}: {sku}")` in the loop. Delete `tests/test_quantity_limit.py:20-23`.
2. **Per-product limit overrides**: `shop/repo.py:6`, `shop/service.py:14`, `shop/service.py:17-18`, `shop/service.py:24`
   - Spec says: "Different limits per product: Ops wants one simple cap for now (answer 2)." and criterion 3: "The limit is the same for every product."
   - Simpler: remove `MAX_QTY_OVERRIDES` and `limit_for`, and compare against the single constant. Replace `tests/test_quantity_limit.py:15-17` with a test showing that 11 of a second product (e.g. `poster`) is also rejected. That test is what closes criterion 3.
3. **Non-strict mode that quietly reduces the quantity to the limit**: `shop/service.py:15`, `shop/service.py:25`, `shop/service.py:40-42`
   - Spec says: "Quietly reducing an over-limit quantity: the customer must be told (answer 3)."
   - Simpler: always raise. Delete the `strict` field, the `qty = limit` branch and `tests/test_quantity_limit.py:26-28`.

---
_Advisory. CI already covers lint, layering, tests and coverage, so they are not repeated
here. This review cannot judge business rules or whether the feature should exist. A human
decides._
