from datetime import datetime

import pytest

from shop import api, discounts, repo, service

ORDER = {"tshirt": 2, "mug": 1}  # 5200 cents


def test_percentage_code():
    assert service.order_total(ORDER, ["SAVE10"]) == 4680


def test_no_code_leaves_total_unchanged():
    assert service.order_total(ORDER, []) == 5200


def test_unknown_code_is_rejected_at_checkout():
    response = api.checkout({"items": ORDER, "promo_codes": ["NOPE"]})
    assert response == {"status": 400, "error": "unknown promo code: NOPE"}


def test_checkout_applies_code():
    assert api.checkout({"items": ORDER, "promo_codes": ["SAVE10"]})["total_cents"] == 4680


def test_fixed_amount_rule_never_goes_below_zero():
    assert discounts.FixedAmountOff(amount_cents=9999).discount(500) == 500


def test_stackable_codes_apply_in_order(monkeypatch):
    monkeypatch.setitem(
        repo.PROMO_CODES,
        "FIVEOFF",
        {"rules": [{"type": "fixed", "params": {"amount_cents": 500}}], "stackable": True},
    )
    monkeypatch.setitem(
        repo.PROMO_CODES, "SAVE10", {**repo.PROMO_CODES["SAVE10"], "stackable": True}
    )
    assert service.order_total(ORDER, ["FIVEOFF", "SAVE10"]) == 4230


def test_non_stackable_codes_cannot_be_combined(monkeypatch):
    monkeypatch.setitem(
        repo.PROMO_CODES, "SAVE20", {"rules": [{"type": "percentage", "params": {"percent": 20}}]}
    )
    with pytest.raises(ValueError, match="cannot be combined"):
        service.order_total(ORDER, ["SAVE10", "SAVE20"])


def test_expired_code_is_rejected(monkeypatch):
    monkeypatch.setitem(
        repo.PROMO_CODES,
        "OLD",
        {
            "rules": [{"type": "percentage", "params": {"percent": 50}}],
            "expires_at": datetime(2026, 1, 1),
        },
    )
    with pytest.raises(ValueError, match="expired"):
        service.order_total(ORDER, ["OLD"], now=datetime(2026, 6, 1))


def test_custom_rules_can_be_registered():
    class FreeOrder(discounts.DiscountRule):
        def discount(self, subtotal: int) -> int:
            return subtotal

    discounts.register_rule("free", FreeOrder)
    promo = discounts.build_promo("FREE", {"rules": [{"type": "free", "params": {}}]})
    assert promo.rules[0].discount(1234) == 1234
