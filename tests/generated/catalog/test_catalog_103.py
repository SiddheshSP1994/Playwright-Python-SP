import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6131", "title": "Catalog scenario 6131", "data": {"sku": "SKU6131", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6131@example.com", "threshold": 310}},
    {"id": "CATALOG-6132", "title": "Catalog scenario 6132", "data": {"sku": "SKU6132", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6132@example.com", "threshold": 320}},
    {"id": "CATALOG-6133", "title": "Catalog scenario 6133", "data": {"sku": "SKU6133", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6133@example.com", "threshold": 330}},
    {"id": "CATALOG-6134", "title": "Catalog scenario 6134", "data": {"sku": "SKU6134", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6134@example.com", "threshold": 340}},
    {"id": "CATALOG-6135", "title": "Catalog scenario 6135", "data": {"sku": "SKU6135", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6135@example.com", "threshold": 350}},
    {"id": "CATALOG-6136", "title": "Catalog scenario 6136", "data": {"sku": "SKU6136", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6136@example.com", "threshold": 360}},
    {"id": "CATALOG-6137", "title": "Catalog scenario 6137", "data": {"sku": "SKU6137", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6137@example.com", "threshold": 370}},
    {"id": "CATALOG-6138", "title": "Catalog scenario 6138", "data": {"sku": "SKU6138", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6138@example.com", "threshold": 380}},
    {"id": "CATALOG-6139", "title": "Catalog scenario 6139", "data": {"sku": "SKU6139", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6139@example.com", "threshold": 390}},
    {"id": "CATALOG-6140", "title": "Catalog scenario 6140", "data": {"sku": "SKU6140", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6140@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
