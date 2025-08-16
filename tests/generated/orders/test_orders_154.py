import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9201", "title": "Orders scenario 9201", "data": {"sku": "SKU9201", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9201@example.com", "threshold": 10}},
    {"id": "ORDERS-9202", "title": "Orders scenario 9202", "data": {"sku": "SKU9202", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9202@example.com", "threshold": 20}},
    {"id": "ORDERS-9203", "title": "Orders scenario 9203", "data": {"sku": "SKU9203", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9203@example.com", "threshold": 30}},
    {"id": "ORDERS-9204", "title": "Orders scenario 9204", "data": {"sku": "SKU9204", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9204@example.com", "threshold": 40}},
    {"id": "ORDERS-9205", "title": "Orders scenario 9205", "data": {"sku": "SKU9205", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9205@example.com", "threshold": 50}},
    {"id": "ORDERS-9206", "title": "Orders scenario 9206", "data": {"sku": "SKU9206", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9206@example.com", "threshold": 60}},
    {"id": "ORDERS-9207", "title": "Orders scenario 9207", "data": {"sku": "SKU9207", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9207@example.com", "threshold": 70}},
    {"id": "ORDERS-9208", "title": "Orders scenario 9208", "data": {"sku": "SKU9208", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9208@example.com", "threshold": 80}},
    {"id": "ORDERS-9209", "title": "Orders scenario 9209", "data": {"sku": "SKU9209", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9209@example.com", "threshold": 90}},
    {"id": "ORDERS-9210", "title": "Orders scenario 9210", "data": {"sku": "SKU9210", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9210@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
