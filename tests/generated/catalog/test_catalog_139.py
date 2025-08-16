import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8291", "title": "Catalog scenario 8291", "data": {"sku": "SKU8291", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8291@example.com", "threshold": 910}},
    {"id": "CATALOG-8292", "title": "Catalog scenario 8292", "data": {"sku": "SKU8292", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8292@example.com", "threshold": 920}},
    {"id": "CATALOG-8293", "title": "Catalog scenario 8293", "data": {"sku": "SKU8293", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8293@example.com", "threshold": 930}},
    {"id": "CATALOG-8294", "title": "Catalog scenario 8294", "data": {"sku": "SKU8294", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8294@example.com", "threshold": 940}},
    {"id": "CATALOG-8295", "title": "Catalog scenario 8295", "data": {"sku": "SKU8295", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8295@example.com", "threshold": 950}},
    {"id": "CATALOG-8296", "title": "Catalog scenario 8296", "data": {"sku": "SKU8296", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8296@example.com", "threshold": 960}},
    {"id": "CATALOG-8297", "title": "Catalog scenario 8297", "data": {"sku": "SKU8297", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8297@example.com", "threshold": 970}},
    {"id": "CATALOG-8298", "title": "Catalog scenario 8298", "data": {"sku": "SKU8298", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8298@example.com", "threshold": 980}},
    {"id": "CATALOG-8299", "title": "Catalog scenario 8299", "data": {"sku": "SKU8299", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8299@example.com", "threshold": 990}},
    {"id": "CATALOG-8300", "title": "Catalog scenario 8300", "data": {"sku": "SKU8300", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8300@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
