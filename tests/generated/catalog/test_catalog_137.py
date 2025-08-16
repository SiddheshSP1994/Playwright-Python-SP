import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8171", "title": "Catalog scenario 8171", "data": {"sku": "SKU8171", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8171@example.com", "threshold": 710}},
    {"id": "CATALOG-8172", "title": "Catalog scenario 8172", "data": {"sku": "SKU8172", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8172@example.com", "threshold": 720}},
    {"id": "CATALOG-8173", "title": "Catalog scenario 8173", "data": {"sku": "SKU8173", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8173@example.com", "threshold": 730}},
    {"id": "CATALOG-8174", "title": "Catalog scenario 8174", "data": {"sku": "SKU8174", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8174@example.com", "threshold": 740}},
    {"id": "CATALOG-8175", "title": "Catalog scenario 8175", "data": {"sku": "SKU8175", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8175@example.com", "threshold": 750}},
    {"id": "CATALOG-8176", "title": "Catalog scenario 8176", "data": {"sku": "SKU8176", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8176@example.com", "threshold": 760}},
    {"id": "CATALOG-8177", "title": "Catalog scenario 8177", "data": {"sku": "SKU8177", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8177@example.com", "threshold": 770}},
    {"id": "CATALOG-8178", "title": "Catalog scenario 8178", "data": {"sku": "SKU8178", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8178@example.com", "threshold": 780}},
    {"id": "CATALOG-8179", "title": "Catalog scenario 8179", "data": {"sku": "SKU8179", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8179@example.com", "threshold": 790}},
    {"id": "CATALOG-8180", "title": "Catalog scenario 8180", "data": {"sku": "SKU8180", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8180@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
