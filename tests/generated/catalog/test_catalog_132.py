import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-7871", "title": "Catalog scenario 7871", "data": {"sku": "SKU7871", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7871@example.com", "threshold": 710}},
    {"id": "CATALOG-7872", "title": "Catalog scenario 7872", "data": {"sku": "SKU7872", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7872@example.com", "threshold": 720}},
    {"id": "CATALOG-7873", "title": "Catalog scenario 7873", "data": {"sku": "SKU7873", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7873@example.com", "threshold": 730}},
    {"id": "CATALOG-7874", "title": "Catalog scenario 7874", "data": {"sku": "SKU7874", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7874@example.com", "threshold": 740}},
    {"id": "CATALOG-7875", "title": "Catalog scenario 7875", "data": {"sku": "SKU7875", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7875@example.com", "threshold": 750}},
    {"id": "CATALOG-7876", "title": "Catalog scenario 7876", "data": {"sku": "SKU7876", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7876@example.com", "threshold": 760}},
    {"id": "CATALOG-7877", "title": "Catalog scenario 7877", "data": {"sku": "SKU7877", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7877@example.com", "threshold": 770}},
    {"id": "CATALOG-7878", "title": "Catalog scenario 7878", "data": {"sku": "SKU7878", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7878@example.com", "threshold": 780}},
    {"id": "CATALOG-7879", "title": "Catalog scenario 7879", "data": {"sku": "SKU7879", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7879@example.com", "threshold": 790}},
    {"id": "CATALOG-7880", "title": "Catalog scenario 7880", "data": {"sku": "SKU7880", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7880@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
