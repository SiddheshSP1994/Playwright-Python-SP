import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9021", "title": "Orders scenario 9021", "data": {"sku": "SKU9021", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9021@example.com", "threshold": 210}},
    {"id": "ORDERS-9022", "title": "Orders scenario 9022", "data": {"sku": "SKU9022", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9022@example.com", "threshold": 220}},
    {"id": "ORDERS-9023", "title": "Orders scenario 9023", "data": {"sku": "SKU9023", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9023@example.com", "threshold": 230}},
    {"id": "ORDERS-9024", "title": "Orders scenario 9024", "data": {"sku": "SKU9024", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9024@example.com", "threshold": 240}},
    {"id": "ORDERS-9025", "title": "Orders scenario 9025", "data": {"sku": "SKU9025", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9025@example.com", "threshold": 250}},
    {"id": "ORDERS-9026", "title": "Orders scenario 9026", "data": {"sku": "SKU9026", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9026@example.com", "threshold": 260}},
    {"id": "ORDERS-9027", "title": "Orders scenario 9027", "data": {"sku": "SKU9027", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9027@example.com", "threshold": 270}},
    {"id": "ORDERS-9028", "title": "Orders scenario 9028", "data": {"sku": "SKU9028", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9028@example.com", "threshold": 280}},
    {"id": "ORDERS-9029", "title": "Orders scenario 9029", "data": {"sku": "SKU9029", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9029@example.com", "threshold": 290}},
    {"id": "ORDERS-9030", "title": "Orders scenario 9030", "data": {"sku": "SKU9030", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9030@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
