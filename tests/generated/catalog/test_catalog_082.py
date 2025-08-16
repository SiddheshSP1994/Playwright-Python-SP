import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4871", "title": "Catalog scenario 4871", "data": {"sku": "SKU4871", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4871@example.com", "threshold": 710}},
    {"id": "CATALOG-4872", "title": "Catalog scenario 4872", "data": {"sku": "SKU4872", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4872@example.com", "threshold": 720}},
    {"id": "CATALOG-4873", "title": "Catalog scenario 4873", "data": {"sku": "SKU4873", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4873@example.com", "threshold": 730}},
    {"id": "CATALOG-4874", "title": "Catalog scenario 4874", "data": {"sku": "SKU4874", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4874@example.com", "threshold": 740}},
    {"id": "CATALOG-4875", "title": "Catalog scenario 4875", "data": {"sku": "SKU4875", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4875@example.com", "threshold": 750}},
    {"id": "CATALOG-4876", "title": "Catalog scenario 4876", "data": {"sku": "SKU4876", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4876@example.com", "threshold": 760}},
    {"id": "CATALOG-4877", "title": "Catalog scenario 4877", "data": {"sku": "SKU4877", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4877@example.com", "threshold": 770}},
    {"id": "CATALOG-4878", "title": "Catalog scenario 4878", "data": {"sku": "SKU4878", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4878@example.com", "threshold": 780}},
    {"id": "CATALOG-4879", "title": "Catalog scenario 4879", "data": {"sku": "SKU4879", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4879@example.com", "threshold": 790}},
    {"id": "CATALOG-4880", "title": "Catalog scenario 4880", "data": {"sku": "SKU4880", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4880@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
