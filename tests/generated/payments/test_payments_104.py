import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6211", "title": "Payments scenario 6211", "data": {"sku": "SKU6211", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6211@example.com", "threshold": 110}},
    {"id": "PAYMENTS-6212", "title": "Payments scenario 6212", "data": {"sku": "SKU6212", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6212@example.com", "threshold": 120}},
    {"id": "PAYMENTS-6213", "title": "Payments scenario 6213", "data": {"sku": "SKU6213", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6213@example.com", "threshold": 130}},
    {"id": "PAYMENTS-6214", "title": "Payments scenario 6214", "data": {"sku": "SKU6214", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6214@example.com", "threshold": 140}},
    {"id": "PAYMENTS-6215", "title": "Payments scenario 6215", "data": {"sku": "SKU6215", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6215@example.com", "threshold": 150}},
    {"id": "PAYMENTS-6216", "title": "Payments scenario 6216", "data": {"sku": "SKU6216", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6216@example.com", "threshold": 160}},
    {"id": "PAYMENTS-6217", "title": "Payments scenario 6217", "data": {"sku": "SKU6217", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6217@example.com", "threshold": 170}},
    {"id": "PAYMENTS-6218", "title": "Payments scenario 6218", "data": {"sku": "SKU6218", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6218@example.com", "threshold": 180}},
    {"id": "PAYMENTS-6219", "title": "Payments scenario 6219", "data": {"sku": "SKU6219", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6219@example.com", "threshold": 190}},
    {"id": "PAYMENTS-6220", "title": "Payments scenario 6220", "data": {"sku": "SKU6220", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6220@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
