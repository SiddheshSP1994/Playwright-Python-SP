import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6181", "title": "Checkout scenario 6181", "data": {"sku": "SKU6181", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6181@example.com", "threshold": 810}},
    {"id": "CHECKOUT-6182", "title": "Checkout scenario 6182", "data": {"sku": "SKU6182", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6182@example.com", "threshold": 820}},
    {"id": "CHECKOUT-6183", "title": "Checkout scenario 6183", "data": {"sku": "SKU6183", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6183@example.com", "threshold": 830}},
    {"id": "CHECKOUT-6184", "title": "Checkout scenario 6184", "data": {"sku": "SKU6184", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6184@example.com", "threshold": 840}},
    {"id": "CHECKOUT-6185", "title": "Checkout scenario 6185", "data": {"sku": "SKU6185", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6185@example.com", "threshold": 850}},
    {"id": "CHECKOUT-6186", "title": "Checkout scenario 6186", "data": {"sku": "SKU6186", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6186@example.com", "threshold": 860}},
    {"id": "CHECKOUT-6187", "title": "Checkout scenario 6187", "data": {"sku": "SKU6187", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6187@example.com", "threshold": 870}},
    {"id": "CHECKOUT-6188", "title": "Checkout scenario 6188", "data": {"sku": "SKU6188", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6188@example.com", "threshold": 880}},
    {"id": "CHECKOUT-6189", "title": "Checkout scenario 6189", "data": {"sku": "SKU6189", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6189@example.com", "threshold": 890}},
    {"id": "CHECKOUT-6190", "title": "Checkout scenario 6190", "data": {"sku": "SKU6190", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6190@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
