import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1211", "title": "Catalog scenario 1211", "data": {"sku": "SKU1211", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1211@example.com", "threshold": 110}},
    {"id": "CATALOG-1212", "title": "Catalog scenario 1212", "data": {"sku": "SKU1212", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1212@example.com", "threshold": 120}},
    {"id": "CATALOG-1213", "title": "Catalog scenario 1213", "data": {"sku": "SKU1213", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1213@example.com", "threshold": 130}},
    {"id": "CATALOG-1214", "title": "Catalog scenario 1214", "data": {"sku": "SKU1214", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1214@example.com", "threshold": 140}},
    {"id": "CATALOG-1215", "title": "Catalog scenario 1215", "data": {"sku": "SKU1215", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1215@example.com", "threshold": 150}},
    {"id": "CATALOG-1216", "title": "Catalog scenario 1216", "data": {"sku": "SKU1216", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1216@example.com", "threshold": 160}},
    {"id": "CATALOG-1217", "title": "Catalog scenario 1217", "data": {"sku": "SKU1217", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1217@example.com", "threshold": 170}},
    {"id": "CATALOG-1218", "title": "Catalog scenario 1218", "data": {"sku": "SKU1218", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1218@example.com", "threshold": 180}},
    {"id": "CATALOG-1219", "title": "Catalog scenario 1219", "data": {"sku": "SKU1219", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1219@example.com", "threshold": 190}},
    {"id": "CATALOG-1220", "title": "Catalog scenario 1220", "data": {"sku": "SKU1220", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1220@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
