import pytest

from shop import api, service


def test_ten_is_accepted():  # criterion 1
    assert service.order_total({"mug": 10}) == 12000


def test_eleven_is_rejected_at_checkout():  # criterion 2
    response = api.checkout({"items": {"mug": 11}})
    assert response == {"status": 400, "error": "quantity must be at most 10: mug"}


@pytest.mark.parametrize("sku", ["tshirt", "mug", "poster"])
def test_same_limit_for_every_product(sku):  # criterion 3
    with pytest.raises(ValueError, match="at most 10"):
        service.order_total({sku: 11})


def test_unknown_product_is_reported_before_the_limit():  # decided in review
    with pytest.raises(ValueError, match="unknown product: hat"):
        service.order_total({"hat": 11})
