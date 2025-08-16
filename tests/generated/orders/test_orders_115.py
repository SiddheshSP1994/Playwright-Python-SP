import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6861", "title": "Orders scenario 6861", "data": {"sku": "SKU6861", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6861@example.com", "threshold": 610}},
    {"id": "ORDERS-6862", "title": "Orders scenario 6862", "data": {"sku": "SKU6862", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6862@example.com", "threshold": 620}},
    {"id": "ORDERS-6863", "title": "Orders scenario 6863", "data": {"sku": "SKU6863", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6863@example.com", "threshold": 630}},
    {"id": "ORDERS-6864", "title": "Orders scenario 6864", "data": {"sku": "SKU6864", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6864@example.com", "threshold": 640}},
    {"id": "ORDERS-6865", "title": "Orders scenario 6865", "data": {"sku": "SKU6865", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6865@example.com", "threshold": 650}},
    {"id": "ORDERS-6866", "title": "Orders scenario 6866", "data": {"sku": "SKU6866", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6866@example.com", "threshold": 660}},
    {"id": "ORDERS-6867", "title": "Orders scenario 6867", "data": {"sku": "SKU6867", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6867@example.com", "threshold": 670}},
    {"id": "ORDERS-6868", "title": "Orders scenario 6868", "data": {"sku": "SKU6868", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6868@example.com", "threshold": 680}},
    {"id": "ORDERS-6869", "title": "Orders scenario 6869", "data": {"sku": "SKU6869", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6869@example.com", "threshold": 690}},
    {"id": "ORDERS-6870", "title": "Orders scenario 6870", "data": {"sku": "SKU6870", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6870@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
