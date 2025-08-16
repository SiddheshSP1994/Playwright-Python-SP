import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1311", "title": "Analytics scenario 1311", "data": {"sku": "SKU1311", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1311@example.com", "threshold": 110}},
    {"id": "ANALYTICS-1312", "title": "Analytics scenario 1312", "data": {"sku": "SKU1312", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1312@example.com", "threshold": 120}},
    {"id": "ANALYTICS-1313", "title": "Analytics scenario 1313", "data": {"sku": "SKU1313", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1313@example.com", "threshold": 130}},
    {"id": "ANALYTICS-1314", "title": "Analytics scenario 1314", "data": {"sku": "SKU1314", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1314@example.com", "threshold": 140}},
    {"id": "ANALYTICS-1315", "title": "Analytics scenario 1315", "data": {"sku": "SKU1315", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1315@example.com", "threshold": 150}},
    {"id": "ANALYTICS-1316", "title": "Analytics scenario 1316", "data": {"sku": "SKU1316", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1316@example.com", "threshold": 160}},
    {"id": "ANALYTICS-1317", "title": "Analytics scenario 1317", "data": {"sku": "SKU1317", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1317@example.com", "threshold": 170}},
    {"id": "ANALYTICS-1318", "title": "Analytics scenario 1318", "data": {"sku": "SKU1318", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1318@example.com", "threshold": 180}},
    {"id": "ANALYTICS-1319", "title": "Analytics scenario 1319", "data": {"sku": "SKU1319", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1319@example.com", "threshold": 190}},
    {"id": "ANALYTICS-1320", "title": "Analytics scenario 1320", "data": {"sku": "SKU1320", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1320@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
