import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7341", "title": "Orders scenario 7341", "data": {"sku": "SKU7341", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7341@example.com", "threshold": 410}},
    {"id": "ORDERS-7342", "title": "Orders scenario 7342", "data": {"sku": "SKU7342", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7342@example.com", "threshold": 420}},
    {"id": "ORDERS-7343", "title": "Orders scenario 7343", "data": {"sku": "SKU7343", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7343@example.com", "threshold": 430}},
    {"id": "ORDERS-7344", "title": "Orders scenario 7344", "data": {"sku": "SKU7344", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7344@example.com", "threshold": 440}},
    {"id": "ORDERS-7345", "title": "Orders scenario 7345", "data": {"sku": "SKU7345", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7345@example.com", "threshold": 450}},
    {"id": "ORDERS-7346", "title": "Orders scenario 7346", "data": {"sku": "SKU7346", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7346@example.com", "threshold": 460}},
    {"id": "ORDERS-7347", "title": "Orders scenario 7347", "data": {"sku": "SKU7347", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7347@example.com", "threshold": 470}},
    {"id": "ORDERS-7348", "title": "Orders scenario 7348", "data": {"sku": "SKU7348", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7348@example.com", "threshold": 480}},
    {"id": "ORDERS-7349", "title": "Orders scenario 7349", "data": {"sku": "SKU7349", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7349@example.com", "threshold": 490}},
    {"id": "ORDERS-7350", "title": "Orders scenario 7350", "data": {"sku": "SKU7350", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7350@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
