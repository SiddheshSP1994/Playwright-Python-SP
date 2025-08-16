import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1341", "title": "Orders scenario 1341", "data": {"sku": "SKU1341", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1341@example.com", "threshold": 410}},
    {"id": "ORDERS-1342", "title": "Orders scenario 1342", "data": {"sku": "SKU1342", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1342@example.com", "threshold": 420}},
    {"id": "ORDERS-1343", "title": "Orders scenario 1343", "data": {"sku": "SKU1343", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1343@example.com", "threshold": 430}},
    {"id": "ORDERS-1344", "title": "Orders scenario 1344", "data": {"sku": "SKU1344", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1344@example.com", "threshold": 440}},
    {"id": "ORDERS-1345", "title": "Orders scenario 1345", "data": {"sku": "SKU1345", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1345@example.com", "threshold": 450}},
    {"id": "ORDERS-1346", "title": "Orders scenario 1346", "data": {"sku": "SKU1346", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1346@example.com", "threshold": 460}},
    {"id": "ORDERS-1347", "title": "Orders scenario 1347", "data": {"sku": "SKU1347", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1347@example.com", "threshold": 470}},
    {"id": "ORDERS-1348", "title": "Orders scenario 1348", "data": {"sku": "SKU1348", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1348@example.com", "threshold": 480}},
    {"id": "ORDERS-1349", "title": "Orders scenario 1349", "data": {"sku": "SKU1349", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1349@example.com", "threshold": 490}},
    {"id": "ORDERS-1350", "title": "Orders scenario 1350", "data": {"sku": "SKU1350", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1350@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
