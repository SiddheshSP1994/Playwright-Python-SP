import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1111", "title": "Payments scenario 1111", "data": {"sku": "SKU1111", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1111@example.com", "threshold": 110}},
    {"id": "PAYMENTS-1112", "title": "Payments scenario 1112", "data": {"sku": "SKU1112", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1112@example.com", "threshold": 120}},
    {"id": "PAYMENTS-1113", "title": "Payments scenario 1113", "data": {"sku": "SKU1113", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1113@example.com", "threshold": 130}},
    {"id": "PAYMENTS-1114", "title": "Payments scenario 1114", "data": {"sku": "SKU1114", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1114@example.com", "threshold": 140}},
    {"id": "PAYMENTS-1115", "title": "Payments scenario 1115", "data": {"sku": "SKU1115", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1115@example.com", "threshold": 150}},
    {"id": "PAYMENTS-1116", "title": "Payments scenario 1116", "data": {"sku": "SKU1116", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1116@example.com", "threshold": 160}},
    {"id": "PAYMENTS-1117", "title": "Payments scenario 1117", "data": {"sku": "SKU1117", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1117@example.com", "threshold": 170}},
    {"id": "PAYMENTS-1118", "title": "Payments scenario 1118", "data": {"sku": "SKU1118", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1118@example.com", "threshold": 180}},
    {"id": "PAYMENTS-1119", "title": "Payments scenario 1119", "data": {"sku": "SKU1119", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1119@example.com", "threshold": 190}},
    {"id": "PAYMENTS-1120", "title": "Payments scenario 1120", "data": {"sku": "SKU1120", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1120@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
