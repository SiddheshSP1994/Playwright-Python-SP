import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1461", "title": "Orders scenario 1461", "data": {"sku": "SKU1461", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1461@example.com", "threshold": 610}},
    {"id": "ORDERS-1462", "title": "Orders scenario 1462", "data": {"sku": "SKU1462", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1462@example.com", "threshold": 620}},
    {"id": "ORDERS-1463", "title": "Orders scenario 1463", "data": {"sku": "SKU1463", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1463@example.com", "threshold": 630}},
    {"id": "ORDERS-1464", "title": "Orders scenario 1464", "data": {"sku": "SKU1464", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1464@example.com", "threshold": 640}},
    {"id": "ORDERS-1465", "title": "Orders scenario 1465", "data": {"sku": "SKU1465", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1465@example.com", "threshold": 650}},
    {"id": "ORDERS-1466", "title": "Orders scenario 1466", "data": {"sku": "SKU1466", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1466@example.com", "threshold": 660}},
    {"id": "ORDERS-1467", "title": "Orders scenario 1467", "data": {"sku": "SKU1467", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1467@example.com", "threshold": 670}},
    {"id": "ORDERS-1468", "title": "Orders scenario 1468", "data": {"sku": "SKU1468", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1468@example.com", "threshold": 680}},
    {"id": "ORDERS-1469", "title": "Orders scenario 1469", "data": {"sku": "SKU1469", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1469@example.com", "threshold": 690}},
    {"id": "ORDERS-1470", "title": "Orders scenario 1470", "data": {"sku": "SKU1470", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1470@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
