import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3371", "title": "Catalog scenario 3371", "data": {"sku": "SKU3371", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3371@example.com", "threshold": 710}},
    {"id": "CATALOG-3372", "title": "Catalog scenario 3372", "data": {"sku": "SKU3372", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3372@example.com", "threshold": 720}},
    {"id": "CATALOG-3373", "title": "Catalog scenario 3373", "data": {"sku": "SKU3373", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3373@example.com", "threshold": 730}},
    {"id": "CATALOG-3374", "title": "Catalog scenario 3374", "data": {"sku": "SKU3374", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3374@example.com", "threshold": 740}},
    {"id": "CATALOG-3375", "title": "Catalog scenario 3375", "data": {"sku": "SKU3375", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3375@example.com", "threshold": 750}},
    {"id": "CATALOG-3376", "title": "Catalog scenario 3376", "data": {"sku": "SKU3376", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3376@example.com", "threshold": 760}},
    {"id": "CATALOG-3377", "title": "Catalog scenario 3377", "data": {"sku": "SKU3377", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3377@example.com", "threshold": 770}},
    {"id": "CATALOG-3378", "title": "Catalog scenario 3378", "data": {"sku": "SKU3378", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3378@example.com", "threshold": 780}},
    {"id": "CATALOG-3379", "title": "Catalog scenario 3379", "data": {"sku": "SKU3379", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3379@example.com", "threshold": 790}},
    {"id": "CATALOG-3380", "title": "Catalog scenario 3380", "data": {"sku": "SKU3380", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3380@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
