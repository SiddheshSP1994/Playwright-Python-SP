import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-9371", "title": "Catalog scenario 9371", "data": {"sku": "SKU9371", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9371@example.com", "threshold": 710}},
    {"id": "CATALOG-9372", "title": "Catalog scenario 9372", "data": {"sku": "SKU9372", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9372@example.com", "threshold": 720}},
    {"id": "CATALOG-9373", "title": "Catalog scenario 9373", "data": {"sku": "SKU9373", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9373@example.com", "threshold": 730}},
    {"id": "CATALOG-9374", "title": "Catalog scenario 9374", "data": {"sku": "SKU9374", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9374@example.com", "threshold": 740}},
    {"id": "CATALOG-9375", "title": "Catalog scenario 9375", "data": {"sku": "SKU9375", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9375@example.com", "threshold": 750}},
    {"id": "CATALOG-9376", "title": "Catalog scenario 9376", "data": {"sku": "SKU9376", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9376@example.com", "threshold": 760}},
    {"id": "CATALOG-9377", "title": "Catalog scenario 9377", "data": {"sku": "SKU9377", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9377@example.com", "threshold": 770}},
    {"id": "CATALOG-9378", "title": "Catalog scenario 9378", "data": {"sku": "SKU9378", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9378@example.com", "threshold": 780}},
    {"id": "CATALOG-9379", "title": "Catalog scenario 9379", "data": {"sku": "SKU9379", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9379@example.com", "threshold": 790}},
    {"id": "CATALOG-9380", "title": "Catalog scenario 9380", "data": {"sku": "SKU9380", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9380@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
