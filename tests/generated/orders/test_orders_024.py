import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1401", "title": "Orders scenario 1401", "data": {"sku": "SKU1401", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1401@example.com", "threshold": 10}},
    {"id": "ORDERS-1402", "title": "Orders scenario 1402", "data": {"sku": "SKU1402", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1402@example.com", "threshold": 20}},
    {"id": "ORDERS-1403", "title": "Orders scenario 1403", "data": {"sku": "SKU1403", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1403@example.com", "threshold": 30}},
    {"id": "ORDERS-1404", "title": "Orders scenario 1404", "data": {"sku": "SKU1404", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1404@example.com", "threshold": 40}},
    {"id": "ORDERS-1405", "title": "Orders scenario 1405", "data": {"sku": "SKU1405", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1405@example.com", "threshold": 50}},
    {"id": "ORDERS-1406", "title": "Orders scenario 1406", "data": {"sku": "SKU1406", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1406@example.com", "threshold": 60}},
    {"id": "ORDERS-1407", "title": "Orders scenario 1407", "data": {"sku": "SKU1407", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1407@example.com", "threshold": 70}},
    {"id": "ORDERS-1408", "title": "Orders scenario 1408", "data": {"sku": "SKU1408", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1408@example.com", "threshold": 80}},
    {"id": "ORDERS-1409", "title": "Orders scenario 1409", "data": {"sku": "SKU1409", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1409@example.com", "threshold": 90}},
    {"id": "ORDERS-1410", "title": "Orders scenario 1410", "data": {"sku": "SKU1410", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1410@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
