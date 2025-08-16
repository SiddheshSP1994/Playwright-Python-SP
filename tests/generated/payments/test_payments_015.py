import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0871", "title": "Payments scenario 871", "data": {"sku": "SKU871", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user871@example.com", "threshold": 710}},
    {"id": "PAYMENTS-0872", "title": "Payments scenario 872", "data": {"sku": "SKU872", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user872@example.com", "threshold": 720}},
    {"id": "PAYMENTS-0873", "title": "Payments scenario 873", "data": {"sku": "SKU873", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user873@example.com", "threshold": 730}},
    {"id": "PAYMENTS-0874", "title": "Payments scenario 874", "data": {"sku": "SKU874", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user874@example.com", "threshold": 740}},
    {"id": "PAYMENTS-0875", "title": "Payments scenario 875", "data": {"sku": "SKU875", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user875@example.com", "threshold": 750}},
    {"id": "PAYMENTS-0876", "title": "Payments scenario 876", "data": {"sku": "SKU876", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user876@example.com", "threshold": 760}},
    {"id": "PAYMENTS-0877", "title": "Payments scenario 877", "data": {"sku": "SKU877", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user877@example.com", "threshold": 770}},
    {"id": "PAYMENTS-0878", "title": "Payments scenario 878", "data": {"sku": "SKU878", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user878@example.com", "threshold": 780}},
    {"id": "PAYMENTS-0879", "title": "Payments scenario 879", "data": {"sku": "SKU879", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user879@example.com", "threshold": 790}},
    {"id": "PAYMENTS-0880", "title": "Payments scenario 880", "data": {"sku": "SKU880", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user880@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
