import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6871", "title": "Payments scenario 6871", "data": {"sku": "SKU6871", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6871@example.com", "threshold": 710}},
    {"id": "PAYMENTS-6872", "title": "Payments scenario 6872", "data": {"sku": "SKU6872", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6872@example.com", "threshold": 720}},
    {"id": "PAYMENTS-6873", "title": "Payments scenario 6873", "data": {"sku": "SKU6873", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6873@example.com", "threshold": 730}},
    {"id": "PAYMENTS-6874", "title": "Payments scenario 6874", "data": {"sku": "SKU6874", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6874@example.com", "threshold": 740}},
    {"id": "PAYMENTS-6875", "title": "Payments scenario 6875", "data": {"sku": "SKU6875", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6875@example.com", "threshold": 750}},
    {"id": "PAYMENTS-6876", "title": "Payments scenario 6876", "data": {"sku": "SKU6876", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6876@example.com", "threshold": 760}},
    {"id": "PAYMENTS-6877", "title": "Payments scenario 6877", "data": {"sku": "SKU6877", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6877@example.com", "threshold": 770}},
    {"id": "PAYMENTS-6878", "title": "Payments scenario 6878", "data": {"sku": "SKU6878", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6878@example.com", "threshold": 780}},
    {"id": "PAYMENTS-6879", "title": "Payments scenario 6879", "data": {"sku": "SKU6879", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6879@example.com", "threshold": 790}},
    {"id": "PAYMENTS-6880", "title": "Payments scenario 6880", "data": {"sku": "SKU6880", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6880@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
