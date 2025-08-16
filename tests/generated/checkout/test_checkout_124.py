import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-7381", "title": "Checkout scenario 7381", "data": {"sku": "SKU7381", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7381@example.com", "threshold": 810}},
    {"id": "CHECKOUT-7382", "title": "Checkout scenario 7382", "data": {"sku": "SKU7382", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7382@example.com", "threshold": 820}},
    {"id": "CHECKOUT-7383", "title": "Checkout scenario 7383", "data": {"sku": "SKU7383", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7383@example.com", "threshold": 830}},
    {"id": "CHECKOUT-7384", "title": "Checkout scenario 7384", "data": {"sku": "SKU7384", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7384@example.com", "threshold": 840}},
    {"id": "CHECKOUT-7385", "title": "Checkout scenario 7385", "data": {"sku": "SKU7385", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7385@example.com", "threshold": 850}},
    {"id": "CHECKOUT-7386", "title": "Checkout scenario 7386", "data": {"sku": "SKU7386", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7386@example.com", "threshold": 860}},
    {"id": "CHECKOUT-7387", "title": "Checkout scenario 7387", "data": {"sku": "SKU7387", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7387@example.com", "threshold": 870}},
    {"id": "CHECKOUT-7388", "title": "Checkout scenario 7388", "data": {"sku": "SKU7388", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7388@example.com", "threshold": 880}},
    {"id": "CHECKOUT-7389", "title": "Checkout scenario 7389", "data": {"sku": "SKU7389", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7389@example.com", "threshold": 890}},
    {"id": "CHECKOUT-7390", "title": "Checkout scenario 7390", "data": {"sku": "SKU7390", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7390@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
