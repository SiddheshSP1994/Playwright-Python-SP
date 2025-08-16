import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8371", "title": "Payments scenario 8371", "data": {"sku": "SKU8371", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8371@example.com", "threshold": 710}},
    {"id": "PAYMENTS-8372", "title": "Payments scenario 8372", "data": {"sku": "SKU8372", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8372@example.com", "threshold": 720}},
    {"id": "PAYMENTS-8373", "title": "Payments scenario 8373", "data": {"sku": "SKU8373", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8373@example.com", "threshold": 730}},
    {"id": "PAYMENTS-8374", "title": "Payments scenario 8374", "data": {"sku": "SKU8374", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8374@example.com", "threshold": 740}},
    {"id": "PAYMENTS-8375", "title": "Payments scenario 8375", "data": {"sku": "SKU8375", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8375@example.com", "threshold": 750}},
    {"id": "PAYMENTS-8376", "title": "Payments scenario 8376", "data": {"sku": "SKU8376", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8376@example.com", "threshold": 760}},
    {"id": "PAYMENTS-8377", "title": "Payments scenario 8377", "data": {"sku": "SKU8377", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8377@example.com", "threshold": 770}},
    {"id": "PAYMENTS-8378", "title": "Payments scenario 8378", "data": {"sku": "SKU8378", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8378@example.com", "threshold": 780}},
    {"id": "PAYMENTS-8379", "title": "Payments scenario 8379", "data": {"sku": "SKU8379", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8379@example.com", "threshold": 790}},
    {"id": "PAYMENTS-8380", "title": "Payments scenario 8380", "data": {"sku": "SKU8380", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8380@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
