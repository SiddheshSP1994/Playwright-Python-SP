import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-2211", "title": "Analytics scenario 2211", "data": {"sku": "SKU2211", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2211@example.com", "threshold": 110}},
    {"id": "ANALYTICS-2212", "title": "Analytics scenario 2212", "data": {"sku": "SKU2212", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2212@example.com", "threshold": 120}},
    {"id": "ANALYTICS-2213", "title": "Analytics scenario 2213", "data": {"sku": "SKU2213", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2213@example.com", "threshold": 130}},
    {"id": "ANALYTICS-2214", "title": "Analytics scenario 2214", "data": {"sku": "SKU2214", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2214@example.com", "threshold": 140}},
    {"id": "ANALYTICS-2215", "title": "Analytics scenario 2215", "data": {"sku": "SKU2215", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2215@example.com", "threshold": 150}},
    {"id": "ANALYTICS-2216", "title": "Analytics scenario 2216", "data": {"sku": "SKU2216", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2216@example.com", "threshold": 160}},
    {"id": "ANALYTICS-2217", "title": "Analytics scenario 2217", "data": {"sku": "SKU2217", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2217@example.com", "threshold": 170}},
    {"id": "ANALYTICS-2218", "title": "Analytics scenario 2218", "data": {"sku": "SKU2218", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2218@example.com", "threshold": 180}},
    {"id": "ANALYTICS-2219", "title": "Analytics scenario 2219", "data": {"sku": "SKU2219", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2219@example.com", "threshold": 190}},
    {"id": "ANALYTICS-2220", "title": "Analytics scenario 2220", "data": {"sku": "SKU2220", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2220@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
