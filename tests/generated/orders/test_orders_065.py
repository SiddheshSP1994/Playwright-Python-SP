import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3861", "title": "Orders scenario 3861", "data": {"sku": "SKU3861", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3861@example.com", "threshold": 610}},
    {"id": "ORDERS-3862", "title": "Orders scenario 3862", "data": {"sku": "SKU3862", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3862@example.com", "threshold": 620}},
    {"id": "ORDERS-3863", "title": "Orders scenario 3863", "data": {"sku": "SKU3863", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3863@example.com", "threshold": 630}},
    {"id": "ORDERS-3864", "title": "Orders scenario 3864", "data": {"sku": "SKU3864", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3864@example.com", "threshold": 640}},
    {"id": "ORDERS-3865", "title": "Orders scenario 3865", "data": {"sku": "SKU3865", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3865@example.com", "threshold": 650}},
    {"id": "ORDERS-3866", "title": "Orders scenario 3866", "data": {"sku": "SKU3866", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3866@example.com", "threshold": 660}},
    {"id": "ORDERS-3867", "title": "Orders scenario 3867", "data": {"sku": "SKU3867", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3867@example.com", "threshold": 670}},
    {"id": "ORDERS-3868", "title": "Orders scenario 3868", "data": {"sku": "SKU3868", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3868@example.com", "threshold": 680}},
    {"id": "ORDERS-3869", "title": "Orders scenario 3869", "data": {"sku": "SKU3869", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3869@example.com", "threshold": 690}},
    {"id": "ORDERS-3870", "title": "Orders scenario 3870", "data": {"sku": "SKU3870", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3870@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
