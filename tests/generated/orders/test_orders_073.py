import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4341", "title": "Orders scenario 4341", "data": {"sku": "SKU4341", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4341@example.com", "threshold": 410}},
    {"id": "ORDERS-4342", "title": "Orders scenario 4342", "data": {"sku": "SKU4342", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4342@example.com", "threshold": 420}},
    {"id": "ORDERS-4343", "title": "Orders scenario 4343", "data": {"sku": "SKU4343", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4343@example.com", "threshold": 430}},
    {"id": "ORDERS-4344", "title": "Orders scenario 4344", "data": {"sku": "SKU4344", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4344@example.com", "threshold": 440}},
    {"id": "ORDERS-4345", "title": "Orders scenario 4345", "data": {"sku": "SKU4345", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4345@example.com", "threshold": 450}},
    {"id": "ORDERS-4346", "title": "Orders scenario 4346", "data": {"sku": "SKU4346", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4346@example.com", "threshold": 460}},
    {"id": "ORDERS-4347", "title": "Orders scenario 4347", "data": {"sku": "SKU4347", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4347@example.com", "threshold": 470}},
    {"id": "ORDERS-4348", "title": "Orders scenario 4348", "data": {"sku": "SKU4348", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4348@example.com", "threshold": 480}},
    {"id": "ORDERS-4349", "title": "Orders scenario 4349", "data": {"sku": "SKU4349", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4349@example.com", "threshold": 490}},
    {"id": "ORDERS-4350", "title": "Orders scenario 4350", "data": {"sku": "SKU4350", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4350@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
