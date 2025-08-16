import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1331", "title": "Catalog scenario 1331", "data": {"sku": "SKU1331", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1331@example.com", "threshold": 310}},
    {"id": "CATALOG-1332", "title": "Catalog scenario 1332", "data": {"sku": "SKU1332", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1332@example.com", "threshold": 320}},
    {"id": "CATALOG-1333", "title": "Catalog scenario 1333", "data": {"sku": "SKU1333", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1333@example.com", "threshold": 330}},
    {"id": "CATALOG-1334", "title": "Catalog scenario 1334", "data": {"sku": "SKU1334", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1334@example.com", "threshold": 340}},
    {"id": "CATALOG-1335", "title": "Catalog scenario 1335", "data": {"sku": "SKU1335", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1335@example.com", "threshold": 350}},
    {"id": "CATALOG-1336", "title": "Catalog scenario 1336", "data": {"sku": "SKU1336", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1336@example.com", "threshold": 360}},
    {"id": "CATALOG-1337", "title": "Catalog scenario 1337", "data": {"sku": "SKU1337", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1337@example.com", "threshold": 370}},
    {"id": "CATALOG-1338", "title": "Catalog scenario 1338", "data": {"sku": "SKU1338", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1338@example.com", "threshold": 380}},
    {"id": "CATALOG-1339", "title": "Catalog scenario 1339", "data": {"sku": "SKU1339", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1339@example.com", "threshold": 390}},
    {"id": "CATALOG-1340", "title": "Catalog scenario 1340", "data": {"sku": "SKU1340", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1340@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
