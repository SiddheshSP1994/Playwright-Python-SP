import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-9271", "title": "Payments scenario 9271", "data": {"sku": "SKU9271", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9271@example.com", "threshold": 710}},
    {"id": "PAYMENTS-9272", "title": "Payments scenario 9272", "data": {"sku": "SKU9272", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9272@example.com", "threshold": 720}},
    {"id": "PAYMENTS-9273", "title": "Payments scenario 9273", "data": {"sku": "SKU9273", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9273@example.com", "threshold": 730}},
    {"id": "PAYMENTS-9274", "title": "Payments scenario 9274", "data": {"sku": "SKU9274", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9274@example.com", "threshold": 740}},
    {"id": "PAYMENTS-9275", "title": "Payments scenario 9275", "data": {"sku": "SKU9275", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9275@example.com", "threshold": 750}},
    {"id": "PAYMENTS-9276", "title": "Payments scenario 9276", "data": {"sku": "SKU9276", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9276@example.com", "threshold": 760}},
    {"id": "PAYMENTS-9277", "title": "Payments scenario 9277", "data": {"sku": "SKU9277", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9277@example.com", "threshold": 770}},
    {"id": "PAYMENTS-9278", "title": "Payments scenario 9278", "data": {"sku": "SKU9278", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9278@example.com", "threshold": 780}},
    {"id": "PAYMENTS-9279", "title": "Payments scenario 9279", "data": {"sku": "SKU9279", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9279@example.com", "threshold": 790}},
    {"id": "PAYMENTS-9280", "title": "Payments scenario 9280", "data": {"sku": "SKU9280", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9280@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
