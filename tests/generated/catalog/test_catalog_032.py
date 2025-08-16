import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1871", "title": "Catalog scenario 1871", "data": {"sku": "SKU1871", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1871@example.com", "threshold": 710}},
    {"id": "CATALOG-1872", "title": "Catalog scenario 1872", "data": {"sku": "SKU1872", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1872@example.com", "threshold": 720}},
    {"id": "CATALOG-1873", "title": "Catalog scenario 1873", "data": {"sku": "SKU1873", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1873@example.com", "threshold": 730}},
    {"id": "CATALOG-1874", "title": "Catalog scenario 1874", "data": {"sku": "SKU1874", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1874@example.com", "threshold": 740}},
    {"id": "CATALOG-1875", "title": "Catalog scenario 1875", "data": {"sku": "SKU1875", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1875@example.com", "threshold": 750}},
    {"id": "CATALOG-1876", "title": "Catalog scenario 1876", "data": {"sku": "SKU1876", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1876@example.com", "threshold": 760}},
    {"id": "CATALOG-1877", "title": "Catalog scenario 1877", "data": {"sku": "SKU1877", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1877@example.com", "threshold": 770}},
    {"id": "CATALOG-1878", "title": "Catalog scenario 1878", "data": {"sku": "SKU1878", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1878@example.com", "threshold": 780}},
    {"id": "CATALOG-1879", "title": "Catalog scenario 1879", "data": {"sku": "SKU1879", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1879@example.com", "threshold": 790}},
    {"id": "CATALOG-1880", "title": "Catalog scenario 1880", "data": {"sku": "SKU1880", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1880@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
