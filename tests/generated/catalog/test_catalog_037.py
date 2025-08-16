import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2171", "title": "Catalog scenario 2171", "data": {"sku": "SKU2171", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2171@example.com", "threshold": 710}},
    {"id": "CATALOG-2172", "title": "Catalog scenario 2172", "data": {"sku": "SKU2172", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2172@example.com", "threshold": 720}},
    {"id": "CATALOG-2173", "title": "Catalog scenario 2173", "data": {"sku": "SKU2173", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2173@example.com", "threshold": 730}},
    {"id": "CATALOG-2174", "title": "Catalog scenario 2174", "data": {"sku": "SKU2174", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2174@example.com", "threshold": 740}},
    {"id": "CATALOG-2175", "title": "Catalog scenario 2175", "data": {"sku": "SKU2175", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2175@example.com", "threshold": 750}},
    {"id": "CATALOG-2176", "title": "Catalog scenario 2176", "data": {"sku": "SKU2176", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2176@example.com", "threshold": 760}},
    {"id": "CATALOG-2177", "title": "Catalog scenario 2177", "data": {"sku": "SKU2177", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2177@example.com", "threshold": 770}},
    {"id": "CATALOG-2178", "title": "Catalog scenario 2178", "data": {"sku": "SKU2178", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2178@example.com", "threshold": 780}},
    {"id": "CATALOG-2179", "title": "Catalog scenario 2179", "data": {"sku": "SKU2179", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2179@example.com", "threshold": 790}},
    {"id": "CATALOG-2180", "title": "Catalog scenario 2180", "data": {"sku": "SKU2180", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2180@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
