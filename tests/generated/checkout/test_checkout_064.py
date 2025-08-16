import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-3781", "title": "Checkout scenario 3781", "data": {"sku": "SKU3781", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3781@example.com", "threshold": 810}},
    {"id": "CHECKOUT-3782", "title": "Checkout scenario 3782", "data": {"sku": "SKU3782", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3782@example.com", "threshold": 820}},
    {"id": "CHECKOUT-3783", "title": "Checkout scenario 3783", "data": {"sku": "SKU3783", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3783@example.com", "threshold": 830}},
    {"id": "CHECKOUT-3784", "title": "Checkout scenario 3784", "data": {"sku": "SKU3784", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3784@example.com", "threshold": 840}},
    {"id": "CHECKOUT-3785", "title": "Checkout scenario 3785", "data": {"sku": "SKU3785", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3785@example.com", "threshold": 850}},
    {"id": "CHECKOUT-3786", "title": "Checkout scenario 3786", "data": {"sku": "SKU3786", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3786@example.com", "threshold": 860}},
    {"id": "CHECKOUT-3787", "title": "Checkout scenario 3787", "data": {"sku": "SKU3787", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3787@example.com", "threshold": 870}},
    {"id": "CHECKOUT-3788", "title": "Checkout scenario 3788", "data": {"sku": "SKU3788", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3788@example.com", "threshold": 880}},
    {"id": "CHECKOUT-3789", "title": "Checkout scenario 3789", "data": {"sku": "SKU3789", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3789@example.com", "threshold": 890}},
    {"id": "CHECKOUT-3790", "title": "Checkout scenario 3790", "data": {"sku": "SKU3790", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3790@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
