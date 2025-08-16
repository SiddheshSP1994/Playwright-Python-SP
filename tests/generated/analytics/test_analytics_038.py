import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-2271", "title": "Analytics scenario 2271", "data": {"sku": "SKU2271", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2271@example.com", "threshold": 710}},
    {"id": "ANALYTICS-2272", "title": "Analytics scenario 2272", "data": {"sku": "SKU2272", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2272@example.com", "threshold": 720}},
    {"id": "ANALYTICS-2273", "title": "Analytics scenario 2273", "data": {"sku": "SKU2273", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2273@example.com", "threshold": 730}},
    {"id": "ANALYTICS-2274", "title": "Analytics scenario 2274", "data": {"sku": "SKU2274", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2274@example.com", "threshold": 740}},
    {"id": "ANALYTICS-2275", "title": "Analytics scenario 2275", "data": {"sku": "SKU2275", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2275@example.com", "threshold": 750}},
    {"id": "ANALYTICS-2276", "title": "Analytics scenario 2276", "data": {"sku": "SKU2276", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2276@example.com", "threshold": 760}},
    {"id": "ANALYTICS-2277", "title": "Analytics scenario 2277", "data": {"sku": "SKU2277", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2277@example.com", "threshold": 770}},
    {"id": "ANALYTICS-2278", "title": "Analytics scenario 2278", "data": {"sku": "SKU2278", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2278@example.com", "threshold": 780}},
    {"id": "ANALYTICS-2279", "title": "Analytics scenario 2279", "data": {"sku": "SKU2279", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2279@example.com", "threshold": 790}},
    {"id": "ANALYTICS-2280", "title": "Analytics scenario 2280", "data": {"sku": "SKU2280", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2280@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
