import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8471", "title": "Catalog scenario 8471", "data": {"sku": "SKU8471", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8471@example.com", "threshold": 710}},
    {"id": "CATALOG-8472", "title": "Catalog scenario 8472", "data": {"sku": "SKU8472", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8472@example.com", "threshold": 720}},
    {"id": "CATALOG-8473", "title": "Catalog scenario 8473", "data": {"sku": "SKU8473", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8473@example.com", "threshold": 730}},
    {"id": "CATALOG-8474", "title": "Catalog scenario 8474", "data": {"sku": "SKU8474", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8474@example.com", "threshold": 740}},
    {"id": "CATALOG-8475", "title": "Catalog scenario 8475", "data": {"sku": "SKU8475", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8475@example.com", "threshold": 750}},
    {"id": "CATALOG-8476", "title": "Catalog scenario 8476", "data": {"sku": "SKU8476", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8476@example.com", "threshold": 760}},
    {"id": "CATALOG-8477", "title": "Catalog scenario 8477", "data": {"sku": "SKU8477", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8477@example.com", "threshold": 770}},
    {"id": "CATALOG-8478", "title": "Catalog scenario 8478", "data": {"sku": "SKU8478", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8478@example.com", "threshold": 780}},
    {"id": "CATALOG-8479", "title": "Catalog scenario 8479", "data": {"sku": "SKU8479", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8479@example.com", "threshold": 790}},
    {"id": "CATALOG-8480", "title": "Catalog scenario 8480", "data": {"sku": "SKU8480", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8480@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
