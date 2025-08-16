import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1371", "title": "Analytics scenario 1371", "data": {"sku": "SKU1371", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1371@example.com", "threshold": 710}},
    {"id": "ANALYTICS-1372", "title": "Analytics scenario 1372", "data": {"sku": "SKU1372", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1372@example.com", "threshold": 720}},
    {"id": "ANALYTICS-1373", "title": "Analytics scenario 1373", "data": {"sku": "SKU1373", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1373@example.com", "threshold": 730}},
    {"id": "ANALYTICS-1374", "title": "Analytics scenario 1374", "data": {"sku": "SKU1374", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1374@example.com", "threshold": 740}},
    {"id": "ANALYTICS-1375", "title": "Analytics scenario 1375", "data": {"sku": "SKU1375", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1375@example.com", "threshold": 750}},
    {"id": "ANALYTICS-1376", "title": "Analytics scenario 1376", "data": {"sku": "SKU1376", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1376@example.com", "threshold": 760}},
    {"id": "ANALYTICS-1377", "title": "Analytics scenario 1377", "data": {"sku": "SKU1377", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1377@example.com", "threshold": 770}},
    {"id": "ANALYTICS-1378", "title": "Analytics scenario 1378", "data": {"sku": "SKU1378", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1378@example.com", "threshold": 780}},
    {"id": "ANALYTICS-1379", "title": "Analytics scenario 1379", "data": {"sku": "SKU1379", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1379@example.com", "threshold": 790}},
    {"id": "ANALYTICS-1380", "title": "Analytics scenario 1380", "data": {"sku": "SKU1380", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1380@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
