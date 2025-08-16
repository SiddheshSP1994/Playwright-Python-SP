import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6781", "title": "Checkout scenario 6781", "data": {"sku": "SKU6781", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6781@example.com", "threshold": 810}},
    {"id": "CHECKOUT-6782", "title": "Checkout scenario 6782", "data": {"sku": "SKU6782", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6782@example.com", "threshold": 820}},
    {"id": "CHECKOUT-6783", "title": "Checkout scenario 6783", "data": {"sku": "SKU6783", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6783@example.com", "threshold": 830}},
    {"id": "CHECKOUT-6784", "title": "Checkout scenario 6784", "data": {"sku": "SKU6784", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6784@example.com", "threshold": 840}},
    {"id": "CHECKOUT-6785", "title": "Checkout scenario 6785", "data": {"sku": "SKU6785", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6785@example.com", "threshold": 850}},
    {"id": "CHECKOUT-6786", "title": "Checkout scenario 6786", "data": {"sku": "SKU6786", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6786@example.com", "threshold": 860}},
    {"id": "CHECKOUT-6787", "title": "Checkout scenario 6787", "data": {"sku": "SKU6787", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6787@example.com", "threshold": 870}},
    {"id": "CHECKOUT-6788", "title": "Checkout scenario 6788", "data": {"sku": "SKU6788", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6788@example.com", "threshold": 880}},
    {"id": "CHECKOUT-6789", "title": "Checkout scenario 6789", "data": {"sku": "SKU6789", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6789@example.com", "threshold": 890}},
    {"id": "CHECKOUT-6790", "title": "Checkout scenario 6790", "data": {"sku": "SKU6790", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6790@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
