import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5311", "title": "Payments scenario 5311", "data": {"sku": "SKU5311", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5311@example.com", "threshold": 110}},
    {"id": "PAYMENTS-5312", "title": "Payments scenario 5312", "data": {"sku": "SKU5312", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5312@example.com", "threshold": 120}},
    {"id": "PAYMENTS-5313", "title": "Payments scenario 5313", "data": {"sku": "SKU5313", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5313@example.com", "threshold": 130}},
    {"id": "PAYMENTS-5314", "title": "Payments scenario 5314", "data": {"sku": "SKU5314", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5314@example.com", "threshold": 140}},
    {"id": "PAYMENTS-5315", "title": "Payments scenario 5315", "data": {"sku": "SKU5315", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5315@example.com", "threshold": 150}},
    {"id": "PAYMENTS-5316", "title": "Payments scenario 5316", "data": {"sku": "SKU5316", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5316@example.com", "threshold": 160}},
    {"id": "PAYMENTS-5317", "title": "Payments scenario 5317", "data": {"sku": "SKU5317", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5317@example.com", "threshold": 170}},
    {"id": "PAYMENTS-5318", "title": "Payments scenario 5318", "data": {"sku": "SKU5318", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5318@example.com", "threshold": 180}},
    {"id": "PAYMENTS-5319", "title": "Payments scenario 5319", "data": {"sku": "SKU5319", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5319@example.com", "threshold": 190}},
    {"id": "PAYMENTS-5320", "title": "Payments scenario 5320", "data": {"sku": "SKU5320", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5320@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
