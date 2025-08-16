import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3211", "title": "Payments scenario 3211", "data": {"sku": "SKU3211", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3211@example.com", "threshold": 110}},
    {"id": "PAYMENTS-3212", "title": "Payments scenario 3212", "data": {"sku": "SKU3212", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3212@example.com", "threshold": 120}},
    {"id": "PAYMENTS-3213", "title": "Payments scenario 3213", "data": {"sku": "SKU3213", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3213@example.com", "threshold": 130}},
    {"id": "PAYMENTS-3214", "title": "Payments scenario 3214", "data": {"sku": "SKU3214", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3214@example.com", "threshold": 140}},
    {"id": "PAYMENTS-3215", "title": "Payments scenario 3215", "data": {"sku": "SKU3215", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3215@example.com", "threshold": 150}},
    {"id": "PAYMENTS-3216", "title": "Payments scenario 3216", "data": {"sku": "SKU3216", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3216@example.com", "threshold": 160}},
    {"id": "PAYMENTS-3217", "title": "Payments scenario 3217", "data": {"sku": "SKU3217", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3217@example.com", "threshold": 170}},
    {"id": "PAYMENTS-3218", "title": "Payments scenario 3218", "data": {"sku": "SKU3218", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3218@example.com", "threshold": 180}},
    {"id": "PAYMENTS-3219", "title": "Payments scenario 3219", "data": {"sku": "SKU3219", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3219@example.com", "threshold": 190}},
    {"id": "PAYMENTS-3220", "title": "Payments scenario 3220", "data": {"sku": "SKU3220", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3220@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
