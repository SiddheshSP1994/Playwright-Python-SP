import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-9871", "title": "Payments scenario 9871", "data": {"sku": "SKU9871", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9871@example.com", "threshold": 710}},
    {"id": "PAYMENTS-9872", "title": "Payments scenario 9872", "data": {"sku": "SKU9872", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9872@example.com", "threshold": 720}},
    {"id": "PAYMENTS-9873", "title": "Payments scenario 9873", "data": {"sku": "SKU9873", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9873@example.com", "threshold": 730}},
    {"id": "PAYMENTS-9874", "title": "Payments scenario 9874", "data": {"sku": "SKU9874", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9874@example.com", "threshold": 740}},
    {"id": "PAYMENTS-9875", "title": "Payments scenario 9875", "data": {"sku": "SKU9875", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9875@example.com", "threshold": 750}},
    {"id": "PAYMENTS-9876", "title": "Payments scenario 9876", "data": {"sku": "SKU9876", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9876@example.com", "threshold": 760}},
    {"id": "PAYMENTS-9877", "title": "Payments scenario 9877", "data": {"sku": "SKU9877", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9877@example.com", "threshold": 770}},
    {"id": "PAYMENTS-9878", "title": "Payments scenario 9878", "data": {"sku": "SKU9878", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9878@example.com", "threshold": 780}},
    {"id": "PAYMENTS-9879", "title": "Payments scenario 9879", "data": {"sku": "SKU9879", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9879@example.com", "threshold": 790}},
    {"id": "PAYMENTS-9880", "title": "Payments scenario 9880", "data": {"sku": "SKU9880", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9880@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
