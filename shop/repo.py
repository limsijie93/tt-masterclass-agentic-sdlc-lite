"""Storage layer. The only module that knows how data is kept."""

PRODUCTS = {"tshirt": 2000, "mug": 1200, "poster": 800}  # price in cents

MAX_QTY = 10  # per product, per order. Changed in code: Ops' answer 4


def get_price(sku: str) -> int:
    if sku not in PRODUCTS:
        raise ValueError(f"unknown product: {sku}")
    return PRODUCTS[sku]
