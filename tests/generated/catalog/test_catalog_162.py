import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-9671", "title": "Catalog scenario 9671", "data": {"sku": "SKU9671", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9671@example.com", "threshold": 710}},
    {"id": "CATALOG-9672", "title": "Catalog scenario 9672", "data": {"sku": "SKU9672", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9672@example.com", "threshold": 720}},
    {"id": "CATALOG-9673", "title": "Catalog scenario 9673", "data": {"sku": "SKU9673", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9673@example.com", "threshold": 730}},
    {"id": "CATALOG-9674", "title": "Catalog scenario 9674", "data": {"sku": "SKU9674", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9674@example.com", "threshold": 740}},
    {"id": "CATALOG-9675", "title": "Catalog scenario 9675", "data": {"sku": "SKU9675", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9675@example.com", "threshold": 750}},
    {"id": "CATALOG-9676", "title": "Catalog scenario 9676", "data": {"sku": "SKU9676", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9676@example.com", "threshold": 760}},
    {"id": "CATALOG-9677", "title": "Catalog scenario 9677", "data": {"sku": "SKU9677", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9677@example.com", "threshold": 770}},
    {"id": "CATALOG-9678", "title": "Catalog scenario 9678", "data": {"sku": "SKU9678", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9678@example.com", "threshold": 780}},
    {"id": "CATALOG-9679", "title": "Catalog scenario 9679", "data": {"sku": "SKU9679", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9679@example.com", "threshold": 790}},
    {"id": "CATALOG-9680", "title": "Catalog scenario 9680", "data": {"sku": "SKU9680", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9680@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
