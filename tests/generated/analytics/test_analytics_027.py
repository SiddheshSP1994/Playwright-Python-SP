import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1611", "title": "Analytics scenario 1611", "data": {"sku": "SKU1611", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1611@example.com", "threshold": 110}},
    {"id": "ANALYTICS-1612", "title": "Analytics scenario 1612", "data": {"sku": "SKU1612", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1612@example.com", "threshold": 120}},
    {"id": "ANALYTICS-1613", "title": "Analytics scenario 1613", "data": {"sku": "SKU1613", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1613@example.com", "threshold": 130}},
    {"id": "ANALYTICS-1614", "title": "Analytics scenario 1614", "data": {"sku": "SKU1614", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1614@example.com", "threshold": 140}},
    {"id": "ANALYTICS-1615", "title": "Analytics scenario 1615", "data": {"sku": "SKU1615", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1615@example.com", "threshold": 150}},
    {"id": "ANALYTICS-1616", "title": "Analytics scenario 1616", "data": {"sku": "SKU1616", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1616@example.com", "threshold": 160}},
    {"id": "ANALYTICS-1617", "title": "Analytics scenario 1617", "data": {"sku": "SKU1617", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1617@example.com", "threshold": 170}},
    {"id": "ANALYTICS-1618", "title": "Analytics scenario 1618", "data": {"sku": "SKU1618", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1618@example.com", "threshold": 180}},
    {"id": "ANALYTICS-1619", "title": "Analytics scenario 1619", "data": {"sku": "SKU1619", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1619@example.com", "threshold": 190}},
    {"id": "ANALYTICS-1620", "title": "Analytics scenario 1620", "data": {"sku": "SKU1620", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1620@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
