import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3571", "title": "Payments scenario 3571", "data": {"sku": "SKU3571", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3571@example.com", "threshold": 710}},
    {"id": "PAYMENTS-3572", "title": "Payments scenario 3572", "data": {"sku": "SKU3572", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3572@example.com", "threshold": 720}},
    {"id": "PAYMENTS-3573", "title": "Payments scenario 3573", "data": {"sku": "SKU3573", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3573@example.com", "threshold": 730}},
    {"id": "PAYMENTS-3574", "title": "Payments scenario 3574", "data": {"sku": "SKU3574", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3574@example.com", "threshold": 740}},
    {"id": "PAYMENTS-3575", "title": "Payments scenario 3575", "data": {"sku": "SKU3575", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3575@example.com", "threshold": 750}},
    {"id": "PAYMENTS-3576", "title": "Payments scenario 3576", "data": {"sku": "SKU3576", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3576@example.com", "threshold": 760}},
    {"id": "PAYMENTS-3577", "title": "Payments scenario 3577", "data": {"sku": "SKU3577", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3577@example.com", "threshold": 770}},
    {"id": "PAYMENTS-3578", "title": "Payments scenario 3578", "data": {"sku": "SKU3578", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3578@example.com", "threshold": 780}},
    {"id": "PAYMENTS-3579", "title": "Payments scenario 3579", "data": {"sku": "SKU3579", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3579@example.com", "threshold": 790}},
    {"id": "PAYMENTS-3580", "title": "Payments scenario 3580", "data": {"sku": "SKU3580", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3580@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
