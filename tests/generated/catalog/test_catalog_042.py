import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2471", "title": "Catalog scenario 2471", "data": {"sku": "SKU2471", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2471@example.com", "threshold": 710}},
    {"id": "CATALOG-2472", "title": "Catalog scenario 2472", "data": {"sku": "SKU2472", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2472@example.com", "threshold": 720}},
    {"id": "CATALOG-2473", "title": "Catalog scenario 2473", "data": {"sku": "SKU2473", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2473@example.com", "threshold": 730}},
    {"id": "CATALOG-2474", "title": "Catalog scenario 2474", "data": {"sku": "SKU2474", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2474@example.com", "threshold": 740}},
    {"id": "CATALOG-2475", "title": "Catalog scenario 2475", "data": {"sku": "SKU2475", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2475@example.com", "threshold": 750}},
    {"id": "CATALOG-2476", "title": "Catalog scenario 2476", "data": {"sku": "SKU2476", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2476@example.com", "threshold": 760}},
    {"id": "CATALOG-2477", "title": "Catalog scenario 2477", "data": {"sku": "SKU2477", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2477@example.com", "threshold": 770}},
    {"id": "CATALOG-2478", "title": "Catalog scenario 2478", "data": {"sku": "SKU2478", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2478@example.com", "threshold": 780}},
    {"id": "CATALOG-2479", "title": "Catalog scenario 2479", "data": {"sku": "SKU2479", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2479@example.com", "threshold": 790}},
    {"id": "CATALOG-2480", "title": "Catalog scenario 2480", "data": {"sku": "SKU2480", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2480@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
