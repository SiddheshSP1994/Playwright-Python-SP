import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1221", "title": "Orders scenario 1221", "data": {"sku": "SKU1221", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1221@example.com", "threshold": 210}},
    {"id": "ORDERS-1222", "title": "Orders scenario 1222", "data": {"sku": "SKU1222", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1222@example.com", "threshold": 220}},
    {"id": "ORDERS-1223", "title": "Orders scenario 1223", "data": {"sku": "SKU1223", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1223@example.com", "threshold": 230}},
    {"id": "ORDERS-1224", "title": "Orders scenario 1224", "data": {"sku": "SKU1224", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1224@example.com", "threshold": 240}},
    {"id": "ORDERS-1225", "title": "Orders scenario 1225", "data": {"sku": "SKU1225", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1225@example.com", "threshold": 250}},
    {"id": "ORDERS-1226", "title": "Orders scenario 1226", "data": {"sku": "SKU1226", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1226@example.com", "threshold": 260}},
    {"id": "ORDERS-1227", "title": "Orders scenario 1227", "data": {"sku": "SKU1227", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1227@example.com", "threshold": 270}},
    {"id": "ORDERS-1228", "title": "Orders scenario 1228", "data": {"sku": "SKU1228", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1228@example.com", "threshold": 280}},
    {"id": "ORDERS-1229", "title": "Orders scenario 1229", "data": {"sku": "SKU1229", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1229@example.com", "threshold": 290}},
    {"id": "ORDERS-1230", "title": "Orders scenario 1230", "data": {"sku": "SKU1230", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1230@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
