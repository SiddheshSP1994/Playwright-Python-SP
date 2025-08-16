import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-4251", "title": "Analytics scenario 4251", "data": {"sku": "SKU4251", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4251@example.com", "threshold": 510}},
    {"id": "ANALYTICS-4252", "title": "Analytics scenario 4252", "data": {"sku": "SKU4252", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4252@example.com", "threshold": 520}},
    {"id": "ANALYTICS-4253", "title": "Analytics scenario 4253", "data": {"sku": "SKU4253", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4253@example.com", "threshold": 530}},
    {"id": "ANALYTICS-4254", "title": "Analytics scenario 4254", "data": {"sku": "SKU4254", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4254@example.com", "threshold": 540}},
    {"id": "ANALYTICS-4255", "title": "Analytics scenario 4255", "data": {"sku": "SKU4255", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4255@example.com", "threshold": 550}},
    {"id": "ANALYTICS-4256", "title": "Analytics scenario 4256", "data": {"sku": "SKU4256", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4256@example.com", "threshold": 560}},
    {"id": "ANALYTICS-4257", "title": "Analytics scenario 4257", "data": {"sku": "SKU4257", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4257@example.com", "threshold": 570}},
    {"id": "ANALYTICS-4258", "title": "Analytics scenario 4258", "data": {"sku": "SKU4258", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4258@example.com", "threshold": 580}},
    {"id": "ANALYTICS-4259", "title": "Analytics scenario 4259", "data": {"sku": "SKU4259", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4259@example.com", "threshold": 590}},
    {"id": "ANALYTICS-4260", "title": "Analytics scenario 4260", "data": {"sku": "SKU4260", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4260@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
