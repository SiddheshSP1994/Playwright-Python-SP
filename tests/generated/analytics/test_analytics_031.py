import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1851", "title": "Analytics scenario 1851", "data": {"sku": "SKU1851", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1851@example.com", "threshold": 510}},
    {"id": "ANALYTICS-1852", "title": "Analytics scenario 1852", "data": {"sku": "SKU1852", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1852@example.com", "threshold": 520}},
    {"id": "ANALYTICS-1853", "title": "Analytics scenario 1853", "data": {"sku": "SKU1853", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1853@example.com", "threshold": 530}},
    {"id": "ANALYTICS-1854", "title": "Analytics scenario 1854", "data": {"sku": "SKU1854", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1854@example.com", "threshold": 540}},
    {"id": "ANALYTICS-1855", "title": "Analytics scenario 1855", "data": {"sku": "SKU1855", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1855@example.com", "threshold": 550}},
    {"id": "ANALYTICS-1856", "title": "Analytics scenario 1856", "data": {"sku": "SKU1856", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1856@example.com", "threshold": 560}},
    {"id": "ANALYTICS-1857", "title": "Analytics scenario 1857", "data": {"sku": "SKU1857", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1857@example.com", "threshold": 570}},
    {"id": "ANALYTICS-1858", "title": "Analytics scenario 1858", "data": {"sku": "SKU1858", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1858@example.com", "threshold": 580}},
    {"id": "ANALYTICS-1859", "title": "Analytics scenario 1859", "data": {"sku": "SKU1859", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1859@example.com", "threshold": 590}},
    {"id": "ANALYTICS-1860", "title": "Analytics scenario 1860", "data": {"sku": "SKU1860", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1860@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
