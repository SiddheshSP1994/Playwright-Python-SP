import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6671", "title": "Catalog scenario 6671", "data": {"sku": "SKU6671", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6671@example.com", "threshold": 710}},
    {"id": "CATALOG-6672", "title": "Catalog scenario 6672", "data": {"sku": "SKU6672", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6672@example.com", "threshold": 720}},
    {"id": "CATALOG-6673", "title": "Catalog scenario 6673", "data": {"sku": "SKU6673", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6673@example.com", "threshold": 730}},
    {"id": "CATALOG-6674", "title": "Catalog scenario 6674", "data": {"sku": "SKU6674", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6674@example.com", "threshold": 740}},
    {"id": "CATALOG-6675", "title": "Catalog scenario 6675", "data": {"sku": "SKU6675", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6675@example.com", "threshold": 750}},
    {"id": "CATALOG-6676", "title": "Catalog scenario 6676", "data": {"sku": "SKU6676", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6676@example.com", "threshold": 760}},
    {"id": "CATALOG-6677", "title": "Catalog scenario 6677", "data": {"sku": "SKU6677", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6677@example.com", "threshold": 770}},
    {"id": "CATALOG-6678", "title": "Catalog scenario 6678", "data": {"sku": "SKU6678", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6678@example.com", "threshold": 780}},
    {"id": "CATALOG-6679", "title": "Catalog scenario 6679", "data": {"sku": "SKU6679", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6679@example.com", "threshold": 790}},
    {"id": "CATALOG-6680", "title": "Catalog scenario 6680", "data": {"sku": "SKU6680", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6680@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
