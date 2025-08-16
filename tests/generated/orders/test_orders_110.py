import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6561", "title": "Orders scenario 6561", "data": {"sku": "SKU6561", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6561@example.com", "threshold": 610}},
    {"id": "ORDERS-6562", "title": "Orders scenario 6562", "data": {"sku": "SKU6562", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6562@example.com", "threshold": 620}},
    {"id": "ORDERS-6563", "title": "Orders scenario 6563", "data": {"sku": "SKU6563", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6563@example.com", "threshold": 630}},
    {"id": "ORDERS-6564", "title": "Orders scenario 6564", "data": {"sku": "SKU6564", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6564@example.com", "threshold": 640}},
    {"id": "ORDERS-6565", "title": "Orders scenario 6565", "data": {"sku": "SKU6565", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6565@example.com", "threshold": 650}},
    {"id": "ORDERS-6566", "title": "Orders scenario 6566", "data": {"sku": "SKU6566", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6566@example.com", "threshold": 660}},
    {"id": "ORDERS-6567", "title": "Orders scenario 6567", "data": {"sku": "SKU6567", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6567@example.com", "threshold": 670}},
    {"id": "ORDERS-6568", "title": "Orders scenario 6568", "data": {"sku": "SKU6568", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6568@example.com", "threshold": 680}},
    {"id": "ORDERS-6569", "title": "Orders scenario 6569", "data": {"sku": "SKU6569", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6569@example.com", "threshold": 690}},
    {"id": "ORDERS-6570", "title": "Orders scenario 6570", "data": {"sku": "SKU6570", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6570@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
