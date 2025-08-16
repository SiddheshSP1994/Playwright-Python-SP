import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0781", "title": "Checkout scenario 781", "data": {"sku": "SKU781", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user781@example.com", "threshold": 810}},
    {"id": "CHECKOUT-0782", "title": "Checkout scenario 782", "data": {"sku": "SKU782", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user782@example.com", "threshold": 820}},
    {"id": "CHECKOUT-0783", "title": "Checkout scenario 783", "data": {"sku": "SKU783", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user783@example.com", "threshold": 830}},
    {"id": "CHECKOUT-0784", "title": "Checkout scenario 784", "data": {"sku": "SKU784", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user784@example.com", "threshold": 840}},
    {"id": "CHECKOUT-0785", "title": "Checkout scenario 785", "data": {"sku": "SKU785", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user785@example.com", "threshold": 850}},
    {"id": "CHECKOUT-0786", "title": "Checkout scenario 786", "data": {"sku": "SKU786", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user786@example.com", "threshold": 860}},
    {"id": "CHECKOUT-0787", "title": "Checkout scenario 787", "data": {"sku": "SKU787", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user787@example.com", "threshold": 870}},
    {"id": "CHECKOUT-0788", "title": "Checkout scenario 788", "data": {"sku": "SKU788", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user788@example.com", "threshold": 880}},
    {"id": "CHECKOUT-0789", "title": "Checkout scenario 789", "data": {"sku": "SKU789", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user789@example.com", "threshold": 890}},
    {"id": "CHECKOUT-0790", "title": "Checkout scenario 790", "data": {"sku": "SKU790", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user790@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
