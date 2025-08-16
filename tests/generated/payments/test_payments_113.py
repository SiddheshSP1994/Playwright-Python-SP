import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6751", "title": "Payments scenario 6751", "data": {"sku": "SKU6751", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6751@example.com", "threshold": 510}},
    {"id": "PAYMENTS-6752", "title": "Payments scenario 6752", "data": {"sku": "SKU6752", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6752@example.com", "threshold": 520}},
    {"id": "PAYMENTS-6753", "title": "Payments scenario 6753", "data": {"sku": "SKU6753", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6753@example.com", "threshold": 530}},
    {"id": "PAYMENTS-6754", "title": "Payments scenario 6754", "data": {"sku": "SKU6754", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6754@example.com", "threshold": 540}},
    {"id": "PAYMENTS-6755", "title": "Payments scenario 6755", "data": {"sku": "SKU6755", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6755@example.com", "threshold": 550}},
    {"id": "PAYMENTS-6756", "title": "Payments scenario 6756", "data": {"sku": "SKU6756", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6756@example.com", "threshold": 560}},
    {"id": "PAYMENTS-6757", "title": "Payments scenario 6757", "data": {"sku": "SKU6757", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6757@example.com", "threshold": 570}},
    {"id": "PAYMENTS-6758", "title": "Payments scenario 6758", "data": {"sku": "SKU6758", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6758@example.com", "threshold": 580}},
    {"id": "PAYMENTS-6759", "title": "Payments scenario 6759", "data": {"sku": "SKU6759", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6759@example.com", "threshold": 590}},
    {"id": "PAYMENTS-6760", "title": "Payments scenario 6760", "data": {"sku": "SKU6760", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6760@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
