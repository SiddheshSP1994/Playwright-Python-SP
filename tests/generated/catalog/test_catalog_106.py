import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6311", "title": "Catalog scenario 6311", "data": {"sku": "SKU6311", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6311@example.com", "threshold": 110}},
    {"id": "CATALOG-6312", "title": "Catalog scenario 6312", "data": {"sku": "SKU6312", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6312@example.com", "threshold": 120}},
    {"id": "CATALOG-6313", "title": "Catalog scenario 6313", "data": {"sku": "SKU6313", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6313@example.com", "threshold": 130}},
    {"id": "CATALOG-6314", "title": "Catalog scenario 6314", "data": {"sku": "SKU6314", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6314@example.com", "threshold": 140}},
    {"id": "CATALOG-6315", "title": "Catalog scenario 6315", "data": {"sku": "SKU6315", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6315@example.com", "threshold": 150}},
    {"id": "CATALOG-6316", "title": "Catalog scenario 6316", "data": {"sku": "SKU6316", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6316@example.com", "threshold": 160}},
    {"id": "CATALOG-6317", "title": "Catalog scenario 6317", "data": {"sku": "SKU6317", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6317@example.com", "threshold": 170}},
    {"id": "CATALOG-6318", "title": "Catalog scenario 6318", "data": {"sku": "SKU6318", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6318@example.com", "threshold": 180}},
    {"id": "CATALOG-6319", "title": "Catalog scenario 6319", "data": {"sku": "SKU6319", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6319@example.com", "threshold": 190}},
    {"id": "CATALOG-6320", "title": "Catalog scenario 6320", "data": {"sku": "SKU6320", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6320@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
