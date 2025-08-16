import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-3181", "title": "Checkout scenario 3181", "data": {"sku": "SKU3181", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3181@example.com", "threshold": 810}},
    {"id": "CHECKOUT-3182", "title": "Checkout scenario 3182", "data": {"sku": "SKU3182", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3182@example.com", "threshold": 820}},
    {"id": "CHECKOUT-3183", "title": "Checkout scenario 3183", "data": {"sku": "SKU3183", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3183@example.com", "threshold": 830}},
    {"id": "CHECKOUT-3184", "title": "Checkout scenario 3184", "data": {"sku": "SKU3184", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3184@example.com", "threshold": 840}},
    {"id": "CHECKOUT-3185", "title": "Checkout scenario 3185", "data": {"sku": "SKU3185", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3185@example.com", "threshold": 850}},
    {"id": "CHECKOUT-3186", "title": "Checkout scenario 3186", "data": {"sku": "SKU3186", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3186@example.com", "threshold": 860}},
    {"id": "CHECKOUT-3187", "title": "Checkout scenario 3187", "data": {"sku": "SKU3187", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3187@example.com", "threshold": 870}},
    {"id": "CHECKOUT-3188", "title": "Checkout scenario 3188", "data": {"sku": "SKU3188", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3188@example.com", "threshold": 880}},
    {"id": "CHECKOUT-3189", "title": "Checkout scenario 3189", "data": {"sku": "SKU3189", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3189@example.com", "threshold": 890}},
    {"id": "CHECKOUT-3190", "title": "Checkout scenario 3190", "data": {"sku": "SKU3190", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3190@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
