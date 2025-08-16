import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6071", "title": "Catalog scenario 6071", "data": {"sku": "SKU6071", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6071@example.com", "threshold": 710}},
    {"id": "CATALOG-6072", "title": "Catalog scenario 6072", "data": {"sku": "SKU6072", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6072@example.com", "threshold": 720}},
    {"id": "CATALOG-6073", "title": "Catalog scenario 6073", "data": {"sku": "SKU6073", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6073@example.com", "threshold": 730}},
    {"id": "CATALOG-6074", "title": "Catalog scenario 6074", "data": {"sku": "SKU6074", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6074@example.com", "threshold": 740}},
    {"id": "CATALOG-6075", "title": "Catalog scenario 6075", "data": {"sku": "SKU6075", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6075@example.com", "threshold": 750}},
    {"id": "CATALOG-6076", "title": "Catalog scenario 6076", "data": {"sku": "SKU6076", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6076@example.com", "threshold": 760}},
    {"id": "CATALOG-6077", "title": "Catalog scenario 6077", "data": {"sku": "SKU6077", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6077@example.com", "threshold": 770}},
    {"id": "CATALOG-6078", "title": "Catalog scenario 6078", "data": {"sku": "SKU6078", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6078@example.com", "threshold": 780}},
    {"id": "CATALOG-6079", "title": "Catalog scenario 6079", "data": {"sku": "SKU6079", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6079@example.com", "threshold": 790}},
    {"id": "CATALOG-6080", "title": "Catalog scenario 6080", "data": {"sku": "SKU6080", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6080@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
