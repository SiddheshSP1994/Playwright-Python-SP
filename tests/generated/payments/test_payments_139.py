import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8311", "title": "Payments scenario 8311", "data": {"sku": "SKU8311", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8311@example.com", "threshold": 110}},
    {"id": "PAYMENTS-8312", "title": "Payments scenario 8312", "data": {"sku": "SKU8312", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8312@example.com", "threshold": 120}},
    {"id": "PAYMENTS-8313", "title": "Payments scenario 8313", "data": {"sku": "SKU8313", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8313@example.com", "threshold": 130}},
    {"id": "PAYMENTS-8314", "title": "Payments scenario 8314", "data": {"sku": "SKU8314", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8314@example.com", "threshold": 140}},
    {"id": "PAYMENTS-8315", "title": "Payments scenario 8315", "data": {"sku": "SKU8315", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8315@example.com", "threshold": 150}},
    {"id": "PAYMENTS-8316", "title": "Payments scenario 8316", "data": {"sku": "SKU8316", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8316@example.com", "threshold": 160}},
    {"id": "PAYMENTS-8317", "title": "Payments scenario 8317", "data": {"sku": "SKU8317", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8317@example.com", "threshold": 170}},
    {"id": "PAYMENTS-8318", "title": "Payments scenario 8318", "data": {"sku": "SKU8318", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8318@example.com", "threshold": 180}},
    {"id": "PAYMENTS-8319", "title": "Payments scenario 8319", "data": {"sku": "SKU8319", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8319@example.com", "threshold": 190}},
    {"id": "PAYMENTS-8320", "title": "Payments scenario 8320", "data": {"sku": "SKU8320", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8320@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
