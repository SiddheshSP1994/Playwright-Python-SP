import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1281", "title": "Orders scenario 1281", "data": {"sku": "SKU1281", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1281@example.com", "threshold": 810}},
    {"id": "ORDERS-1282", "title": "Orders scenario 1282", "data": {"sku": "SKU1282", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1282@example.com", "threshold": 820}},
    {"id": "ORDERS-1283", "title": "Orders scenario 1283", "data": {"sku": "SKU1283", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1283@example.com", "threshold": 830}},
    {"id": "ORDERS-1284", "title": "Orders scenario 1284", "data": {"sku": "SKU1284", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1284@example.com", "threshold": 840}},
    {"id": "ORDERS-1285", "title": "Orders scenario 1285", "data": {"sku": "SKU1285", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1285@example.com", "threshold": 850}},
    {"id": "ORDERS-1286", "title": "Orders scenario 1286", "data": {"sku": "SKU1286", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1286@example.com", "threshold": 860}},
    {"id": "ORDERS-1287", "title": "Orders scenario 1287", "data": {"sku": "SKU1287", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1287@example.com", "threshold": 870}},
    {"id": "ORDERS-1288", "title": "Orders scenario 1288", "data": {"sku": "SKU1288", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1288@example.com", "threshold": 880}},
    {"id": "ORDERS-1289", "title": "Orders scenario 1289", "data": {"sku": "SKU1289", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1289@example.com", "threshold": 890}},
    {"id": "ORDERS-1290", "title": "Orders scenario 1290", "data": {"sku": "SKU1290", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1290@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
