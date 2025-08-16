import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1731", "title": "Analytics scenario 1731", "data": {"sku": "SKU1731", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1731@example.com", "threshold": 310}},
    {"id": "ANALYTICS-1732", "title": "Analytics scenario 1732", "data": {"sku": "SKU1732", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1732@example.com", "threshold": 320}},
    {"id": "ANALYTICS-1733", "title": "Analytics scenario 1733", "data": {"sku": "SKU1733", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1733@example.com", "threshold": 330}},
    {"id": "ANALYTICS-1734", "title": "Analytics scenario 1734", "data": {"sku": "SKU1734", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1734@example.com", "threshold": 340}},
    {"id": "ANALYTICS-1735", "title": "Analytics scenario 1735", "data": {"sku": "SKU1735", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1735@example.com", "threshold": 350}},
    {"id": "ANALYTICS-1736", "title": "Analytics scenario 1736", "data": {"sku": "SKU1736", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1736@example.com", "threshold": 360}},
    {"id": "ANALYTICS-1737", "title": "Analytics scenario 1737", "data": {"sku": "SKU1737", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1737@example.com", "threshold": 370}},
    {"id": "ANALYTICS-1738", "title": "Analytics scenario 1738", "data": {"sku": "SKU1738", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1738@example.com", "threshold": 380}},
    {"id": "ANALYTICS-1739", "title": "Analytics scenario 1739", "data": {"sku": "SKU1739", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1739@example.com", "threshold": 390}},
    {"id": "ANALYTICS-1740", "title": "Analytics scenario 1740", "data": {"sku": "SKU1740", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1740@example.com", "threshold": 400}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
