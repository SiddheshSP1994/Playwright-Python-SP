import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0001", "title": "Checkout scenario 1", "data": {"sku": "SKU1", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1@example.com", "threshold": 10}},
    {"id": "CHECKOUT-0002", "title": "Checkout scenario 2", "data": {"sku": "SKU2", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2@example.com", "threshold": 20}},
    {"id": "CHECKOUT-0003", "title": "Checkout scenario 3", "data": {"sku": "SKU3", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3@example.com", "threshold": 30}},
    {"id": "CHECKOUT-0004", "title": "Checkout scenario 4", "data": {"sku": "SKU4", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4@example.com", "threshold": 40}},
    {"id": "CHECKOUT-0005", "title": "Checkout scenario 5", "data": {"sku": "SKU5", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5@example.com", "threshold": 50}},
    {"id": "CHECKOUT-0006", "title": "Checkout scenario 6", "data": {"sku": "SKU6", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6@example.com", "threshold": 60}},
    {"id": "CHECKOUT-0007", "title": "Checkout scenario 7", "data": {"sku": "SKU7", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7@example.com", "threshold": 70}},
    {"id": "CHECKOUT-0008", "title": "Checkout scenario 8", "data": {"sku": "SKU8", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8@example.com", "threshold": 80}},
    {"id": "CHECKOUT-0009", "title": "Checkout scenario 9", "data": {"sku": "SKU9", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9@example.com", "threshold": 90}},
    {"id": "CHECKOUT-0010", "title": "Checkout scenario 10", "data": {"sku": "SKU10", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user10@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
