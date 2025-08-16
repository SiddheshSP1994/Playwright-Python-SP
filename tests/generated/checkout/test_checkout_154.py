import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-9181", "title": "Checkout scenario 9181", "data": {"sku": "SKU9181", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9181@example.com", "threshold": 810}},
    {"id": "CHECKOUT-9182", "title": "Checkout scenario 9182", "data": {"sku": "SKU9182", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9182@example.com", "threshold": 820}},
    {"id": "CHECKOUT-9183", "title": "Checkout scenario 9183", "data": {"sku": "SKU9183", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9183@example.com", "threshold": 830}},
    {"id": "CHECKOUT-9184", "title": "Checkout scenario 9184", "data": {"sku": "SKU9184", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9184@example.com", "threshold": 840}},
    {"id": "CHECKOUT-9185", "title": "Checkout scenario 9185", "data": {"sku": "SKU9185", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9185@example.com", "threshold": 850}},
    {"id": "CHECKOUT-9186", "title": "Checkout scenario 9186", "data": {"sku": "SKU9186", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9186@example.com", "threshold": 860}},
    {"id": "CHECKOUT-9187", "title": "Checkout scenario 9187", "data": {"sku": "SKU9187", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9187@example.com", "threshold": 870}},
    {"id": "CHECKOUT-9188", "title": "Checkout scenario 9188", "data": {"sku": "SKU9188", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9188@example.com", "threshold": 880}},
    {"id": "CHECKOUT-9189", "title": "Checkout scenario 9189", "data": {"sku": "SKU9189", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9189@example.com", "threshold": 890}},
    {"id": "CHECKOUT-9190", "title": "Checkout scenario 9190", "data": {"sku": "SKU9190", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9190@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
