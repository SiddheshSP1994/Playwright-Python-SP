import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6301", "title": "Checkout scenario 6301", "data": {"sku": "SKU6301", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6301@example.com", "threshold": 10}},
    {"id": "CHECKOUT-6302", "title": "Checkout scenario 6302", "data": {"sku": "SKU6302", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6302@example.com", "threshold": 20}},
    {"id": "CHECKOUT-6303", "title": "Checkout scenario 6303", "data": {"sku": "SKU6303", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6303@example.com", "threshold": 30}},
    {"id": "CHECKOUT-6304", "title": "Checkout scenario 6304", "data": {"sku": "SKU6304", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6304@example.com", "threshold": 40}},
    {"id": "CHECKOUT-6305", "title": "Checkout scenario 6305", "data": {"sku": "SKU6305", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6305@example.com", "threshold": 50}},
    {"id": "CHECKOUT-6306", "title": "Checkout scenario 6306", "data": {"sku": "SKU6306", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6306@example.com", "threshold": 60}},
    {"id": "CHECKOUT-6307", "title": "Checkout scenario 6307", "data": {"sku": "SKU6307", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6307@example.com", "threshold": 70}},
    {"id": "CHECKOUT-6308", "title": "Checkout scenario 6308", "data": {"sku": "SKU6308", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6308@example.com", "threshold": 80}},
    {"id": "CHECKOUT-6309", "title": "Checkout scenario 6309", "data": {"sku": "SKU6309", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6309@example.com", "threshold": 90}},
    {"id": "CHECKOUT-6310", "title": "Checkout scenario 6310", "data": {"sku": "SKU6310", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6310@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
