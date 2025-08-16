import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6361", "title": "Checkout scenario 6361", "data": {"sku": "SKU6361", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6361@example.com", "threshold": 610}},
    {"id": "CHECKOUT-6362", "title": "Checkout scenario 6362", "data": {"sku": "SKU6362", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6362@example.com", "threshold": 620}},
    {"id": "CHECKOUT-6363", "title": "Checkout scenario 6363", "data": {"sku": "SKU6363", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6363@example.com", "threshold": 630}},
    {"id": "CHECKOUT-6364", "title": "Checkout scenario 6364", "data": {"sku": "SKU6364", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6364@example.com", "threshold": 640}},
    {"id": "CHECKOUT-6365", "title": "Checkout scenario 6365", "data": {"sku": "SKU6365", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6365@example.com", "threshold": 650}},
    {"id": "CHECKOUT-6366", "title": "Checkout scenario 6366", "data": {"sku": "SKU6366", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6366@example.com", "threshold": 660}},
    {"id": "CHECKOUT-6367", "title": "Checkout scenario 6367", "data": {"sku": "SKU6367", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6367@example.com", "threshold": 670}},
    {"id": "CHECKOUT-6368", "title": "Checkout scenario 6368", "data": {"sku": "SKU6368", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6368@example.com", "threshold": 680}},
    {"id": "CHECKOUT-6369", "title": "Checkout scenario 6369", "data": {"sku": "SKU6369", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6369@example.com", "threshold": 690}},
    {"id": "CHECKOUT-6370", "title": "Checkout scenario 6370", "data": {"sku": "SKU6370", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6370@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
