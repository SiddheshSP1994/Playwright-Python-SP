import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0861", "title": "Orders scenario 861", "data": {"sku": "SKU861", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user861@example.com", "threshold": 610}},
    {"id": "ORDERS-0862", "title": "Orders scenario 862", "data": {"sku": "SKU862", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user862@example.com", "threshold": 620}},
    {"id": "ORDERS-0863", "title": "Orders scenario 863", "data": {"sku": "SKU863", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user863@example.com", "threshold": 630}},
    {"id": "ORDERS-0864", "title": "Orders scenario 864", "data": {"sku": "SKU864", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user864@example.com", "threshold": 640}},
    {"id": "ORDERS-0865", "title": "Orders scenario 865", "data": {"sku": "SKU865", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user865@example.com", "threshold": 650}},
    {"id": "ORDERS-0866", "title": "Orders scenario 866", "data": {"sku": "SKU866", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user866@example.com", "threshold": 660}},
    {"id": "ORDERS-0867", "title": "Orders scenario 867", "data": {"sku": "SKU867", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user867@example.com", "threshold": 670}},
    {"id": "ORDERS-0868", "title": "Orders scenario 868", "data": {"sku": "SKU868", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user868@example.com", "threshold": 680}},
    {"id": "ORDERS-0869", "title": "Orders scenario 869", "data": {"sku": "SKU869", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user869@example.com", "threshold": 690}},
    {"id": "ORDERS-0870", "title": "Orders scenario 870", "data": {"sku": "SKU870", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user870@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
