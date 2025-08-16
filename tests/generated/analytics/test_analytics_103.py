import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-6171", "title": "Analytics scenario 6171", "data": {"sku": "SKU6171", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6171@example.com", "threshold": 710}},
    {"id": "ANALYTICS-6172", "title": "Analytics scenario 6172", "data": {"sku": "SKU6172", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6172@example.com", "threshold": 720}},
    {"id": "ANALYTICS-6173", "title": "Analytics scenario 6173", "data": {"sku": "SKU6173", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6173@example.com", "threshold": 730}},
    {"id": "ANALYTICS-6174", "title": "Analytics scenario 6174", "data": {"sku": "SKU6174", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6174@example.com", "threshold": 740}},
    {"id": "ANALYTICS-6175", "title": "Analytics scenario 6175", "data": {"sku": "SKU6175", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6175@example.com", "threshold": 750}},
    {"id": "ANALYTICS-6176", "title": "Analytics scenario 6176", "data": {"sku": "SKU6176", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6176@example.com", "threshold": 760}},
    {"id": "ANALYTICS-6177", "title": "Analytics scenario 6177", "data": {"sku": "SKU6177", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6177@example.com", "threshold": 770}},
    {"id": "ANALYTICS-6178", "title": "Analytics scenario 6178", "data": {"sku": "SKU6178", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6178@example.com", "threshold": 780}},
    {"id": "ANALYTICS-6179", "title": "Analytics scenario 6179", "data": {"sku": "SKU6179", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6179@example.com", "threshold": 790}},
    {"id": "ANALYTICS-6180", "title": "Analytics scenario 6180", "data": {"sku": "SKU6180", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6180@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
