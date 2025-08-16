import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6201", "title": "Orders scenario 6201", "data": {"sku": "SKU6201", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6201@example.com", "threshold": 10}},
    {"id": "ORDERS-6202", "title": "Orders scenario 6202", "data": {"sku": "SKU6202", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6202@example.com", "threshold": 20}},
    {"id": "ORDERS-6203", "title": "Orders scenario 6203", "data": {"sku": "SKU6203", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6203@example.com", "threshold": 30}},
    {"id": "ORDERS-6204", "title": "Orders scenario 6204", "data": {"sku": "SKU6204", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6204@example.com", "threshold": 40}},
    {"id": "ORDERS-6205", "title": "Orders scenario 6205", "data": {"sku": "SKU6205", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6205@example.com", "threshold": 50}},
    {"id": "ORDERS-6206", "title": "Orders scenario 6206", "data": {"sku": "SKU6206", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6206@example.com", "threshold": 60}},
    {"id": "ORDERS-6207", "title": "Orders scenario 6207", "data": {"sku": "SKU6207", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6207@example.com", "threshold": 70}},
    {"id": "ORDERS-6208", "title": "Orders scenario 6208", "data": {"sku": "SKU6208", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6208@example.com", "threshold": 80}},
    {"id": "ORDERS-6209", "title": "Orders scenario 6209", "data": {"sku": "SKU6209", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6209@example.com", "threshold": 90}},
    {"id": "ORDERS-6210", "title": "Orders scenario 6210", "data": {"sku": "SKU6210", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6210@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
