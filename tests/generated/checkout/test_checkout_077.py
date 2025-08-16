import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4561", "title": "Checkout scenario 4561", "data": {"sku": "SKU4561", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4561@example.com", "threshold": 610}},
    {"id": "CHECKOUT-4562", "title": "Checkout scenario 4562", "data": {"sku": "SKU4562", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4562@example.com", "threshold": 620}},
    {"id": "CHECKOUT-4563", "title": "Checkout scenario 4563", "data": {"sku": "SKU4563", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4563@example.com", "threshold": 630}},
    {"id": "CHECKOUT-4564", "title": "Checkout scenario 4564", "data": {"sku": "SKU4564", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4564@example.com", "threshold": 640}},
    {"id": "CHECKOUT-4565", "title": "Checkout scenario 4565", "data": {"sku": "SKU4565", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4565@example.com", "threshold": 650}},
    {"id": "CHECKOUT-4566", "title": "Checkout scenario 4566", "data": {"sku": "SKU4566", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4566@example.com", "threshold": 660}},
    {"id": "CHECKOUT-4567", "title": "Checkout scenario 4567", "data": {"sku": "SKU4567", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4567@example.com", "threshold": 670}},
    {"id": "CHECKOUT-4568", "title": "Checkout scenario 4568", "data": {"sku": "SKU4568", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4568@example.com", "threshold": 680}},
    {"id": "CHECKOUT-4569", "title": "Checkout scenario 4569", "data": {"sku": "SKU4569", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4569@example.com", "threshold": 690}},
    {"id": "CHECKOUT-4570", "title": "Checkout scenario 4570", "data": {"sku": "SKU4570", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4570@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
