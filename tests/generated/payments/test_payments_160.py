import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-9571", "title": "Payments scenario 9571", "data": {"sku": "SKU9571", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9571@example.com", "threshold": 710}},
    {"id": "PAYMENTS-9572", "title": "Payments scenario 9572", "data": {"sku": "SKU9572", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9572@example.com", "threshold": 720}},
    {"id": "PAYMENTS-9573", "title": "Payments scenario 9573", "data": {"sku": "SKU9573", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9573@example.com", "threshold": 730}},
    {"id": "PAYMENTS-9574", "title": "Payments scenario 9574", "data": {"sku": "SKU9574", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9574@example.com", "threshold": 740}},
    {"id": "PAYMENTS-9575", "title": "Payments scenario 9575", "data": {"sku": "SKU9575", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9575@example.com", "threshold": 750}},
    {"id": "PAYMENTS-9576", "title": "Payments scenario 9576", "data": {"sku": "SKU9576", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9576@example.com", "threshold": 760}},
    {"id": "PAYMENTS-9577", "title": "Payments scenario 9577", "data": {"sku": "SKU9577", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9577@example.com", "threshold": 770}},
    {"id": "PAYMENTS-9578", "title": "Payments scenario 9578", "data": {"sku": "SKU9578", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9578@example.com", "threshold": 780}},
    {"id": "PAYMENTS-9579", "title": "Payments scenario 9579", "data": {"sku": "SKU9579", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9579@example.com", "threshold": 790}},
    {"id": "PAYMENTS-9580", "title": "Payments scenario 9580", "data": {"sku": "SKU9580", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9580@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
