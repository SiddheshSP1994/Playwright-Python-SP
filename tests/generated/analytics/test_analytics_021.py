import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1251", "title": "Analytics scenario 1251", "data": {"sku": "SKU1251", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1251@example.com", "threshold": 510}},
    {"id": "ANALYTICS-1252", "title": "Analytics scenario 1252", "data": {"sku": "SKU1252", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1252@example.com", "threshold": 520}},
    {"id": "ANALYTICS-1253", "title": "Analytics scenario 1253", "data": {"sku": "SKU1253", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1253@example.com", "threshold": 530}},
    {"id": "ANALYTICS-1254", "title": "Analytics scenario 1254", "data": {"sku": "SKU1254", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1254@example.com", "threshold": 540}},
    {"id": "ANALYTICS-1255", "title": "Analytics scenario 1255", "data": {"sku": "SKU1255", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1255@example.com", "threshold": 550}},
    {"id": "ANALYTICS-1256", "title": "Analytics scenario 1256", "data": {"sku": "SKU1256", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1256@example.com", "threshold": 560}},
    {"id": "ANALYTICS-1257", "title": "Analytics scenario 1257", "data": {"sku": "SKU1257", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1257@example.com", "threshold": 570}},
    {"id": "ANALYTICS-1258", "title": "Analytics scenario 1258", "data": {"sku": "SKU1258", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1258@example.com", "threshold": 580}},
    {"id": "ANALYTICS-1259", "title": "Analytics scenario 1259", "data": {"sku": "SKU1259", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1259@example.com", "threshold": 590}},
    {"id": "ANALYTICS-1260", "title": "Analytics scenario 1260", "data": {"sku": "SKU1260", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1260@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
