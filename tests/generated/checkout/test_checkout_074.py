import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4381", "title": "Checkout scenario 4381", "data": {"sku": "SKU4381", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4381@example.com", "threshold": 810}},
    {"id": "CHECKOUT-4382", "title": "Checkout scenario 4382", "data": {"sku": "SKU4382", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4382@example.com", "threshold": 820}},
    {"id": "CHECKOUT-4383", "title": "Checkout scenario 4383", "data": {"sku": "SKU4383", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4383@example.com", "threshold": 830}},
    {"id": "CHECKOUT-4384", "title": "Checkout scenario 4384", "data": {"sku": "SKU4384", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4384@example.com", "threshold": 840}},
    {"id": "CHECKOUT-4385", "title": "Checkout scenario 4385", "data": {"sku": "SKU4385", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4385@example.com", "threshold": 850}},
    {"id": "CHECKOUT-4386", "title": "Checkout scenario 4386", "data": {"sku": "SKU4386", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4386@example.com", "threshold": 860}},
    {"id": "CHECKOUT-4387", "title": "Checkout scenario 4387", "data": {"sku": "SKU4387", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4387@example.com", "threshold": 870}},
    {"id": "CHECKOUT-4388", "title": "Checkout scenario 4388", "data": {"sku": "SKU4388", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4388@example.com", "threshold": 880}},
    {"id": "CHECKOUT-4389", "title": "Checkout scenario 4389", "data": {"sku": "SKU4389", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4389@example.com", "threshold": 890}},
    {"id": "CHECKOUT-4390", "title": "Checkout scenario 4390", "data": {"sku": "SKU4390", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4390@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
