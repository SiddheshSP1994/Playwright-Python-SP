import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-0171", "title": "Analytics scenario 171", "data": {"sku": "SKU171", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user171@example.com", "threshold": 710}},
    {"id": "ANALYTICS-0172", "title": "Analytics scenario 172", "data": {"sku": "SKU172", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user172@example.com", "threshold": 720}},
    {"id": "ANALYTICS-0173", "title": "Analytics scenario 173", "data": {"sku": "SKU173", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user173@example.com", "threshold": 730}},
    {"id": "ANALYTICS-0174", "title": "Analytics scenario 174", "data": {"sku": "SKU174", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user174@example.com", "threshold": 740}},
    {"id": "ANALYTICS-0175", "title": "Analytics scenario 175", "data": {"sku": "SKU175", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user175@example.com", "threshold": 750}},
    {"id": "ANALYTICS-0176", "title": "Analytics scenario 176", "data": {"sku": "SKU176", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user176@example.com", "threshold": 760}},
    {"id": "ANALYTICS-0177", "title": "Analytics scenario 177", "data": {"sku": "SKU177", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user177@example.com", "threshold": 770}},
    {"id": "ANALYTICS-0178", "title": "Analytics scenario 178", "data": {"sku": "SKU178", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user178@example.com", "threshold": 780}},
    {"id": "ANALYTICS-0179", "title": "Analytics scenario 179", "data": {"sku": "SKU179", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user179@example.com", "threshold": 790}},
    {"id": "ANALYTICS-0180", "title": "Analytics scenario 180", "data": {"sku": "SKU180", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user180@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
