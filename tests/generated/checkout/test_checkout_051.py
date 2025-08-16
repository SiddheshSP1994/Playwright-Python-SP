import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-3001", "title": "Checkout scenario 3001", "data": {"sku": "SKU3001", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3001@example.com", "threshold": 10}},
    {"id": "CHECKOUT-3002", "title": "Checkout scenario 3002", "data": {"sku": "SKU3002", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3002@example.com", "threshold": 20}},
    {"id": "CHECKOUT-3003", "title": "Checkout scenario 3003", "data": {"sku": "SKU3003", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3003@example.com", "threshold": 30}},
    {"id": "CHECKOUT-3004", "title": "Checkout scenario 3004", "data": {"sku": "SKU3004", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3004@example.com", "threshold": 40}},
    {"id": "CHECKOUT-3005", "title": "Checkout scenario 3005", "data": {"sku": "SKU3005", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3005@example.com", "threshold": 50}},
    {"id": "CHECKOUT-3006", "title": "Checkout scenario 3006", "data": {"sku": "SKU3006", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3006@example.com", "threshold": 60}},
    {"id": "CHECKOUT-3007", "title": "Checkout scenario 3007", "data": {"sku": "SKU3007", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3007@example.com", "threshold": 70}},
    {"id": "CHECKOUT-3008", "title": "Checkout scenario 3008", "data": {"sku": "SKU3008", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3008@example.com", "threshold": 80}},
    {"id": "CHECKOUT-3009", "title": "Checkout scenario 3009", "data": {"sku": "SKU3009", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3009@example.com", "threshold": 90}},
    {"id": "CHECKOUT-3010", "title": "Checkout scenario 3010", "data": {"sku": "SKU3010", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3010@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
