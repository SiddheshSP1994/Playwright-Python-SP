import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-5871", "title": "Analytics scenario 5871", "data": {"sku": "SKU5871", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5871@example.com", "threshold": 710}},
    {"id": "ANALYTICS-5872", "title": "Analytics scenario 5872", "data": {"sku": "SKU5872", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5872@example.com", "threshold": 720}},
    {"id": "ANALYTICS-5873", "title": "Analytics scenario 5873", "data": {"sku": "SKU5873", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5873@example.com", "threshold": 730}},
    {"id": "ANALYTICS-5874", "title": "Analytics scenario 5874", "data": {"sku": "SKU5874", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5874@example.com", "threshold": 740}},
    {"id": "ANALYTICS-5875", "title": "Analytics scenario 5875", "data": {"sku": "SKU5875", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5875@example.com", "threshold": 750}},
    {"id": "ANALYTICS-5876", "title": "Analytics scenario 5876", "data": {"sku": "SKU5876", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5876@example.com", "threshold": 760}},
    {"id": "ANALYTICS-5877", "title": "Analytics scenario 5877", "data": {"sku": "SKU5877", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5877@example.com", "threshold": 770}},
    {"id": "ANALYTICS-5878", "title": "Analytics scenario 5878", "data": {"sku": "SKU5878", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5878@example.com", "threshold": 780}},
    {"id": "ANALYTICS-5879", "title": "Analytics scenario 5879", "data": {"sku": "SKU5879", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5879@example.com", "threshold": 790}},
    {"id": "ANALYTICS-5880", "title": "Analytics scenario 5880", "data": {"sku": "SKU5880", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5880@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
