import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3671", "title": "Catalog scenario 3671", "data": {"sku": "SKU3671", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3671@example.com", "threshold": 710}},
    {"id": "CATALOG-3672", "title": "Catalog scenario 3672", "data": {"sku": "SKU3672", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3672@example.com", "threshold": 720}},
    {"id": "CATALOG-3673", "title": "Catalog scenario 3673", "data": {"sku": "SKU3673", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3673@example.com", "threshold": 730}},
    {"id": "CATALOG-3674", "title": "Catalog scenario 3674", "data": {"sku": "SKU3674", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3674@example.com", "threshold": 740}},
    {"id": "CATALOG-3675", "title": "Catalog scenario 3675", "data": {"sku": "SKU3675", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3675@example.com", "threshold": 750}},
    {"id": "CATALOG-3676", "title": "Catalog scenario 3676", "data": {"sku": "SKU3676", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3676@example.com", "threshold": 760}},
    {"id": "CATALOG-3677", "title": "Catalog scenario 3677", "data": {"sku": "SKU3677", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3677@example.com", "threshold": 770}},
    {"id": "CATALOG-3678", "title": "Catalog scenario 3678", "data": {"sku": "SKU3678", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3678@example.com", "threshold": 780}},
    {"id": "CATALOG-3679", "title": "Catalog scenario 3679", "data": {"sku": "SKU3679", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3679@example.com", "threshold": 790}},
    {"id": "CATALOG-3680", "title": "Catalog scenario 3680", "data": {"sku": "SKU3680", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3680@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
