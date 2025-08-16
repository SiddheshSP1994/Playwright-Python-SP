import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-4311", "title": "Analytics scenario 4311", "data": {"sku": "SKU4311", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4311@example.com", "threshold": 110}},
    {"id": "ANALYTICS-4312", "title": "Analytics scenario 4312", "data": {"sku": "SKU4312", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4312@example.com", "threshold": 120}},
    {"id": "ANALYTICS-4313", "title": "Analytics scenario 4313", "data": {"sku": "SKU4313", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4313@example.com", "threshold": 130}},
    {"id": "ANALYTICS-4314", "title": "Analytics scenario 4314", "data": {"sku": "SKU4314", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4314@example.com", "threshold": 140}},
    {"id": "ANALYTICS-4315", "title": "Analytics scenario 4315", "data": {"sku": "SKU4315", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4315@example.com", "threshold": 150}},
    {"id": "ANALYTICS-4316", "title": "Analytics scenario 4316", "data": {"sku": "SKU4316", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4316@example.com", "threshold": 160}},
    {"id": "ANALYTICS-4317", "title": "Analytics scenario 4317", "data": {"sku": "SKU4317", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4317@example.com", "threshold": 170}},
    {"id": "ANALYTICS-4318", "title": "Analytics scenario 4318", "data": {"sku": "SKU4318", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4318@example.com", "threshold": 180}},
    {"id": "ANALYTICS-4319", "title": "Analytics scenario 4319", "data": {"sku": "SKU4319", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4319@example.com", "threshold": 190}},
    {"id": "ANALYTICS-4320", "title": "Analytics scenario 4320", "data": {"sku": "SKU4320", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4320@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
