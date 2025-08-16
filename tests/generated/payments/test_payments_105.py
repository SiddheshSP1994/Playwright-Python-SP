import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6271", "title": "Payments scenario 6271", "data": {"sku": "SKU6271", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6271@example.com", "threshold": 710}},
    {"id": "PAYMENTS-6272", "title": "Payments scenario 6272", "data": {"sku": "SKU6272", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6272@example.com", "threshold": 720}},
    {"id": "PAYMENTS-6273", "title": "Payments scenario 6273", "data": {"sku": "SKU6273", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6273@example.com", "threshold": 730}},
    {"id": "PAYMENTS-6274", "title": "Payments scenario 6274", "data": {"sku": "SKU6274", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6274@example.com", "threshold": 740}},
    {"id": "PAYMENTS-6275", "title": "Payments scenario 6275", "data": {"sku": "SKU6275", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6275@example.com", "threshold": 750}},
    {"id": "PAYMENTS-6276", "title": "Payments scenario 6276", "data": {"sku": "SKU6276", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6276@example.com", "threshold": 760}},
    {"id": "PAYMENTS-6277", "title": "Payments scenario 6277", "data": {"sku": "SKU6277", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6277@example.com", "threshold": 770}},
    {"id": "PAYMENTS-6278", "title": "Payments scenario 6278", "data": {"sku": "SKU6278", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6278@example.com", "threshold": 780}},
    {"id": "PAYMENTS-6279", "title": "Payments scenario 6279", "data": {"sku": "SKU6279", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6279@example.com", "threshold": 790}},
    {"id": "PAYMENTS-6280", "title": "Payments scenario 6280", "data": {"sku": "SKU6280", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6280@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
