import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3311", "title": "Catalog scenario 3311", "data": {"sku": "SKU3311", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3311@example.com", "threshold": 110}},
    {"id": "CATALOG-3312", "title": "Catalog scenario 3312", "data": {"sku": "SKU3312", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3312@example.com", "threshold": 120}},
    {"id": "CATALOG-3313", "title": "Catalog scenario 3313", "data": {"sku": "SKU3313", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3313@example.com", "threshold": 130}},
    {"id": "CATALOG-3314", "title": "Catalog scenario 3314", "data": {"sku": "SKU3314", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3314@example.com", "threshold": 140}},
    {"id": "CATALOG-3315", "title": "Catalog scenario 3315", "data": {"sku": "SKU3315", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3315@example.com", "threshold": 150}},
    {"id": "CATALOG-3316", "title": "Catalog scenario 3316", "data": {"sku": "SKU3316", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3316@example.com", "threshold": 160}},
    {"id": "CATALOG-3317", "title": "Catalog scenario 3317", "data": {"sku": "SKU3317", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3317@example.com", "threshold": 170}},
    {"id": "CATALOG-3318", "title": "Catalog scenario 3318", "data": {"sku": "SKU3318", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3318@example.com", "threshold": 180}},
    {"id": "CATALOG-3319", "title": "Catalog scenario 3319", "data": {"sku": "SKU3319", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3319@example.com", "threshold": 190}},
    {"id": "CATALOG-3320", "title": "Catalog scenario 3320", "data": {"sku": "SKU3320", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3320@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
