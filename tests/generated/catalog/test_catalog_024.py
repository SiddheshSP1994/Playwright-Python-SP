import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1391", "title": "Catalog scenario 1391", "data": {"sku": "SKU1391", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1391@example.com", "threshold": 910}},
    {"id": "CATALOG-1392", "title": "Catalog scenario 1392", "data": {"sku": "SKU1392", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1392@example.com", "threshold": 920}},
    {"id": "CATALOG-1393", "title": "Catalog scenario 1393", "data": {"sku": "SKU1393", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1393@example.com", "threshold": 930}},
    {"id": "CATALOG-1394", "title": "Catalog scenario 1394", "data": {"sku": "SKU1394", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1394@example.com", "threshold": 940}},
    {"id": "CATALOG-1395", "title": "Catalog scenario 1395", "data": {"sku": "SKU1395", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1395@example.com", "threshold": 950}},
    {"id": "CATALOG-1396", "title": "Catalog scenario 1396", "data": {"sku": "SKU1396", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1396@example.com", "threshold": 960}},
    {"id": "CATALOG-1397", "title": "Catalog scenario 1397", "data": {"sku": "SKU1397", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1397@example.com", "threshold": 970}},
    {"id": "CATALOG-1398", "title": "Catalog scenario 1398", "data": {"sku": "SKU1398", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1398@example.com", "threshold": 980}},
    {"id": "CATALOG-1399", "title": "Catalog scenario 1399", "data": {"sku": "SKU1399", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1399@example.com", "threshold": 990}},
    {"id": "CATALOG-1400", "title": "Catalog scenario 1400", "data": {"sku": "SKU1400", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1400@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
