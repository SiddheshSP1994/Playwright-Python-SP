import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3071", "title": "Catalog scenario 3071", "data": {"sku": "SKU3071", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3071@example.com", "threshold": 710}},
    {"id": "CATALOG-3072", "title": "Catalog scenario 3072", "data": {"sku": "SKU3072", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3072@example.com", "threshold": 720}},
    {"id": "CATALOG-3073", "title": "Catalog scenario 3073", "data": {"sku": "SKU3073", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3073@example.com", "threshold": 730}},
    {"id": "CATALOG-3074", "title": "Catalog scenario 3074", "data": {"sku": "SKU3074", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3074@example.com", "threshold": 740}},
    {"id": "CATALOG-3075", "title": "Catalog scenario 3075", "data": {"sku": "SKU3075", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3075@example.com", "threshold": 750}},
    {"id": "CATALOG-3076", "title": "Catalog scenario 3076", "data": {"sku": "SKU3076", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3076@example.com", "threshold": 760}},
    {"id": "CATALOG-3077", "title": "Catalog scenario 3077", "data": {"sku": "SKU3077", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3077@example.com", "threshold": 770}},
    {"id": "CATALOG-3078", "title": "Catalog scenario 3078", "data": {"sku": "SKU3078", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3078@example.com", "threshold": 780}},
    {"id": "CATALOG-3079", "title": "Catalog scenario 3079", "data": {"sku": "SKU3079", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3079@example.com", "threshold": 790}},
    {"id": "CATALOG-3080", "title": "Catalog scenario 3080", "data": {"sku": "SKU3080", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3080@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
