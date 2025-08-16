import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5171", "title": "Catalog scenario 5171", "data": {"sku": "SKU5171", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5171@example.com", "threshold": 710}},
    {"id": "CATALOG-5172", "title": "Catalog scenario 5172", "data": {"sku": "SKU5172", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5172@example.com", "threshold": 720}},
    {"id": "CATALOG-5173", "title": "Catalog scenario 5173", "data": {"sku": "SKU5173", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5173@example.com", "threshold": 730}},
    {"id": "CATALOG-5174", "title": "Catalog scenario 5174", "data": {"sku": "SKU5174", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5174@example.com", "threshold": 740}},
    {"id": "CATALOG-5175", "title": "Catalog scenario 5175", "data": {"sku": "SKU5175", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5175@example.com", "threshold": 750}},
    {"id": "CATALOG-5176", "title": "Catalog scenario 5176", "data": {"sku": "SKU5176", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5176@example.com", "threshold": 760}},
    {"id": "CATALOG-5177", "title": "Catalog scenario 5177", "data": {"sku": "SKU5177", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5177@example.com", "threshold": 770}},
    {"id": "CATALOG-5178", "title": "Catalog scenario 5178", "data": {"sku": "SKU5178", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5178@example.com", "threshold": 780}},
    {"id": "CATALOG-5179", "title": "Catalog scenario 5179", "data": {"sku": "SKU5179", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5179@example.com", "threshold": 790}},
    {"id": "CATALOG-5180", "title": "Catalog scenario 5180", "data": {"sku": "SKU5180", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5180@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
