import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-2871", "title": "Analytics scenario 2871", "data": {"sku": "SKU2871", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2871@example.com", "threshold": 710}},
    {"id": "ANALYTICS-2872", "title": "Analytics scenario 2872", "data": {"sku": "SKU2872", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2872@example.com", "threshold": 720}},
    {"id": "ANALYTICS-2873", "title": "Analytics scenario 2873", "data": {"sku": "SKU2873", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2873@example.com", "threshold": 730}},
    {"id": "ANALYTICS-2874", "title": "Analytics scenario 2874", "data": {"sku": "SKU2874", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2874@example.com", "threshold": 740}},
    {"id": "ANALYTICS-2875", "title": "Analytics scenario 2875", "data": {"sku": "SKU2875", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2875@example.com", "threshold": 750}},
    {"id": "ANALYTICS-2876", "title": "Analytics scenario 2876", "data": {"sku": "SKU2876", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2876@example.com", "threshold": 760}},
    {"id": "ANALYTICS-2877", "title": "Analytics scenario 2877", "data": {"sku": "SKU2877", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2877@example.com", "threshold": 770}},
    {"id": "ANALYTICS-2878", "title": "Analytics scenario 2878", "data": {"sku": "SKU2878", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2878@example.com", "threshold": 780}},
    {"id": "ANALYTICS-2879", "title": "Analytics scenario 2879", "data": {"sku": "SKU2879", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2879@example.com", "threshold": 790}},
    {"id": "ANALYTICS-2880", "title": "Analytics scenario 2880", "data": {"sku": "SKU2880", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2880@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
