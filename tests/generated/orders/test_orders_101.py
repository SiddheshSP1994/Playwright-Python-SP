import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6021", "title": "Orders scenario 6021", "data": {"sku": "SKU6021", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6021@example.com", "threshold": 210}},
    {"id": "ORDERS-6022", "title": "Orders scenario 6022", "data": {"sku": "SKU6022", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6022@example.com", "threshold": 220}},
    {"id": "ORDERS-6023", "title": "Orders scenario 6023", "data": {"sku": "SKU6023", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6023@example.com", "threshold": 230}},
    {"id": "ORDERS-6024", "title": "Orders scenario 6024", "data": {"sku": "SKU6024", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6024@example.com", "threshold": 240}},
    {"id": "ORDERS-6025", "title": "Orders scenario 6025", "data": {"sku": "SKU6025", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6025@example.com", "threshold": 250}},
    {"id": "ORDERS-6026", "title": "Orders scenario 6026", "data": {"sku": "SKU6026", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6026@example.com", "threshold": 260}},
    {"id": "ORDERS-6027", "title": "Orders scenario 6027", "data": {"sku": "SKU6027", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6027@example.com", "threshold": 270}},
    {"id": "ORDERS-6028", "title": "Orders scenario 6028", "data": {"sku": "SKU6028", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6028@example.com", "threshold": 280}},
    {"id": "ORDERS-6029", "title": "Orders scenario 6029", "data": {"sku": "SKU6029", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6029@example.com", "threshold": 290}},
    {"id": "ORDERS-6030", "title": "Orders scenario 6030", "data": {"sku": "SKU6030", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6030@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
