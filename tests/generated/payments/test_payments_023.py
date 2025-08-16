import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1351", "title": "Payments scenario 1351", "data": {"sku": "SKU1351", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1351@example.com", "threshold": 510}},
    {"id": "PAYMENTS-1352", "title": "Payments scenario 1352", "data": {"sku": "SKU1352", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1352@example.com", "threshold": 520}},
    {"id": "PAYMENTS-1353", "title": "Payments scenario 1353", "data": {"sku": "SKU1353", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1353@example.com", "threshold": 530}},
    {"id": "PAYMENTS-1354", "title": "Payments scenario 1354", "data": {"sku": "SKU1354", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1354@example.com", "threshold": 540}},
    {"id": "PAYMENTS-1355", "title": "Payments scenario 1355", "data": {"sku": "SKU1355", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1355@example.com", "threshold": 550}},
    {"id": "PAYMENTS-1356", "title": "Payments scenario 1356", "data": {"sku": "SKU1356", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1356@example.com", "threshold": 560}},
    {"id": "PAYMENTS-1357", "title": "Payments scenario 1357", "data": {"sku": "SKU1357", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1357@example.com", "threshold": 570}},
    {"id": "PAYMENTS-1358", "title": "Payments scenario 1358", "data": {"sku": "SKU1358", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1358@example.com", "threshold": 580}},
    {"id": "PAYMENTS-1359", "title": "Payments scenario 1359", "data": {"sku": "SKU1359", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1359@example.com", "threshold": 590}},
    {"id": "PAYMENTS-1360", "title": "Payments scenario 1360", "data": {"sku": "SKU1360", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1360@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
