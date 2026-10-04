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


def receipt_line(code: str, percent: int) -> str:
    """The line shown on the receipt for an applied promo code."""
    if percent >= 50:
        return f"{code.upper()}: {percent}% off. Big savings!"
    if percent >= 20:
        return f"{code.upper()}: {percent}% off. Nice!"
    if percent > 0:
        return f"{code.upper()}: {percent}% off"
    return f"{code.upper()}: no discount"


def format_cents(cents: int) -> str:
    """Render cents as dollars for the receipt, e.g. 4680 -> "$46.80"."""
    if cents < 0:
        raise ValueError("amount cannot be negative")
    dollars, rest = divmod(cents, 100)
    return f"${dollars}.{rest:02d}"
