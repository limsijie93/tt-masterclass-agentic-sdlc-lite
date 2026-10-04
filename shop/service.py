"""Business rules. Talks to repo, never to the caller's payload."""

from shop import repo


def order_total(items: dict[str, int], promo_code: str | None = None) -> int:
    """Total in cents for {sku: quantity}, after an optional promo code."""
    if not items:
        raise ValueError("order is empty")
    total = 0
    for sku, qty in items.items():
        if qty < 1:
            raise ValueError(f"quantity must be at least 1: {sku}")
        total += repo.get_price(sku) * qty
    if promo_code:
        # Decided in review: round the discount up, in the customer's favour.
        discount = -(-total * repo.get_promo_percent(promo_code) // 100)
        total -= discount
    return total
