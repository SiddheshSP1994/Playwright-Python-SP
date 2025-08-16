import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-4671", "title": "Analytics scenario 4671", "data": {"sku": "SKU4671", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4671@example.com", "threshold": 710}},
    {"id": "ANALYTICS-4672", "title": "Analytics scenario 4672", "data": {"sku": "SKU4672", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4672@example.com", "threshold": 720}},
    {"id": "ANALYTICS-4673", "title": "Analytics scenario 4673", "data": {"sku": "SKU4673", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4673@example.com", "threshold": 730}},
    {"id": "ANALYTICS-4674", "title": "Analytics scenario 4674", "data": {"sku": "SKU4674", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4674@example.com", "threshold": 740}},
    {"id": "ANALYTICS-4675", "title": "Analytics scenario 4675", "data": {"sku": "SKU4675", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4675@example.com", "threshold": 750}},
    {"id": "ANALYTICS-4676", "title": "Analytics scenario 4676", "data": {"sku": "SKU4676", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4676@example.com", "threshold": 760}},
    {"id": "ANALYTICS-4677", "title": "Analytics scenario 4677", "data": {"sku": "SKU4677", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4677@example.com", "threshold": 770}},
    {"id": "ANALYTICS-4678", "title": "Analytics scenario 4678", "data": {"sku": "SKU4678", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4678@example.com", "threshold": 780}},
    {"id": "ANALYTICS-4679", "title": "Analytics scenario 4679", "data": {"sku": "SKU4679", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4679@example.com", "threshold": 790}},
    {"id": "ANALYTICS-4680", "title": "Analytics scenario 4680", "data": {"sku": "SKU4680", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4680@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
