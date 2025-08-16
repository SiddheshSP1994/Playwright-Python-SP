import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6621", "title": "Orders scenario 6621", "data": {"sku": "SKU6621", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6621@example.com", "threshold": 210}},
    {"id": "ORDERS-6622", "title": "Orders scenario 6622", "data": {"sku": "SKU6622", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6622@example.com", "threshold": 220}},
    {"id": "ORDERS-6623", "title": "Orders scenario 6623", "data": {"sku": "SKU6623", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6623@example.com", "threshold": 230}},
    {"id": "ORDERS-6624", "title": "Orders scenario 6624", "data": {"sku": "SKU6624", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6624@example.com", "threshold": 240}},
    {"id": "ORDERS-6625", "title": "Orders scenario 6625", "data": {"sku": "SKU6625", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6625@example.com", "threshold": 250}},
    {"id": "ORDERS-6626", "title": "Orders scenario 6626", "data": {"sku": "SKU6626", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6626@example.com", "threshold": 260}},
    {"id": "ORDERS-6627", "title": "Orders scenario 6627", "data": {"sku": "SKU6627", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6627@example.com", "threshold": 270}},
    {"id": "ORDERS-6628", "title": "Orders scenario 6628", "data": {"sku": "SKU6628", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6628@example.com", "threshold": 280}},
    {"id": "ORDERS-6629", "title": "Orders scenario 6629", "data": {"sku": "SKU6629", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6629@example.com", "threshold": 290}},
    {"id": "ORDERS-6630", "title": "Orders scenario 6630", "data": {"sku": "SKU6630", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6630@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
