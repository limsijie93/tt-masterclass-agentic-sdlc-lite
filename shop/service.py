"""Business rules. Talks to repo, never to the caller's payload."""

from shop import repo


def order_total(items: dict[str, int]) -> int:
    """Total in cents for {sku: quantity}."""
    if not items:
        raise ValueError("order is empty")
    total = 0
    for sku, qty in items.items():
        if qty < 1:
            raise ValueError(f"quantity must be at least 1: {sku}")
        price = repo.get_price(sku)  # decided in review: an unknown product is reported first
        if qty > repo.MAX_QTY:
            raise ValueError(f"quantity must be at most {repo.MAX_QTY}: {sku}")
        total += price * qty
    return total
