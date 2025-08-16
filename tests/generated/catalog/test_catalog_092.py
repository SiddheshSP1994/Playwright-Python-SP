import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5471", "title": "Catalog scenario 5471", "data": {"sku": "SKU5471", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5471@example.com", "threshold": 710}},
    {"id": "CATALOG-5472", "title": "Catalog scenario 5472", "data": {"sku": "SKU5472", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5472@example.com", "threshold": 720}},
    {"id": "CATALOG-5473", "title": "Catalog scenario 5473", "data": {"sku": "SKU5473", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5473@example.com", "threshold": 730}},
    {"id": "CATALOG-5474", "title": "Catalog scenario 5474", "data": {"sku": "SKU5474", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5474@example.com", "threshold": 740}},
    {"id": "CATALOG-5475", "title": "Catalog scenario 5475", "data": {"sku": "SKU5475", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5475@example.com", "threshold": 750}},
    {"id": "CATALOG-5476", "title": "Catalog scenario 5476", "data": {"sku": "SKU5476", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5476@example.com", "threshold": 760}},
    {"id": "CATALOG-5477", "title": "Catalog scenario 5477", "data": {"sku": "SKU5477", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5477@example.com", "threshold": 770}},
    {"id": "CATALOG-5478", "title": "Catalog scenario 5478", "data": {"sku": "SKU5478", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5478@example.com", "threshold": 780}},
    {"id": "CATALOG-5479", "title": "Catalog scenario 5479", "data": {"sku": "SKU5479", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5479@example.com", "threshold": 790}},
    {"id": "CATALOG-5480", "title": "Catalog scenario 5480", "data": {"sku": "SKU5480", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5480@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
