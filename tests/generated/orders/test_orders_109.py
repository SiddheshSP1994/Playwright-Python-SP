import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6501", "title": "Orders scenario 6501", "data": {"sku": "SKU6501", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6501@example.com", "threshold": 10}},
    {"id": "ORDERS-6502", "title": "Orders scenario 6502", "data": {"sku": "SKU6502", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6502@example.com", "threshold": 20}},
    {"id": "ORDERS-6503", "title": "Orders scenario 6503", "data": {"sku": "SKU6503", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6503@example.com", "threshold": 30}},
    {"id": "ORDERS-6504", "title": "Orders scenario 6504", "data": {"sku": "SKU6504", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6504@example.com", "threshold": 40}},
    {"id": "ORDERS-6505", "title": "Orders scenario 6505", "data": {"sku": "SKU6505", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6505@example.com", "threshold": 50}},
    {"id": "ORDERS-6506", "title": "Orders scenario 6506", "data": {"sku": "SKU6506", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6506@example.com", "threshold": 60}},
    {"id": "ORDERS-6507", "title": "Orders scenario 6507", "data": {"sku": "SKU6507", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6507@example.com", "threshold": 70}},
    {"id": "ORDERS-6508", "title": "Orders scenario 6508", "data": {"sku": "SKU6508", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6508@example.com", "threshold": 80}},
    {"id": "ORDERS-6509", "title": "Orders scenario 6509", "data": {"sku": "SKU6509", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6509@example.com", "threshold": 90}},
    {"id": "ORDERS-6510", "title": "Orders scenario 6510", "data": {"sku": "SKU6510", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6510@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
