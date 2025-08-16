import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6571", "title": "Payments scenario 6571", "data": {"sku": "SKU6571", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6571@example.com", "threshold": 710}},
    {"id": "PAYMENTS-6572", "title": "Payments scenario 6572", "data": {"sku": "SKU6572", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6572@example.com", "threshold": 720}},
    {"id": "PAYMENTS-6573", "title": "Payments scenario 6573", "data": {"sku": "SKU6573", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6573@example.com", "threshold": 730}},
    {"id": "PAYMENTS-6574", "title": "Payments scenario 6574", "data": {"sku": "SKU6574", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6574@example.com", "threshold": 740}},
    {"id": "PAYMENTS-6575", "title": "Payments scenario 6575", "data": {"sku": "SKU6575", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6575@example.com", "threshold": 750}},
    {"id": "PAYMENTS-6576", "title": "Payments scenario 6576", "data": {"sku": "SKU6576", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6576@example.com", "threshold": 760}},
    {"id": "PAYMENTS-6577", "title": "Payments scenario 6577", "data": {"sku": "SKU6577", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6577@example.com", "threshold": 770}},
    {"id": "PAYMENTS-6578", "title": "Payments scenario 6578", "data": {"sku": "SKU6578", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6578@example.com", "threshold": 780}},
    {"id": "PAYMENTS-6579", "title": "Payments scenario 6579", "data": {"sku": "SKU6579", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6579@example.com", "threshold": 790}},
    {"id": "PAYMENTS-6580", "title": "Payments scenario 6580", "data": {"sku": "SKU6580", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6580@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
