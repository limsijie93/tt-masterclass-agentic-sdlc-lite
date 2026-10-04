"""Business rules. Talks to repo, never to the caller's payload."""

import os
from dataclasses import dataclass, field

from shop import repo


@dataclass(frozen=True)
class QuantityPolicy:
    """How many of each product one order may contain. Tunable without a deploy."""

    default_max: int
    overrides: dict[str, int] = field(default_factory=dict)
    strict: bool = True  # False: quietly reduce to the limit instead of rejecting

    def limit_for(self, sku: str) -> int:
        return self.overrides.get(sku, self.default_max)

    @classmethod
    def from_env(cls) -> "QuantityPolicy":
        return cls(
            default_max=int(os.environ.get("SHOP_MAX_QTY", repo.DEFAULT_MAX_QTY)),
            overrides=dict(repo.MAX_QTY_OVERRIDES),
            strict=os.environ.get("SHOP_QTY_STRICT", "1") == "1",
        )


def order_total(items: dict[str, int], policy: QuantityPolicy | None = None) -> int:
    """Total in cents for {sku: quantity}."""
    if not items:
        raise ValueError("order is empty")
    policy = policy or QuantityPolicy.from_env()
    total = 0
    for sku, qty in items.items():
        if qty < 1:
            raise ValueError(f"quantity must be at least 1: {sku}")
        limit = policy.limit_for(sku)
        if qty > limit:
            if policy.strict:
                raise ValueError(f"quantity must be at most {limit}: {sku}")
            qty = limit
        total += repo.get_price(sku) * qty
    return total
