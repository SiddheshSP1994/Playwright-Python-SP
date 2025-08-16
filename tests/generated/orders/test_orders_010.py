import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0561", "title": "Orders scenario 561", "data": {"sku": "SKU561", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user561@example.com", "threshold": 610}},
    {"id": "ORDERS-0562", "title": "Orders scenario 562", "data": {"sku": "SKU562", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user562@example.com", "threshold": 620}},
    {"id": "ORDERS-0563", "title": "Orders scenario 563", "data": {"sku": "SKU563", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user563@example.com", "threshold": 630}},
    {"id": "ORDERS-0564", "title": "Orders scenario 564", "data": {"sku": "SKU564", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user564@example.com", "threshold": 640}},
    {"id": "ORDERS-0565", "title": "Orders scenario 565", "data": {"sku": "SKU565", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user565@example.com", "threshold": 650}},
    {"id": "ORDERS-0566", "title": "Orders scenario 566", "data": {"sku": "SKU566", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user566@example.com", "threshold": 660}},
    {"id": "ORDERS-0567", "title": "Orders scenario 567", "data": {"sku": "SKU567", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user567@example.com", "threshold": 670}},
    {"id": "ORDERS-0568", "title": "Orders scenario 568", "data": {"sku": "SKU568", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user568@example.com", "threshold": 680}},
    {"id": "ORDERS-0569", "title": "Orders scenario 569", "data": {"sku": "SKU569", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user569@example.com", "threshold": 690}},
    {"id": "ORDERS-0570", "title": "Orders scenario 570", "data": {"sku": "SKU570", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user570@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
