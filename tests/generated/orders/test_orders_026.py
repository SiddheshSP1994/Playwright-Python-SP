import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1521", "title": "Orders scenario 1521", "data": {"sku": "SKU1521", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1521@example.com", "threshold": 210}},
    {"id": "ORDERS-1522", "title": "Orders scenario 1522", "data": {"sku": "SKU1522", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1522@example.com", "threshold": 220}},
    {"id": "ORDERS-1523", "title": "Orders scenario 1523", "data": {"sku": "SKU1523", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1523@example.com", "threshold": 230}},
    {"id": "ORDERS-1524", "title": "Orders scenario 1524", "data": {"sku": "SKU1524", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1524@example.com", "threshold": 240}},
    {"id": "ORDERS-1525", "title": "Orders scenario 1525", "data": {"sku": "SKU1525", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1525@example.com", "threshold": 250}},
    {"id": "ORDERS-1526", "title": "Orders scenario 1526", "data": {"sku": "SKU1526", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1526@example.com", "threshold": 260}},
    {"id": "ORDERS-1527", "title": "Orders scenario 1527", "data": {"sku": "SKU1527", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1527@example.com", "threshold": 270}},
    {"id": "ORDERS-1528", "title": "Orders scenario 1528", "data": {"sku": "SKU1528", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1528@example.com", "threshold": 280}},
    {"id": "ORDERS-1529", "title": "Orders scenario 1529", "data": {"sku": "SKU1529", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1529@example.com", "threshold": 290}},
    {"id": "ORDERS-1530", "title": "Orders scenario 1530", "data": {"sku": "SKU1530", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1530@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
