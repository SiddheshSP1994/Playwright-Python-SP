import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-3111", "title": "Analytics scenario 3111", "data": {"sku": "SKU3111", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3111@example.com", "threshold": 110}},
    {"id": "ANALYTICS-3112", "title": "Analytics scenario 3112", "data": {"sku": "SKU3112", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3112@example.com", "threshold": 120}},
    {"id": "ANALYTICS-3113", "title": "Analytics scenario 3113", "data": {"sku": "SKU3113", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3113@example.com", "threshold": 130}},
    {"id": "ANALYTICS-3114", "title": "Analytics scenario 3114", "data": {"sku": "SKU3114", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3114@example.com", "threshold": 140}},
    {"id": "ANALYTICS-3115", "title": "Analytics scenario 3115", "data": {"sku": "SKU3115", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3115@example.com", "threshold": 150}},
    {"id": "ANALYTICS-3116", "title": "Analytics scenario 3116", "data": {"sku": "SKU3116", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3116@example.com", "threshold": 160}},
    {"id": "ANALYTICS-3117", "title": "Analytics scenario 3117", "data": {"sku": "SKU3117", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3117@example.com", "threshold": 170}},
    {"id": "ANALYTICS-3118", "title": "Analytics scenario 3118", "data": {"sku": "SKU3118", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3118@example.com", "threshold": 180}},
    {"id": "ANALYTICS-3119", "title": "Analytics scenario 3119", "data": {"sku": "SKU3119", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3119@example.com", "threshold": 190}},
    {"id": "ANALYTICS-3120", "title": "Analytics scenario 3120", "data": {"sku": "SKU3120", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3120@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
