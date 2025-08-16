import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-9311", "title": "Catalog scenario 9311", "data": {"sku": "SKU9311", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9311@example.com", "threshold": 110}},
    {"id": "CATALOG-9312", "title": "Catalog scenario 9312", "data": {"sku": "SKU9312", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9312@example.com", "threshold": 120}},
    {"id": "CATALOG-9313", "title": "Catalog scenario 9313", "data": {"sku": "SKU9313", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9313@example.com", "threshold": 130}},
    {"id": "CATALOG-9314", "title": "Catalog scenario 9314", "data": {"sku": "SKU9314", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9314@example.com", "threshold": 140}},
    {"id": "CATALOG-9315", "title": "Catalog scenario 9315", "data": {"sku": "SKU9315", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9315@example.com", "threshold": 150}},
    {"id": "CATALOG-9316", "title": "Catalog scenario 9316", "data": {"sku": "SKU9316", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9316@example.com", "threshold": 160}},
    {"id": "CATALOG-9317", "title": "Catalog scenario 9317", "data": {"sku": "SKU9317", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9317@example.com", "threshold": 170}},
    {"id": "CATALOG-9318", "title": "Catalog scenario 9318", "data": {"sku": "SKU9318", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9318@example.com", "threshold": 180}},
    {"id": "CATALOG-9319", "title": "Catalog scenario 9319", "data": {"sku": "SKU9319", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9319@example.com", "threshold": 190}},
    {"id": "CATALOG-9320", "title": "Catalog scenario 9320", "data": {"sku": "SKU9320", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9320@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
