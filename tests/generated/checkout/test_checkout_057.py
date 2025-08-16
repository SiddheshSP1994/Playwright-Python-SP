import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-3361", "title": "Checkout scenario 3361", "data": {"sku": "SKU3361", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3361@example.com", "threshold": 610}},
    {"id": "CHECKOUT-3362", "title": "Checkout scenario 3362", "data": {"sku": "SKU3362", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3362@example.com", "threshold": 620}},
    {"id": "CHECKOUT-3363", "title": "Checkout scenario 3363", "data": {"sku": "SKU3363", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3363@example.com", "threshold": 630}},
    {"id": "CHECKOUT-3364", "title": "Checkout scenario 3364", "data": {"sku": "SKU3364", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3364@example.com", "threshold": 640}},
    {"id": "CHECKOUT-3365", "title": "Checkout scenario 3365", "data": {"sku": "SKU3365", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3365@example.com", "threshold": 650}},
    {"id": "CHECKOUT-3366", "title": "Checkout scenario 3366", "data": {"sku": "SKU3366", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3366@example.com", "threshold": 660}},
    {"id": "CHECKOUT-3367", "title": "Checkout scenario 3367", "data": {"sku": "SKU3367", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3367@example.com", "threshold": 670}},
    {"id": "CHECKOUT-3368", "title": "Checkout scenario 3368", "data": {"sku": "SKU3368", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3368@example.com", "threshold": 680}},
    {"id": "CHECKOUT-3369", "title": "Checkout scenario 3369", "data": {"sku": "SKU3369", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3369@example.com", "threshold": 690}},
    {"id": "CHECKOUT-3370", "title": "Checkout scenario 3370", "data": {"sku": "SKU3370", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3370@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
