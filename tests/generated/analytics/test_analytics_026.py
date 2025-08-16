import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1551", "title": "Analytics scenario 1551", "data": {"sku": "SKU1551", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1551@example.com", "threshold": 510}},
    {"id": "ANALYTICS-1552", "title": "Analytics scenario 1552", "data": {"sku": "SKU1552", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1552@example.com", "threshold": 520}},
    {"id": "ANALYTICS-1553", "title": "Analytics scenario 1553", "data": {"sku": "SKU1553", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1553@example.com", "threshold": 530}},
    {"id": "ANALYTICS-1554", "title": "Analytics scenario 1554", "data": {"sku": "SKU1554", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1554@example.com", "threshold": 540}},
    {"id": "ANALYTICS-1555", "title": "Analytics scenario 1555", "data": {"sku": "SKU1555", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1555@example.com", "threshold": 550}},
    {"id": "ANALYTICS-1556", "title": "Analytics scenario 1556", "data": {"sku": "SKU1556", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1556@example.com", "threshold": 560}},
    {"id": "ANALYTICS-1557", "title": "Analytics scenario 1557", "data": {"sku": "SKU1557", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1557@example.com", "threshold": 570}},
    {"id": "ANALYTICS-1558", "title": "Analytics scenario 1558", "data": {"sku": "SKU1558", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1558@example.com", "threshold": 580}},
    {"id": "ANALYTICS-1559", "title": "Analytics scenario 1559", "data": {"sku": "SKU1559", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1559@example.com", "threshold": 590}},
    {"id": "ANALYTICS-1560", "title": "Analytics scenario 1560", "data": {"sku": "SKU1560", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1560@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
