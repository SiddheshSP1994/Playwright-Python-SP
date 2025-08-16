import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8701", "title": "Checkout scenario 8701", "data": {"sku": "SKU8701", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8701@example.com", "threshold": 10}},
    {"id": "CHECKOUT-8702", "title": "Checkout scenario 8702", "data": {"sku": "SKU8702", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8702@example.com", "threshold": 20}},
    {"id": "CHECKOUT-8703", "title": "Checkout scenario 8703", "data": {"sku": "SKU8703", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8703@example.com", "threshold": 30}},
    {"id": "CHECKOUT-8704", "title": "Checkout scenario 8704", "data": {"sku": "SKU8704", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8704@example.com", "threshold": 40}},
    {"id": "CHECKOUT-8705", "title": "Checkout scenario 8705", "data": {"sku": "SKU8705", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8705@example.com", "threshold": 50}},
    {"id": "CHECKOUT-8706", "title": "Checkout scenario 8706", "data": {"sku": "SKU8706", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8706@example.com", "threshold": 60}},
    {"id": "CHECKOUT-8707", "title": "Checkout scenario 8707", "data": {"sku": "SKU8707", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8707@example.com", "threshold": 70}},
    {"id": "CHECKOUT-8708", "title": "Checkout scenario 8708", "data": {"sku": "SKU8708", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8708@example.com", "threshold": 80}},
    {"id": "CHECKOUT-8709", "title": "Checkout scenario 8709", "data": {"sku": "SKU8709", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8709@example.com", "threshold": 90}},
    {"id": "CHECKOUT-8710", "title": "Checkout scenario 8710", "data": {"sku": "SKU8710", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8710@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
