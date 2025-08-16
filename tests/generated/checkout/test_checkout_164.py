import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-9781", "title": "Checkout scenario 9781", "data": {"sku": "SKU9781", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9781@example.com", "threshold": 810}},
    {"id": "CHECKOUT-9782", "title": "Checkout scenario 9782", "data": {"sku": "SKU9782", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9782@example.com", "threshold": 820}},
    {"id": "CHECKOUT-9783", "title": "Checkout scenario 9783", "data": {"sku": "SKU9783", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9783@example.com", "threshold": 830}},
    {"id": "CHECKOUT-9784", "title": "Checkout scenario 9784", "data": {"sku": "SKU9784", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9784@example.com", "threshold": 840}},
    {"id": "CHECKOUT-9785", "title": "Checkout scenario 9785", "data": {"sku": "SKU9785", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9785@example.com", "threshold": 850}},
    {"id": "CHECKOUT-9786", "title": "Checkout scenario 9786", "data": {"sku": "SKU9786", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9786@example.com", "threshold": 860}},
    {"id": "CHECKOUT-9787", "title": "Checkout scenario 9787", "data": {"sku": "SKU9787", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9787@example.com", "threshold": 870}},
    {"id": "CHECKOUT-9788", "title": "Checkout scenario 9788", "data": {"sku": "SKU9788", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9788@example.com", "threshold": 880}},
    {"id": "CHECKOUT-9789", "title": "Checkout scenario 9789", "data": {"sku": "SKU9789", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9789@example.com", "threshold": 890}},
    {"id": "CHECKOUT-9790", "title": "Checkout scenario 9790", "data": {"sku": "SKU9790", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9790@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
