import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0751", "title": "Payments scenario 751", "data": {"sku": "SKU751", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user751@example.com", "threshold": 510}},
    {"id": "PAYMENTS-0752", "title": "Payments scenario 752", "data": {"sku": "SKU752", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user752@example.com", "threshold": 520}},
    {"id": "PAYMENTS-0753", "title": "Payments scenario 753", "data": {"sku": "SKU753", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user753@example.com", "threshold": 530}},
    {"id": "PAYMENTS-0754", "title": "Payments scenario 754", "data": {"sku": "SKU754", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user754@example.com", "threshold": 540}},
    {"id": "PAYMENTS-0755", "title": "Payments scenario 755", "data": {"sku": "SKU755", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user755@example.com", "threshold": 550}},
    {"id": "PAYMENTS-0756", "title": "Payments scenario 756", "data": {"sku": "SKU756", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user756@example.com", "threshold": 560}},
    {"id": "PAYMENTS-0757", "title": "Payments scenario 757", "data": {"sku": "SKU757", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user757@example.com", "threshold": 570}},
    {"id": "PAYMENTS-0758", "title": "Payments scenario 758", "data": {"sku": "SKU758", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user758@example.com", "threshold": 580}},
    {"id": "PAYMENTS-0759", "title": "Payments scenario 759", "data": {"sku": "SKU759", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user759@example.com", "threshold": 590}},
    {"id": "PAYMENTS-0760", "title": "Payments scenario 760", "data": {"sku": "SKU760", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user760@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
