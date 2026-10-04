"""Storage layer. The only module that knows how data is kept."""

PRODUCTS = {"tshirt": 2000, "mug": 1200, "poster": 800}  # price in cents

PROMO_CODES = {"SAVE10": 10}  # code -> percent off the order


def get_price(sku: str) -> int:
    if sku not in PRODUCTS:
        raise ValueError(f"unknown product: {sku}")
    return PRODUCTS[sku]


def get_promo_percent(code: str) -> int:
    key = code.upper()  # decided in review: codes are case-insensitive
    if key not in PROMO_CODES:
        raise ValueError(f"unknown promo code: {code}")
    return PROMO_CODES[key]
