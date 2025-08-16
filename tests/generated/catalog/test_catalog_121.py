import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-7211", "title": "Catalog scenario 7211", "data": {"sku": "SKU7211", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7211@example.com", "threshold": 110}},
    {"id": "CATALOG-7212", "title": "Catalog scenario 7212", "data": {"sku": "SKU7212", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7212@example.com", "threshold": 120}},
    {"id": "CATALOG-7213", "title": "Catalog scenario 7213", "data": {"sku": "SKU7213", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7213@example.com", "threshold": 130}},
    {"id": "CATALOG-7214", "title": "Catalog scenario 7214", "data": {"sku": "SKU7214", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7214@example.com", "threshold": 140}},
    {"id": "CATALOG-7215", "title": "Catalog scenario 7215", "data": {"sku": "SKU7215", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7215@example.com", "threshold": 150}},
    {"id": "CATALOG-7216", "title": "Catalog scenario 7216", "data": {"sku": "SKU7216", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7216@example.com", "threshold": 160}},
    {"id": "CATALOG-7217", "title": "Catalog scenario 7217", "data": {"sku": "SKU7217", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7217@example.com", "threshold": 170}},
    {"id": "CATALOG-7218", "title": "Catalog scenario 7218", "data": {"sku": "SKU7218", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7218@example.com", "threshold": 180}},
    {"id": "CATALOG-7219", "title": "Catalog scenario 7219", "data": {"sku": "SKU7219", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7219@example.com", "threshold": 190}},
    {"id": "CATALOG-7220", "title": "Catalog scenario 7220", "data": {"sku": "SKU7220", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7220@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
