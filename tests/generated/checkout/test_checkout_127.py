import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-7561", "title": "Checkout scenario 7561", "data": {"sku": "SKU7561", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7561@example.com", "threshold": 610}},
    {"id": "CHECKOUT-7562", "title": "Checkout scenario 7562", "data": {"sku": "SKU7562", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7562@example.com", "threshold": 620}},
    {"id": "CHECKOUT-7563", "title": "Checkout scenario 7563", "data": {"sku": "SKU7563", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7563@example.com", "threshold": 630}},
    {"id": "CHECKOUT-7564", "title": "Checkout scenario 7564", "data": {"sku": "SKU7564", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7564@example.com", "threshold": 640}},
    {"id": "CHECKOUT-7565", "title": "Checkout scenario 7565", "data": {"sku": "SKU7565", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7565@example.com", "threshold": 650}},
    {"id": "CHECKOUT-7566", "title": "Checkout scenario 7566", "data": {"sku": "SKU7566", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7566@example.com", "threshold": 660}},
    {"id": "CHECKOUT-7567", "title": "Checkout scenario 7567", "data": {"sku": "SKU7567", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7567@example.com", "threshold": 670}},
    {"id": "CHECKOUT-7568", "title": "Checkout scenario 7568", "data": {"sku": "SKU7568", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7568@example.com", "threshold": 680}},
    {"id": "CHECKOUT-7569", "title": "Checkout scenario 7569", "data": {"sku": "SKU7569", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7569@example.com", "threshold": 690}},
    {"id": "CHECKOUT-7570", "title": "Checkout scenario 7570", "data": {"sku": "SKU7570", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7570@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
