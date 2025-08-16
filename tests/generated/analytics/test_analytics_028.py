import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1671", "title": "Analytics scenario 1671", "data": {"sku": "SKU1671", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1671@example.com", "threshold": 710}},
    {"id": "ANALYTICS-1672", "title": "Analytics scenario 1672", "data": {"sku": "SKU1672", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1672@example.com", "threshold": 720}},
    {"id": "ANALYTICS-1673", "title": "Analytics scenario 1673", "data": {"sku": "SKU1673", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1673@example.com", "threshold": 730}},
    {"id": "ANALYTICS-1674", "title": "Analytics scenario 1674", "data": {"sku": "SKU1674", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1674@example.com", "threshold": 740}},
    {"id": "ANALYTICS-1675", "title": "Analytics scenario 1675", "data": {"sku": "SKU1675", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1675@example.com", "threshold": 750}},
    {"id": "ANALYTICS-1676", "title": "Analytics scenario 1676", "data": {"sku": "SKU1676", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1676@example.com", "threshold": 760}},
    {"id": "ANALYTICS-1677", "title": "Analytics scenario 1677", "data": {"sku": "SKU1677", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1677@example.com", "threshold": 770}},
    {"id": "ANALYTICS-1678", "title": "Analytics scenario 1678", "data": {"sku": "SKU1678", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1678@example.com", "threshold": 780}},
    {"id": "ANALYTICS-1679", "title": "Analytics scenario 1679", "data": {"sku": "SKU1679", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1679@example.com", "threshold": 790}},
    {"id": "ANALYTICS-1680", "title": "Analytics scenario 1680", "data": {"sku": "SKU1680", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1680@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
