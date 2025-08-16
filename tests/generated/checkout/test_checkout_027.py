import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1561", "title": "Checkout scenario 1561", "data": {"sku": "SKU1561", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1561@example.com", "threshold": 610}},
    {"id": "CHECKOUT-1562", "title": "Checkout scenario 1562", "data": {"sku": "SKU1562", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1562@example.com", "threshold": 620}},
    {"id": "CHECKOUT-1563", "title": "Checkout scenario 1563", "data": {"sku": "SKU1563", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1563@example.com", "threshold": 630}},
    {"id": "CHECKOUT-1564", "title": "Checkout scenario 1564", "data": {"sku": "SKU1564", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1564@example.com", "threshold": 640}},
    {"id": "CHECKOUT-1565", "title": "Checkout scenario 1565", "data": {"sku": "SKU1565", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1565@example.com", "threshold": 650}},
    {"id": "CHECKOUT-1566", "title": "Checkout scenario 1566", "data": {"sku": "SKU1566", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1566@example.com", "threshold": 660}},
    {"id": "CHECKOUT-1567", "title": "Checkout scenario 1567", "data": {"sku": "SKU1567", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1567@example.com", "threshold": 670}},
    {"id": "CHECKOUT-1568", "title": "Checkout scenario 1568", "data": {"sku": "SKU1568", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1568@example.com", "threshold": 680}},
    {"id": "CHECKOUT-1569", "title": "Checkout scenario 1569", "data": {"sku": "SKU1569", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1569@example.com", "threshold": 690}},
    {"id": "CHECKOUT-1570", "title": "Checkout scenario 1570", "data": {"sku": "SKU1570", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1570@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
