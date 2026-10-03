"""Storage layer. The only module that knows how data is kept."""

PRODUCTS = {"tshirt": 2000, "mug": 1200, "poster": 800}  # price in cents


def get_price(sku: str) -> int:
    if sku not in PRODUCTS:
        raise ValueError(f"unknown product: {sku}")
    return PRODUCTS[sku]
