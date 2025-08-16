import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1411", "title": "Payments scenario 1411", "data": {"sku": "SKU1411", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1411@example.com", "threshold": 110}},
    {"id": "PAYMENTS-1412", "title": "Payments scenario 1412", "data": {"sku": "SKU1412", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1412@example.com", "threshold": 120}},
    {"id": "PAYMENTS-1413", "title": "Payments scenario 1413", "data": {"sku": "SKU1413", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1413@example.com", "threshold": 130}},
    {"id": "PAYMENTS-1414", "title": "Payments scenario 1414", "data": {"sku": "SKU1414", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1414@example.com", "threshold": 140}},
    {"id": "PAYMENTS-1415", "title": "Payments scenario 1415", "data": {"sku": "SKU1415", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1415@example.com", "threshold": 150}},
    {"id": "PAYMENTS-1416", "title": "Payments scenario 1416", "data": {"sku": "SKU1416", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1416@example.com", "threshold": 160}},
    {"id": "PAYMENTS-1417", "title": "Payments scenario 1417", "data": {"sku": "SKU1417", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1417@example.com", "threshold": 170}},
    {"id": "PAYMENTS-1418", "title": "Payments scenario 1418", "data": {"sku": "SKU1418", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1418@example.com", "threshold": 180}},
    {"id": "PAYMENTS-1419", "title": "Payments scenario 1419", "data": {"sku": "SKU1419", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1419@example.com", "threshold": 190}},
    {"id": "PAYMENTS-1420", "title": "Payments scenario 1420", "data": {"sku": "SKU1420", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1420@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
