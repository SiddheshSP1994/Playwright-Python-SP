import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-3171", "title": "Analytics scenario 3171", "data": {"sku": "SKU3171", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3171@example.com", "threshold": 710}},
    {"id": "ANALYTICS-3172", "title": "Analytics scenario 3172", "data": {"sku": "SKU3172", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3172@example.com", "threshold": 720}},
    {"id": "ANALYTICS-3173", "title": "Analytics scenario 3173", "data": {"sku": "SKU3173", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3173@example.com", "threshold": 730}},
    {"id": "ANALYTICS-3174", "title": "Analytics scenario 3174", "data": {"sku": "SKU3174", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3174@example.com", "threshold": 740}},
    {"id": "ANALYTICS-3175", "title": "Analytics scenario 3175", "data": {"sku": "SKU3175", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3175@example.com", "threshold": 750}},
    {"id": "ANALYTICS-3176", "title": "Analytics scenario 3176", "data": {"sku": "SKU3176", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3176@example.com", "threshold": 760}},
    {"id": "ANALYTICS-3177", "title": "Analytics scenario 3177", "data": {"sku": "SKU3177", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3177@example.com", "threshold": 770}},
    {"id": "ANALYTICS-3178", "title": "Analytics scenario 3178", "data": {"sku": "SKU3178", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3178@example.com", "threshold": 780}},
    {"id": "ANALYTICS-3179", "title": "Analytics scenario 3179", "data": {"sku": "SKU3179", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3179@example.com", "threshold": 790}},
    {"id": "ANALYTICS-3180", "title": "Analytics scenario 3180", "data": {"sku": "SKU3180", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3180@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
