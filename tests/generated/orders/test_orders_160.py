import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9561", "title": "Orders scenario 9561", "data": {"sku": "SKU9561", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9561@example.com", "threshold": 610}},
    {"id": "ORDERS-9562", "title": "Orders scenario 9562", "data": {"sku": "SKU9562", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9562@example.com", "threshold": 620}},
    {"id": "ORDERS-9563", "title": "Orders scenario 9563", "data": {"sku": "SKU9563", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9563@example.com", "threshold": 630}},
    {"id": "ORDERS-9564", "title": "Orders scenario 9564", "data": {"sku": "SKU9564", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9564@example.com", "threshold": 640}},
    {"id": "ORDERS-9565", "title": "Orders scenario 9565", "data": {"sku": "SKU9565", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9565@example.com", "threshold": 650}},
    {"id": "ORDERS-9566", "title": "Orders scenario 9566", "data": {"sku": "SKU9566", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9566@example.com", "threshold": 660}},
    {"id": "ORDERS-9567", "title": "Orders scenario 9567", "data": {"sku": "SKU9567", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9567@example.com", "threshold": 670}},
    {"id": "ORDERS-9568", "title": "Orders scenario 9568", "data": {"sku": "SKU9568", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9568@example.com", "threshold": 680}},
    {"id": "ORDERS-9569", "title": "Orders scenario 9569", "data": {"sku": "SKU9569", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9569@example.com", "threshold": 690}},
    {"id": "ORDERS-9570", "title": "Orders scenario 9570", "data": {"sku": "SKU9570", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9570@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
