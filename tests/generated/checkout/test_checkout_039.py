import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2281", "title": "Checkout scenario 2281", "data": {"sku": "SKU2281", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2281@example.com", "threshold": 810}},
    {"id": "CHECKOUT-2282", "title": "Checkout scenario 2282", "data": {"sku": "SKU2282", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2282@example.com", "threshold": 820}},
    {"id": "CHECKOUT-2283", "title": "Checkout scenario 2283", "data": {"sku": "SKU2283", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2283@example.com", "threshold": 830}},
    {"id": "CHECKOUT-2284", "title": "Checkout scenario 2284", "data": {"sku": "SKU2284", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2284@example.com", "threshold": 840}},
    {"id": "CHECKOUT-2285", "title": "Checkout scenario 2285", "data": {"sku": "SKU2285", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2285@example.com", "threshold": 850}},
    {"id": "CHECKOUT-2286", "title": "Checkout scenario 2286", "data": {"sku": "SKU2286", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2286@example.com", "threshold": 860}},
    {"id": "CHECKOUT-2287", "title": "Checkout scenario 2287", "data": {"sku": "SKU2287", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2287@example.com", "threshold": 870}},
    {"id": "CHECKOUT-2288", "title": "Checkout scenario 2288", "data": {"sku": "SKU2288", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2288@example.com", "threshold": 880}},
    {"id": "CHECKOUT-2289", "title": "Checkout scenario 2289", "data": {"sku": "SKU2289", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2289@example.com", "threshold": 890}},
    {"id": "CHECKOUT-2290", "title": "Checkout scenario 2290", "data": {"sku": "SKU2290", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2290@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
