import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0181", "title": "Checkout scenario 181", "data": {"sku": "SKU181", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user181@example.com", "threshold": 810}},
    {"id": "CHECKOUT-0182", "title": "Checkout scenario 182", "data": {"sku": "SKU182", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user182@example.com", "threshold": 820}},
    {"id": "CHECKOUT-0183", "title": "Checkout scenario 183", "data": {"sku": "SKU183", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user183@example.com", "threshold": 830}},
    {"id": "CHECKOUT-0184", "title": "Checkout scenario 184", "data": {"sku": "SKU184", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user184@example.com", "threshold": 840}},
    {"id": "CHECKOUT-0185", "title": "Checkout scenario 185", "data": {"sku": "SKU185", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user185@example.com", "threshold": 850}},
    {"id": "CHECKOUT-0186", "title": "Checkout scenario 186", "data": {"sku": "SKU186", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user186@example.com", "threshold": 860}},
    {"id": "CHECKOUT-0187", "title": "Checkout scenario 187", "data": {"sku": "SKU187", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user187@example.com", "threshold": 870}},
    {"id": "CHECKOUT-0188", "title": "Checkout scenario 188", "data": {"sku": "SKU188", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user188@example.com", "threshold": 880}},
    {"id": "CHECKOUT-0189", "title": "Checkout scenario 189", "data": {"sku": "SKU189", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user189@example.com", "threshold": 890}},
    {"id": "CHECKOUT-0190", "title": "Checkout scenario 190", "data": {"sku": "SKU190", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user190@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
