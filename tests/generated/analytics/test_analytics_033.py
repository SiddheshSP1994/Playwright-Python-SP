import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1971", "title": "Analytics scenario 1971", "data": {"sku": "SKU1971", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1971@example.com", "threshold": 710}},
    {"id": "ANALYTICS-1972", "title": "Analytics scenario 1972", "data": {"sku": "SKU1972", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1972@example.com", "threshold": 720}},
    {"id": "ANALYTICS-1973", "title": "Analytics scenario 1973", "data": {"sku": "SKU1973", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1973@example.com", "threshold": 730}},
    {"id": "ANALYTICS-1974", "title": "Analytics scenario 1974", "data": {"sku": "SKU1974", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1974@example.com", "threshold": 740}},
    {"id": "ANALYTICS-1975", "title": "Analytics scenario 1975", "data": {"sku": "SKU1975", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1975@example.com", "threshold": 750}},
    {"id": "ANALYTICS-1976", "title": "Analytics scenario 1976", "data": {"sku": "SKU1976", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1976@example.com", "threshold": 760}},
    {"id": "ANALYTICS-1977", "title": "Analytics scenario 1977", "data": {"sku": "SKU1977", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1977@example.com", "threshold": 770}},
    {"id": "ANALYTICS-1978", "title": "Analytics scenario 1978", "data": {"sku": "SKU1978", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1978@example.com", "threshold": 780}},
    {"id": "ANALYTICS-1979", "title": "Analytics scenario 1979", "data": {"sku": "SKU1979", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1979@example.com", "threshold": 790}},
    {"id": "ANALYTICS-1980", "title": "Analytics scenario 1980", "data": {"sku": "SKU1980", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1980@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
