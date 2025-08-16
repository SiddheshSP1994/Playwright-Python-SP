import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2881", "title": "Checkout scenario 2881", "data": {"sku": "SKU2881", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2881@example.com", "threshold": 810}},
    {"id": "CHECKOUT-2882", "title": "Checkout scenario 2882", "data": {"sku": "SKU2882", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2882@example.com", "threshold": 820}},
    {"id": "CHECKOUT-2883", "title": "Checkout scenario 2883", "data": {"sku": "SKU2883", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2883@example.com", "threshold": 830}},
    {"id": "CHECKOUT-2884", "title": "Checkout scenario 2884", "data": {"sku": "SKU2884", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2884@example.com", "threshold": 840}},
    {"id": "CHECKOUT-2885", "title": "Checkout scenario 2885", "data": {"sku": "SKU2885", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2885@example.com", "threshold": 850}},
    {"id": "CHECKOUT-2886", "title": "Checkout scenario 2886", "data": {"sku": "SKU2886", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2886@example.com", "threshold": 860}},
    {"id": "CHECKOUT-2887", "title": "Checkout scenario 2887", "data": {"sku": "SKU2887", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2887@example.com", "threshold": 870}},
    {"id": "CHECKOUT-2888", "title": "Checkout scenario 2888", "data": {"sku": "SKU2888", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2888@example.com", "threshold": 880}},
    {"id": "CHECKOUT-2889", "title": "Checkout scenario 2889", "data": {"sku": "SKU2889", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2889@example.com", "threshold": 890}},
    {"id": "CHECKOUT-2890", "title": "Checkout scenario 2890", "data": {"sku": "SKU2890", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2890@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
