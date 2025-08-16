import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-9361", "title": "Checkout scenario 9361", "data": {"sku": "SKU9361", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9361@example.com", "threshold": 610}},
    {"id": "CHECKOUT-9362", "title": "Checkout scenario 9362", "data": {"sku": "SKU9362", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9362@example.com", "threshold": 620}},
    {"id": "CHECKOUT-9363", "title": "Checkout scenario 9363", "data": {"sku": "SKU9363", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9363@example.com", "threshold": 630}},
    {"id": "CHECKOUT-9364", "title": "Checkout scenario 9364", "data": {"sku": "SKU9364", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9364@example.com", "threshold": 640}},
    {"id": "CHECKOUT-9365", "title": "Checkout scenario 9365", "data": {"sku": "SKU9365", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9365@example.com", "threshold": 650}},
    {"id": "CHECKOUT-9366", "title": "Checkout scenario 9366", "data": {"sku": "SKU9366", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9366@example.com", "threshold": 660}},
    {"id": "CHECKOUT-9367", "title": "Checkout scenario 9367", "data": {"sku": "SKU9367", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9367@example.com", "threshold": 670}},
    {"id": "CHECKOUT-9368", "title": "Checkout scenario 9368", "data": {"sku": "SKU9368", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9368@example.com", "threshold": 680}},
    {"id": "CHECKOUT-9369", "title": "Checkout scenario 9369", "data": {"sku": "SKU9369", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9369@example.com", "threshold": 690}},
    {"id": "CHECKOUT-9370", "title": "Checkout scenario 9370", "data": {"sku": "SKU9370", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9370@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
