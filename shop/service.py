"""Business rules. Talks to repo, never to the caller's payload."""

from datetime import datetime

from shop import discounts, repo


def order_total(
    items: dict[str, int],
    promo_codes: list[str] | None = None,
    now: datetime | None = None,
) -> int:
    """Total in cents for {sku: quantity}, after any promo codes."""
    if not items:
        raise ValueError("order is empty")
    total = 0
    for sku, qty in items.items():
        if qty < 1:
            raise ValueError(f"quantity must be at least 1: {sku}")
        total += repo.get_price(sku) * qty

    promos = [load_promo(code) for code in promo_codes or []]
    if len(promos) > 1 and not all(p.stackable for p in promos):
        raise ValueError("these promo codes cannot be combined")
    now = now or datetime.now()
    for promo in promos:
        if not promo.is_active(now):
            raise ValueError(f"promo code expired: {promo.code}")
        for rule in promo.rules:
            total -= rule.discount(total)
    return max(total, 0)


def load_promo(code: str) -> discounts.PromoCode:
    config = repo.get_promo_config(code)
    if config is None:
        raise ValueError(f"unknown promo code: {code}")
    return discounts.build_promo(code, config)
