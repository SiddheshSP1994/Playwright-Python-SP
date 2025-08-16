import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1271", "title": "Catalog scenario 1271", "data": {"sku": "SKU1271", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1271@example.com", "threshold": 710}},
    {"id": "CATALOG-1272", "title": "Catalog scenario 1272", "data": {"sku": "SKU1272", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1272@example.com", "threshold": 720}},
    {"id": "CATALOG-1273", "title": "Catalog scenario 1273", "data": {"sku": "SKU1273", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1273@example.com", "threshold": 730}},
    {"id": "CATALOG-1274", "title": "Catalog scenario 1274", "data": {"sku": "SKU1274", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1274@example.com", "threshold": 740}},
    {"id": "CATALOG-1275", "title": "Catalog scenario 1275", "data": {"sku": "SKU1275", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1275@example.com", "threshold": 750}},
    {"id": "CATALOG-1276", "title": "Catalog scenario 1276", "data": {"sku": "SKU1276", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1276@example.com", "threshold": 760}},
    {"id": "CATALOG-1277", "title": "Catalog scenario 1277", "data": {"sku": "SKU1277", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1277@example.com", "threshold": 770}},
    {"id": "CATALOG-1278", "title": "Catalog scenario 1278", "data": {"sku": "SKU1278", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1278@example.com", "threshold": 780}},
    {"id": "CATALOG-1279", "title": "Catalog scenario 1279", "data": {"sku": "SKU1279", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1279@example.com", "threshold": 790}},
    {"id": "CATALOG-1280", "title": "Catalog scenario 1280", "data": {"sku": "SKU1280", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1280@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
