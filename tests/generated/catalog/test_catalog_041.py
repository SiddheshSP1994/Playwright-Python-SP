import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2411", "title": "Catalog scenario 2411", "data": {"sku": "SKU2411", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2411@example.com", "threshold": 110}},
    {"id": "CATALOG-2412", "title": "Catalog scenario 2412", "data": {"sku": "SKU2412", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2412@example.com", "threshold": 120}},
    {"id": "CATALOG-2413", "title": "Catalog scenario 2413", "data": {"sku": "SKU2413", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2413@example.com", "threshold": 130}},
    {"id": "CATALOG-2414", "title": "Catalog scenario 2414", "data": {"sku": "SKU2414", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2414@example.com", "threshold": 140}},
    {"id": "CATALOG-2415", "title": "Catalog scenario 2415", "data": {"sku": "SKU2415", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2415@example.com", "threshold": 150}},
    {"id": "CATALOG-2416", "title": "Catalog scenario 2416", "data": {"sku": "SKU2416", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2416@example.com", "threshold": 160}},
    {"id": "CATALOG-2417", "title": "Catalog scenario 2417", "data": {"sku": "SKU2417", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2417@example.com", "threshold": 170}},
    {"id": "CATALOG-2418", "title": "Catalog scenario 2418", "data": {"sku": "SKU2418", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2418@example.com", "threshold": 180}},
    {"id": "CATALOG-2419", "title": "Catalog scenario 2419", "data": {"sku": "SKU2419", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2419@example.com", "threshold": 190}},
    {"id": "CATALOG-2420", "title": "Catalog scenario 2420", "data": {"sku": "SKU2420", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2420@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
