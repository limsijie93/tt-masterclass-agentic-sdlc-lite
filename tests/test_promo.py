from shop import api, repo, service

ORDER = {"tshirt": 2, "mug": 1}  # 5200 cents


def test_percentage_code():  # criterion 1
    assert service.order_total(ORDER, "SAVE10") == 4680


def test_unknown_code_is_rejected_at_checkout():  # criterion 2
    response = api.checkout({"items": ORDER, "promo_code": "NOPE"})
    assert response == {"status": 400, "error": "unknown promo code: NOPE"}


def test_no_code_leaves_total_unchanged():  # criterion 3
    assert service.order_total(ORDER) == 5200


def test_checkout_applies_code():
    assert api.checkout({"items": ORDER, "promo_code": "SAVE10"})["total_cents"] == 4680


def test_codes_are_case_insensitive():  # decided in review
    assert service.order_total(ORDER, "save10") == 4680


def test_discount_rounds_in_the_customers_favour(monkeypatch):  # decided in review
    monkeypatch.setitem(repo.PRODUCTS, "pin", 1205)
    assert service.order_total({"pin": 1}, "SAVE10") == 1084  # 120.5 off rounds up to 121
