import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9861", "title": "Orders scenario 9861", "data": {"sku": "SKU9861", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9861@example.com", "threshold": 610}},
    {"id": "ORDERS-9862", "title": "Orders scenario 9862", "data": {"sku": "SKU9862", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9862@example.com", "threshold": 620}},
    {"id": "ORDERS-9863", "title": "Orders scenario 9863", "data": {"sku": "SKU9863", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9863@example.com", "threshold": 630}},
    {"id": "ORDERS-9864", "title": "Orders scenario 9864", "data": {"sku": "SKU9864", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9864@example.com", "threshold": 640}},
    {"id": "ORDERS-9865", "title": "Orders scenario 9865", "data": {"sku": "SKU9865", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9865@example.com", "threshold": 650}},
    {"id": "ORDERS-9866", "title": "Orders scenario 9866", "data": {"sku": "SKU9866", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9866@example.com", "threshold": 660}},
    {"id": "ORDERS-9867", "title": "Orders scenario 9867", "data": {"sku": "SKU9867", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9867@example.com", "threshold": 670}},
    {"id": "ORDERS-9868", "title": "Orders scenario 9868", "data": {"sku": "SKU9868", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9868@example.com", "threshold": 680}},
    {"id": "ORDERS-9869", "title": "Orders scenario 9869", "data": {"sku": "SKU9869", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9869@example.com", "threshold": 690}},
    {"id": "ORDERS-9870", "title": "Orders scenario 9870", "data": {"sku": "SKU9870", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9870@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
