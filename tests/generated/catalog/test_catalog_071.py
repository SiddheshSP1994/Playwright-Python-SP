import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4211", "title": "Catalog scenario 4211", "data": {"sku": "SKU4211", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4211@example.com", "threshold": 110}},
    {"id": "CATALOG-4212", "title": "Catalog scenario 4212", "data": {"sku": "SKU4212", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4212@example.com", "threshold": 120}},
    {"id": "CATALOG-4213", "title": "Catalog scenario 4213", "data": {"sku": "SKU4213", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4213@example.com", "threshold": 130}},
    {"id": "CATALOG-4214", "title": "Catalog scenario 4214", "data": {"sku": "SKU4214", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4214@example.com", "threshold": 140}},
    {"id": "CATALOG-4215", "title": "Catalog scenario 4215", "data": {"sku": "SKU4215", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4215@example.com", "threshold": 150}},
    {"id": "CATALOG-4216", "title": "Catalog scenario 4216", "data": {"sku": "SKU4216", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4216@example.com", "threshold": 160}},
    {"id": "CATALOG-4217", "title": "Catalog scenario 4217", "data": {"sku": "SKU4217", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4217@example.com", "threshold": 170}},
    {"id": "CATALOG-4218", "title": "Catalog scenario 4218", "data": {"sku": "SKU4218", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4218@example.com", "threshold": 180}},
    {"id": "CATALOG-4219", "title": "Catalog scenario 4219", "data": {"sku": "SKU4219", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4219@example.com", "threshold": 190}},
    {"id": "CATALOG-4220", "title": "Catalog scenario 4220", "data": {"sku": "SKU4220", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4220@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
