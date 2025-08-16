import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-9131", "title": "Catalog scenario 9131", "data": {"sku": "SKU9131", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9131@example.com", "threshold": 310}},
    {"id": "CATALOG-9132", "title": "Catalog scenario 9132", "data": {"sku": "SKU9132", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9132@example.com", "threshold": 320}},
    {"id": "CATALOG-9133", "title": "Catalog scenario 9133", "data": {"sku": "SKU9133", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9133@example.com", "threshold": 330}},
    {"id": "CATALOG-9134", "title": "Catalog scenario 9134", "data": {"sku": "SKU9134", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9134@example.com", "threshold": 340}},
    {"id": "CATALOG-9135", "title": "Catalog scenario 9135", "data": {"sku": "SKU9135", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9135@example.com", "threshold": 350}},
    {"id": "CATALOG-9136", "title": "Catalog scenario 9136", "data": {"sku": "SKU9136", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9136@example.com", "threshold": 360}},
    {"id": "CATALOG-9137", "title": "Catalog scenario 9137", "data": {"sku": "SKU9137", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9137@example.com", "threshold": 370}},
    {"id": "CATALOG-9138", "title": "Catalog scenario 9138", "data": {"sku": "SKU9138", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9138@example.com", "threshold": 380}},
    {"id": "CATALOG-9139", "title": "Catalog scenario 9139", "data": {"sku": "SKU9139", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9139@example.com", "threshold": 390}},
    {"id": "CATALOG-9140", "title": "Catalog scenario 9140", "data": {"sku": "SKU9140", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9140@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
