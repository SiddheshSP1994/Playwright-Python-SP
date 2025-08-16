import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6001", "title": "Checkout scenario 6001", "data": {"sku": "SKU6001", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6001@example.com", "threshold": 10}},
    {"id": "CHECKOUT-6002", "title": "Checkout scenario 6002", "data": {"sku": "SKU6002", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6002@example.com", "threshold": 20}},
    {"id": "CHECKOUT-6003", "title": "Checkout scenario 6003", "data": {"sku": "SKU6003", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6003@example.com", "threshold": 30}},
    {"id": "CHECKOUT-6004", "title": "Checkout scenario 6004", "data": {"sku": "SKU6004", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6004@example.com", "threshold": 40}},
    {"id": "CHECKOUT-6005", "title": "Checkout scenario 6005", "data": {"sku": "SKU6005", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6005@example.com", "threshold": 50}},
    {"id": "CHECKOUT-6006", "title": "Checkout scenario 6006", "data": {"sku": "SKU6006", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6006@example.com", "threshold": 60}},
    {"id": "CHECKOUT-6007", "title": "Checkout scenario 6007", "data": {"sku": "SKU6007", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6007@example.com", "threshold": 70}},
    {"id": "CHECKOUT-6008", "title": "Checkout scenario 6008", "data": {"sku": "SKU6008", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6008@example.com", "threshold": 80}},
    {"id": "CHECKOUT-6009", "title": "Checkout scenario 6009", "data": {"sku": "SKU6009", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6009@example.com", "threshold": 90}},
    {"id": "CHECKOUT-6010", "title": "Checkout scenario 6010", "data": {"sku": "SKU6010", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6010@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
