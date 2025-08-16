import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8871", "title": "Analytics scenario 8871", "data": {"sku": "SKU8871", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8871@example.com", "threshold": 710}},
    {"id": "ANALYTICS-8872", "title": "Analytics scenario 8872", "data": {"sku": "SKU8872", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8872@example.com", "threshold": 720}},
    {"id": "ANALYTICS-8873", "title": "Analytics scenario 8873", "data": {"sku": "SKU8873", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8873@example.com", "threshold": 730}},
    {"id": "ANALYTICS-8874", "title": "Analytics scenario 8874", "data": {"sku": "SKU8874", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8874@example.com", "threshold": 740}},
    {"id": "ANALYTICS-8875", "title": "Analytics scenario 8875", "data": {"sku": "SKU8875", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8875@example.com", "threshold": 750}},
    {"id": "ANALYTICS-8876", "title": "Analytics scenario 8876", "data": {"sku": "SKU8876", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8876@example.com", "threshold": 760}},
    {"id": "ANALYTICS-8877", "title": "Analytics scenario 8877", "data": {"sku": "SKU8877", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8877@example.com", "threshold": 770}},
    {"id": "ANALYTICS-8878", "title": "Analytics scenario 8878", "data": {"sku": "SKU8878", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8878@example.com", "threshold": 780}},
    {"id": "ANALYTICS-8879", "title": "Analytics scenario 8879", "data": {"sku": "SKU8879", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8879@example.com", "threshold": 790}},
    {"id": "ANALYTICS-8880", "title": "Analytics scenario 8880", "data": {"sku": "SKU8880", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8880@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
