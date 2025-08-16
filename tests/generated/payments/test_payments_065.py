import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3871", "title": "Payments scenario 3871", "data": {"sku": "SKU3871", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3871@example.com", "threshold": 710}},
    {"id": "PAYMENTS-3872", "title": "Payments scenario 3872", "data": {"sku": "SKU3872", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3872@example.com", "threshold": 720}},
    {"id": "PAYMENTS-3873", "title": "Payments scenario 3873", "data": {"sku": "SKU3873", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3873@example.com", "threshold": 730}},
    {"id": "PAYMENTS-3874", "title": "Payments scenario 3874", "data": {"sku": "SKU3874", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3874@example.com", "threshold": 740}},
    {"id": "PAYMENTS-3875", "title": "Payments scenario 3875", "data": {"sku": "SKU3875", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3875@example.com", "threshold": 750}},
    {"id": "PAYMENTS-3876", "title": "Payments scenario 3876", "data": {"sku": "SKU3876", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3876@example.com", "threshold": 760}},
    {"id": "PAYMENTS-3877", "title": "Payments scenario 3877", "data": {"sku": "SKU3877", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3877@example.com", "threshold": 770}},
    {"id": "PAYMENTS-3878", "title": "Payments scenario 3878", "data": {"sku": "SKU3878", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3878@example.com", "threshold": 780}},
    {"id": "PAYMENTS-3879", "title": "Payments scenario 3879", "data": {"sku": "SKU3879", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3879@example.com", "threshold": 790}},
    {"id": "PAYMENTS-3880", "title": "Payments scenario 3880", "data": {"sku": "SKU3880", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3880@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
