import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1191", "title": "Analytics scenario 1191", "data": {"sku": "SKU1191", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1191@example.com", "threshold": 910}},
    {"id": "ANALYTICS-1192", "title": "Analytics scenario 1192", "data": {"sku": "SKU1192", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1192@example.com", "threshold": 920}},
    {"id": "ANALYTICS-1193", "title": "Analytics scenario 1193", "data": {"sku": "SKU1193", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1193@example.com", "threshold": 930}},
    {"id": "ANALYTICS-1194", "title": "Analytics scenario 1194", "data": {"sku": "SKU1194", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1194@example.com", "threshold": 940}},
    {"id": "ANALYTICS-1195", "title": "Analytics scenario 1195", "data": {"sku": "SKU1195", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1195@example.com", "threshold": 950}},
    {"id": "ANALYTICS-1196", "title": "Analytics scenario 1196", "data": {"sku": "SKU1196", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1196@example.com", "threshold": 960}},
    {"id": "ANALYTICS-1197", "title": "Analytics scenario 1197", "data": {"sku": "SKU1197", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1197@example.com", "threshold": 970}},
    {"id": "ANALYTICS-1198", "title": "Analytics scenario 1198", "data": {"sku": "SKU1198", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1198@example.com", "threshold": 980}},
    {"id": "ANALYTICS-1199", "title": "Analytics scenario 1199", "data": {"sku": "SKU1199", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1199@example.com", "threshold": 990}},
    {"id": "ANALYTICS-1200", "title": "Analytics scenario 1200", "data": {"sku": "SKU1200", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1200@example.com", "threshold": 0}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
