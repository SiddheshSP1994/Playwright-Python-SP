import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6371", "title": "Catalog scenario 6371", "data": {"sku": "SKU6371", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6371@example.com", "threshold": 710}},
    {"id": "CATALOG-6372", "title": "Catalog scenario 6372", "data": {"sku": "SKU6372", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6372@example.com", "threshold": 720}},
    {"id": "CATALOG-6373", "title": "Catalog scenario 6373", "data": {"sku": "SKU6373", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6373@example.com", "threshold": 730}},
    {"id": "CATALOG-6374", "title": "Catalog scenario 6374", "data": {"sku": "SKU6374", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6374@example.com", "threshold": 740}},
    {"id": "CATALOG-6375", "title": "Catalog scenario 6375", "data": {"sku": "SKU6375", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6375@example.com", "threshold": 750}},
    {"id": "CATALOG-6376", "title": "Catalog scenario 6376", "data": {"sku": "SKU6376", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6376@example.com", "threshold": 760}},
    {"id": "CATALOG-6377", "title": "Catalog scenario 6377", "data": {"sku": "SKU6377", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6377@example.com", "threshold": 770}},
    {"id": "CATALOG-6378", "title": "Catalog scenario 6378", "data": {"sku": "SKU6378", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6378@example.com", "threshold": 780}},
    {"id": "CATALOG-6379", "title": "Catalog scenario 6379", "data": {"sku": "SKU6379", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6379@example.com", "threshold": 790}},
    {"id": "CATALOG-6380", "title": "Catalog scenario 6380", "data": {"sku": "SKU6380", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6380@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
