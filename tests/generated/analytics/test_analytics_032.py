import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1911", "title": "Analytics scenario 1911", "data": {"sku": "SKU1911", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1911@example.com", "threshold": 110}},
    {"id": "ANALYTICS-1912", "title": "Analytics scenario 1912", "data": {"sku": "SKU1912", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1912@example.com", "threshold": 120}},
    {"id": "ANALYTICS-1913", "title": "Analytics scenario 1913", "data": {"sku": "SKU1913", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1913@example.com", "threshold": 130}},
    {"id": "ANALYTICS-1914", "title": "Analytics scenario 1914", "data": {"sku": "SKU1914", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1914@example.com", "threshold": 140}},
    {"id": "ANALYTICS-1915", "title": "Analytics scenario 1915", "data": {"sku": "SKU1915", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1915@example.com", "threshold": 150}},
    {"id": "ANALYTICS-1916", "title": "Analytics scenario 1916", "data": {"sku": "SKU1916", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1916@example.com", "threshold": 160}},
    {"id": "ANALYTICS-1917", "title": "Analytics scenario 1917", "data": {"sku": "SKU1917", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1917@example.com", "threshold": 170}},
    {"id": "ANALYTICS-1918", "title": "Analytics scenario 1918", "data": {"sku": "SKU1918", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1918@example.com", "threshold": 180}},
    {"id": "ANALYTICS-1919", "title": "Analytics scenario 1919", "data": {"sku": "SKU1919", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1919@example.com", "threshold": 190}},
    {"id": "ANALYTICS-1920", "title": "Analytics scenario 1920", "data": {"sku": "SKU1920", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1920@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
