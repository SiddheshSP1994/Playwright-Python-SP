import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9621", "title": "Orders scenario 9621", "data": {"sku": "SKU9621", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9621@example.com", "threshold": 210}},
    {"id": "ORDERS-9622", "title": "Orders scenario 9622", "data": {"sku": "SKU9622", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9622@example.com", "threshold": 220}},
    {"id": "ORDERS-9623", "title": "Orders scenario 9623", "data": {"sku": "SKU9623", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9623@example.com", "threshold": 230}},
    {"id": "ORDERS-9624", "title": "Orders scenario 9624", "data": {"sku": "SKU9624", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9624@example.com", "threshold": 240}},
    {"id": "ORDERS-9625", "title": "Orders scenario 9625", "data": {"sku": "SKU9625", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9625@example.com", "threshold": 250}},
    {"id": "ORDERS-9626", "title": "Orders scenario 9626", "data": {"sku": "SKU9626", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9626@example.com", "threshold": 260}},
    {"id": "ORDERS-9627", "title": "Orders scenario 9627", "data": {"sku": "SKU9627", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9627@example.com", "threshold": 270}},
    {"id": "ORDERS-9628", "title": "Orders scenario 9628", "data": {"sku": "SKU9628", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9628@example.com", "threshold": 280}},
    {"id": "ORDERS-9629", "title": "Orders scenario 9629", "data": {"sku": "SKU9629", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9629@example.com", "threshold": 290}},
    {"id": "ORDERS-9630", "title": "Orders scenario 9630", "data": {"sku": "SKU9630", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9630@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
