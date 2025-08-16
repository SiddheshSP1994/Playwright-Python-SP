import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3561", "title": "Orders scenario 3561", "data": {"sku": "SKU3561", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3561@example.com", "threshold": 610}},
    {"id": "ORDERS-3562", "title": "Orders scenario 3562", "data": {"sku": "SKU3562", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3562@example.com", "threshold": 620}},
    {"id": "ORDERS-3563", "title": "Orders scenario 3563", "data": {"sku": "SKU3563", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3563@example.com", "threshold": 630}},
    {"id": "ORDERS-3564", "title": "Orders scenario 3564", "data": {"sku": "SKU3564", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3564@example.com", "threshold": 640}},
    {"id": "ORDERS-3565", "title": "Orders scenario 3565", "data": {"sku": "SKU3565", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3565@example.com", "threshold": 650}},
    {"id": "ORDERS-3566", "title": "Orders scenario 3566", "data": {"sku": "SKU3566", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3566@example.com", "threshold": 660}},
    {"id": "ORDERS-3567", "title": "Orders scenario 3567", "data": {"sku": "SKU3567", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3567@example.com", "threshold": 670}},
    {"id": "ORDERS-3568", "title": "Orders scenario 3568", "data": {"sku": "SKU3568", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3568@example.com", "threshold": 680}},
    {"id": "ORDERS-3569", "title": "Orders scenario 3569", "data": {"sku": "SKU3569", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3569@example.com", "threshold": 690}},
    {"id": "ORDERS-3570", "title": "Orders scenario 3570", "data": {"sku": "SKU3570", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3570@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
