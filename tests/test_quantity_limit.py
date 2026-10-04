import pytest

from shop import api, repo, service


def test_ten_is_accepted():
    assert service.order_total({"mug": 10}) == 12000


def test_eleven_is_rejected_at_checkout():
    response = api.checkout({"items": {"mug": 11}})
    assert response == {"status": 400, "error": "quantity must be at most 10: mug"}


def test_per_product_override(monkeypatch):
    monkeypatch.setitem(repo.MAX_QTY_OVERRIDES, "poster", 50)
    assert service.order_total({"poster": 50}) == 40000


def test_limit_from_environment(monkeypatch):
    monkeypatch.setenv("SHOP_MAX_QTY", "3")
    with pytest.raises(ValueError, match="at most 3"):
        service.order_total({"mug": 4})


def test_non_strict_policy_clamps_quietly():
    policy = service.QuantityPolicy(default_max=2, strict=False)
    assert service.order_total({"mug": 5}, policy) == 2400
