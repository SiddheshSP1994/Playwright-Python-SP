import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8111", "title": "Catalog scenario 8111", "data": {"sku": "SKU8111", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8111@example.com", "threshold": 110}},
    {"id": "CATALOG-8112", "title": "Catalog scenario 8112", "data": {"sku": "SKU8112", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8112@example.com", "threshold": 120}},
    {"id": "CATALOG-8113", "title": "Catalog scenario 8113", "data": {"sku": "SKU8113", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8113@example.com", "threshold": 130}},
    {"id": "CATALOG-8114", "title": "Catalog scenario 8114", "data": {"sku": "SKU8114", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8114@example.com", "threshold": 140}},
    {"id": "CATALOG-8115", "title": "Catalog scenario 8115", "data": {"sku": "SKU8115", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8115@example.com", "threshold": 150}},
    {"id": "CATALOG-8116", "title": "Catalog scenario 8116", "data": {"sku": "SKU8116", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8116@example.com", "threshold": 160}},
    {"id": "CATALOG-8117", "title": "Catalog scenario 8117", "data": {"sku": "SKU8117", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8117@example.com", "threshold": 170}},
    {"id": "CATALOG-8118", "title": "Catalog scenario 8118", "data": {"sku": "SKU8118", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8118@example.com", "threshold": 180}},
    {"id": "CATALOG-8119", "title": "Catalog scenario 8119", "data": {"sku": "SKU8119", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8119@example.com", "threshold": 190}},
    {"id": "CATALOG-8120", "title": "Catalog scenario 8120", "data": {"sku": "SKU8120", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8120@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
