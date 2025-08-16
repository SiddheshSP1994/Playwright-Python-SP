import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8881", "title": "Checkout scenario 8881", "data": {"sku": "SKU8881", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8881@example.com", "threshold": 810}},
    {"id": "CHECKOUT-8882", "title": "Checkout scenario 8882", "data": {"sku": "SKU8882", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8882@example.com", "threshold": 820}},
    {"id": "CHECKOUT-8883", "title": "Checkout scenario 8883", "data": {"sku": "SKU8883", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8883@example.com", "threshold": 830}},
    {"id": "CHECKOUT-8884", "title": "Checkout scenario 8884", "data": {"sku": "SKU8884", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8884@example.com", "threshold": 840}},
    {"id": "CHECKOUT-8885", "title": "Checkout scenario 8885", "data": {"sku": "SKU8885", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8885@example.com", "threshold": 850}},
    {"id": "CHECKOUT-8886", "title": "Checkout scenario 8886", "data": {"sku": "SKU8886", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8886@example.com", "threshold": 860}},
    {"id": "CHECKOUT-8887", "title": "Checkout scenario 8887", "data": {"sku": "SKU8887", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8887@example.com", "threshold": 870}},
    {"id": "CHECKOUT-8888", "title": "Checkout scenario 8888", "data": {"sku": "SKU8888", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8888@example.com", "threshold": 880}},
    {"id": "CHECKOUT-8889", "title": "Checkout scenario 8889", "data": {"sku": "SKU8889", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8889@example.com", "threshold": 890}},
    {"id": "CHECKOUT-8890", "title": "Checkout scenario 8890", "data": {"sku": "SKU8890", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8890@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
