import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1491", "title": "Analytics scenario 1491", "data": {"sku": "SKU1491", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1491@example.com", "threshold": 910}},
    {"id": "ANALYTICS-1492", "title": "Analytics scenario 1492", "data": {"sku": "SKU1492", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1492@example.com", "threshold": 920}},
    {"id": "ANALYTICS-1493", "title": "Analytics scenario 1493", "data": {"sku": "SKU1493", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1493@example.com", "threshold": 930}},
    {"id": "ANALYTICS-1494", "title": "Analytics scenario 1494", "data": {"sku": "SKU1494", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1494@example.com", "threshold": 940}},
    {"id": "ANALYTICS-1495", "title": "Analytics scenario 1495", "data": {"sku": "SKU1495", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1495@example.com", "threshold": 950}},
    {"id": "ANALYTICS-1496", "title": "Analytics scenario 1496", "data": {"sku": "SKU1496", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1496@example.com", "threshold": 960}},
    {"id": "ANALYTICS-1497", "title": "Analytics scenario 1497", "data": {"sku": "SKU1497", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1497@example.com", "threshold": 970}},
    {"id": "ANALYTICS-1498", "title": "Analytics scenario 1498", "data": {"sku": "SKU1498", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1498@example.com", "threshold": 980}},
    {"id": "ANALYTICS-1499", "title": "Analytics scenario 1499", "data": {"sku": "SKU1499", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1499@example.com", "threshold": 990}},
    {"id": "ANALYTICS-1500", "title": "Analytics scenario 1500", "data": {"sku": "SKU1500", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1500@example.com", "threshold": 0}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
