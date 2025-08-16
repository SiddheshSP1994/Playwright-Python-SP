import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1451", "title": "Catalog scenario 1451", "data": {"sku": "SKU1451", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1451@example.com", "threshold": 510}},
    {"id": "CATALOG-1452", "title": "Catalog scenario 1452", "data": {"sku": "SKU1452", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1452@example.com", "threshold": 520}},
    {"id": "CATALOG-1453", "title": "Catalog scenario 1453", "data": {"sku": "SKU1453", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1453@example.com", "threshold": 530}},
    {"id": "CATALOG-1454", "title": "Catalog scenario 1454", "data": {"sku": "SKU1454", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1454@example.com", "threshold": 540}},
    {"id": "CATALOG-1455", "title": "Catalog scenario 1455", "data": {"sku": "SKU1455", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1455@example.com", "threshold": 550}},
    {"id": "CATALOG-1456", "title": "Catalog scenario 1456", "data": {"sku": "SKU1456", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1456@example.com", "threshold": 560}},
    {"id": "CATALOG-1457", "title": "Catalog scenario 1457", "data": {"sku": "SKU1457", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1457@example.com", "threshold": 570}},
    {"id": "CATALOG-1458", "title": "Catalog scenario 1458", "data": {"sku": "SKU1458", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1458@example.com", "threshold": 580}},
    {"id": "CATALOG-1459", "title": "Catalog scenario 1459", "data": {"sku": "SKU1459", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1459@example.com", "threshold": 590}},
    {"id": "CATALOG-1460", "title": "Catalog scenario 1460", "data": {"sku": "SKU1460", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1460@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
