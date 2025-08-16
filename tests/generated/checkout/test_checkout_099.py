import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5881", "title": "Checkout scenario 5881", "data": {"sku": "SKU5881", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5881@example.com", "threshold": 810}},
    {"id": "CHECKOUT-5882", "title": "Checkout scenario 5882", "data": {"sku": "SKU5882", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5882@example.com", "threshold": 820}},
    {"id": "CHECKOUT-5883", "title": "Checkout scenario 5883", "data": {"sku": "SKU5883", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5883@example.com", "threshold": 830}},
    {"id": "CHECKOUT-5884", "title": "Checkout scenario 5884", "data": {"sku": "SKU5884", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5884@example.com", "threshold": 840}},
    {"id": "CHECKOUT-5885", "title": "Checkout scenario 5885", "data": {"sku": "SKU5885", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5885@example.com", "threshold": 850}},
    {"id": "CHECKOUT-5886", "title": "Checkout scenario 5886", "data": {"sku": "SKU5886", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5886@example.com", "threshold": 860}},
    {"id": "CHECKOUT-5887", "title": "Checkout scenario 5887", "data": {"sku": "SKU5887", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5887@example.com", "threshold": 870}},
    {"id": "CHECKOUT-5888", "title": "Checkout scenario 5888", "data": {"sku": "SKU5888", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5888@example.com", "threshold": 880}},
    {"id": "CHECKOUT-5889", "title": "Checkout scenario 5889", "data": {"sku": "SKU5889", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5889@example.com", "threshold": 890}},
    {"id": "CHECKOUT-5890", "title": "Checkout scenario 5890", "data": {"sku": "SKU5890", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5890@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
