import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1701", "title": "Orders scenario 1701", "data": {"sku": "SKU1701", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1701@example.com", "threshold": 10}},
    {"id": "ORDERS-1702", "title": "Orders scenario 1702", "data": {"sku": "SKU1702", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1702@example.com", "threshold": 20}},
    {"id": "ORDERS-1703", "title": "Orders scenario 1703", "data": {"sku": "SKU1703", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1703@example.com", "threshold": 30}},
    {"id": "ORDERS-1704", "title": "Orders scenario 1704", "data": {"sku": "SKU1704", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1704@example.com", "threshold": 40}},
    {"id": "ORDERS-1705", "title": "Orders scenario 1705", "data": {"sku": "SKU1705", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1705@example.com", "threshold": 50}},
    {"id": "ORDERS-1706", "title": "Orders scenario 1706", "data": {"sku": "SKU1706", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1706@example.com", "threshold": 60}},
    {"id": "ORDERS-1707", "title": "Orders scenario 1707", "data": {"sku": "SKU1707", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1707@example.com", "threshold": 70}},
    {"id": "ORDERS-1708", "title": "Orders scenario 1708", "data": {"sku": "SKU1708", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1708@example.com", "threshold": 80}},
    {"id": "ORDERS-1709", "title": "Orders scenario 1709", "data": {"sku": "SKU1709", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1709@example.com", "threshold": 90}},
    {"id": "ORDERS-1710", "title": "Orders scenario 1710", "data": {"sku": "SKU1710", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1710@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
