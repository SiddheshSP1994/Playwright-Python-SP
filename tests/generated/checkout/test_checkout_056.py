import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-3301", "title": "Checkout scenario 3301", "data": {"sku": "SKU3301", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3301@example.com", "threshold": 10}},
    {"id": "CHECKOUT-3302", "title": "Checkout scenario 3302", "data": {"sku": "SKU3302", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3302@example.com", "threshold": 20}},
    {"id": "CHECKOUT-3303", "title": "Checkout scenario 3303", "data": {"sku": "SKU3303", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3303@example.com", "threshold": 30}},
    {"id": "CHECKOUT-3304", "title": "Checkout scenario 3304", "data": {"sku": "SKU3304", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3304@example.com", "threshold": 40}},
    {"id": "CHECKOUT-3305", "title": "Checkout scenario 3305", "data": {"sku": "SKU3305", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3305@example.com", "threshold": 50}},
    {"id": "CHECKOUT-3306", "title": "Checkout scenario 3306", "data": {"sku": "SKU3306", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3306@example.com", "threshold": 60}},
    {"id": "CHECKOUT-3307", "title": "Checkout scenario 3307", "data": {"sku": "SKU3307", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3307@example.com", "threshold": 70}},
    {"id": "CHECKOUT-3308", "title": "Checkout scenario 3308", "data": {"sku": "SKU3308", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3308@example.com", "threshold": 80}},
    {"id": "CHECKOUT-3309", "title": "Checkout scenario 3309", "data": {"sku": "SKU3309", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3309@example.com", "threshold": 90}},
    {"id": "CHECKOUT-3310", "title": "Checkout scenario 3310", "data": {"sku": "SKU3310", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3310@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
