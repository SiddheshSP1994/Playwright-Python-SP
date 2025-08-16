import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0361", "title": "Checkout scenario 361", "data": {"sku": "SKU361", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user361@example.com", "threshold": 610}},
    {"id": "CHECKOUT-0362", "title": "Checkout scenario 362", "data": {"sku": "SKU362", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user362@example.com", "threshold": 620}},
    {"id": "CHECKOUT-0363", "title": "Checkout scenario 363", "data": {"sku": "SKU363", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user363@example.com", "threshold": 630}},
    {"id": "CHECKOUT-0364", "title": "Checkout scenario 364", "data": {"sku": "SKU364", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user364@example.com", "threshold": 640}},
    {"id": "CHECKOUT-0365", "title": "Checkout scenario 365", "data": {"sku": "SKU365", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user365@example.com", "threshold": 650}},
    {"id": "CHECKOUT-0366", "title": "Checkout scenario 366", "data": {"sku": "SKU366", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user366@example.com", "threshold": 660}},
    {"id": "CHECKOUT-0367", "title": "Checkout scenario 367", "data": {"sku": "SKU367", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user367@example.com", "threshold": 670}},
    {"id": "CHECKOUT-0368", "title": "Checkout scenario 368", "data": {"sku": "SKU368", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user368@example.com", "threshold": 680}},
    {"id": "CHECKOUT-0369", "title": "Checkout scenario 369", "data": {"sku": "SKU369", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user369@example.com", "threshold": 690}},
    {"id": "CHECKOUT-0370", "title": "Checkout scenario 370", "data": {"sku": "SKU370", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user370@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
