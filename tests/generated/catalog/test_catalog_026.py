import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1511", "title": "Catalog scenario 1511", "data": {"sku": "SKU1511", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1511@example.com", "threshold": 110}},
    {"id": "CATALOG-1512", "title": "Catalog scenario 1512", "data": {"sku": "SKU1512", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1512@example.com", "threshold": 120}},
    {"id": "CATALOG-1513", "title": "Catalog scenario 1513", "data": {"sku": "SKU1513", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1513@example.com", "threshold": 130}},
    {"id": "CATALOG-1514", "title": "Catalog scenario 1514", "data": {"sku": "SKU1514", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1514@example.com", "threshold": 140}},
    {"id": "CATALOG-1515", "title": "Catalog scenario 1515", "data": {"sku": "SKU1515", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1515@example.com", "threshold": 150}},
    {"id": "CATALOG-1516", "title": "Catalog scenario 1516", "data": {"sku": "SKU1516", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1516@example.com", "threshold": 160}},
    {"id": "CATALOG-1517", "title": "Catalog scenario 1517", "data": {"sku": "SKU1517", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1517@example.com", "threshold": 170}},
    {"id": "CATALOG-1518", "title": "Catalog scenario 1518", "data": {"sku": "SKU1518", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1518@example.com", "threshold": 180}},
    {"id": "CATALOG-1519", "title": "Catalog scenario 1519", "data": {"sku": "SKU1519", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1519@example.com", "threshold": 190}},
    {"id": "CATALOG-1520", "title": "Catalog scenario 1520", "data": {"sku": "SKU1520", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1520@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
