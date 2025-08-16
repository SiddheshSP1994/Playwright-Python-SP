import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2111", "title": "Catalog scenario 2111", "data": {"sku": "SKU2111", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2111@example.com", "threshold": 110}},
    {"id": "CATALOG-2112", "title": "Catalog scenario 2112", "data": {"sku": "SKU2112", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2112@example.com", "threshold": 120}},
    {"id": "CATALOG-2113", "title": "Catalog scenario 2113", "data": {"sku": "SKU2113", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2113@example.com", "threshold": 130}},
    {"id": "CATALOG-2114", "title": "Catalog scenario 2114", "data": {"sku": "SKU2114", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2114@example.com", "threshold": 140}},
    {"id": "CATALOG-2115", "title": "Catalog scenario 2115", "data": {"sku": "SKU2115", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2115@example.com", "threshold": 150}},
    {"id": "CATALOG-2116", "title": "Catalog scenario 2116", "data": {"sku": "SKU2116", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2116@example.com", "threshold": 160}},
    {"id": "CATALOG-2117", "title": "Catalog scenario 2117", "data": {"sku": "SKU2117", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2117@example.com", "threshold": 170}},
    {"id": "CATALOG-2118", "title": "Catalog scenario 2118", "data": {"sku": "SKU2118", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2118@example.com", "threshold": 180}},
    {"id": "CATALOG-2119", "title": "Catalog scenario 2119", "data": {"sku": "SKU2119", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2119@example.com", "threshold": 190}},
    {"id": "CATALOG-2120", "title": "Catalog scenario 2120", "data": {"sku": "SKU2120", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2120@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
