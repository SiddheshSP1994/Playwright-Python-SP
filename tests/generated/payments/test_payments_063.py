import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3751", "title": "Payments scenario 3751", "data": {"sku": "SKU3751", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3751@example.com", "threshold": 510}},
    {"id": "PAYMENTS-3752", "title": "Payments scenario 3752", "data": {"sku": "SKU3752", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3752@example.com", "threshold": 520}},
    {"id": "PAYMENTS-3753", "title": "Payments scenario 3753", "data": {"sku": "SKU3753", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3753@example.com", "threshold": 530}},
    {"id": "PAYMENTS-3754", "title": "Payments scenario 3754", "data": {"sku": "SKU3754", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3754@example.com", "threshold": 540}},
    {"id": "PAYMENTS-3755", "title": "Payments scenario 3755", "data": {"sku": "SKU3755", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3755@example.com", "threshold": 550}},
    {"id": "PAYMENTS-3756", "title": "Payments scenario 3756", "data": {"sku": "SKU3756", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3756@example.com", "threshold": 560}},
    {"id": "PAYMENTS-3757", "title": "Payments scenario 3757", "data": {"sku": "SKU3757", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3757@example.com", "threshold": 570}},
    {"id": "PAYMENTS-3758", "title": "Payments scenario 3758", "data": {"sku": "SKU3758", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3758@example.com", "threshold": 580}},
    {"id": "PAYMENTS-3759", "title": "Payments scenario 3759", "data": {"sku": "SKU3759", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3759@example.com", "threshold": 590}},
    {"id": "PAYMENTS-3760", "title": "Payments scenario 3760", "data": {"sku": "SKU3760", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3760@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
