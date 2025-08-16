import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1471", "title": "Payments scenario 1471", "data": {"sku": "SKU1471", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1471@example.com", "threshold": 710}},
    {"id": "PAYMENTS-1472", "title": "Payments scenario 1472", "data": {"sku": "SKU1472", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1472@example.com", "threshold": 720}},
    {"id": "PAYMENTS-1473", "title": "Payments scenario 1473", "data": {"sku": "SKU1473", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1473@example.com", "threshold": 730}},
    {"id": "PAYMENTS-1474", "title": "Payments scenario 1474", "data": {"sku": "SKU1474", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1474@example.com", "threshold": 740}},
    {"id": "PAYMENTS-1475", "title": "Payments scenario 1475", "data": {"sku": "SKU1475", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1475@example.com", "threshold": 750}},
    {"id": "PAYMENTS-1476", "title": "Payments scenario 1476", "data": {"sku": "SKU1476", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1476@example.com", "threshold": 760}},
    {"id": "PAYMENTS-1477", "title": "Payments scenario 1477", "data": {"sku": "SKU1477", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1477@example.com", "threshold": 770}},
    {"id": "PAYMENTS-1478", "title": "Payments scenario 1478", "data": {"sku": "SKU1478", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1478@example.com", "threshold": 780}},
    {"id": "PAYMENTS-1479", "title": "Payments scenario 1479", "data": {"sku": "SKU1479", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1479@example.com", "threshold": 790}},
    {"id": "PAYMENTS-1480", "title": "Payments scenario 1480", "data": {"sku": "SKU1480", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1480@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
