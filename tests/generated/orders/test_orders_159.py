import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9501", "title": "Orders scenario 9501", "data": {"sku": "SKU9501", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9501@example.com", "threshold": 10}},
    {"id": "ORDERS-9502", "title": "Orders scenario 9502", "data": {"sku": "SKU9502", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9502@example.com", "threshold": 20}},
    {"id": "ORDERS-9503", "title": "Orders scenario 9503", "data": {"sku": "SKU9503", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9503@example.com", "threshold": 30}},
    {"id": "ORDERS-9504", "title": "Orders scenario 9504", "data": {"sku": "SKU9504", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9504@example.com", "threshold": 40}},
    {"id": "ORDERS-9505", "title": "Orders scenario 9505", "data": {"sku": "SKU9505", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9505@example.com", "threshold": 50}},
    {"id": "ORDERS-9506", "title": "Orders scenario 9506", "data": {"sku": "SKU9506", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9506@example.com", "threshold": 60}},
    {"id": "ORDERS-9507", "title": "Orders scenario 9507", "data": {"sku": "SKU9507", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9507@example.com", "threshold": 70}},
    {"id": "ORDERS-9508", "title": "Orders scenario 9508", "data": {"sku": "SKU9508", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9508@example.com", "threshold": 80}},
    {"id": "ORDERS-9509", "title": "Orders scenario 9509", "data": {"sku": "SKU9509", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9509@example.com", "threshold": 90}},
    {"id": "ORDERS-9510", "title": "Orders scenario 9510", "data": {"sku": "SKU9510", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9510@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
