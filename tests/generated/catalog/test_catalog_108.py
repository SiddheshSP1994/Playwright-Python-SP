import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6431", "title": "Catalog scenario 6431", "data": {"sku": "SKU6431", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6431@example.com", "threshold": 310}},
    {"id": "CATALOG-6432", "title": "Catalog scenario 6432", "data": {"sku": "SKU6432", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6432@example.com", "threshold": 320}},
    {"id": "CATALOG-6433", "title": "Catalog scenario 6433", "data": {"sku": "SKU6433", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6433@example.com", "threshold": 330}},
    {"id": "CATALOG-6434", "title": "Catalog scenario 6434", "data": {"sku": "SKU6434", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6434@example.com", "threshold": 340}},
    {"id": "CATALOG-6435", "title": "Catalog scenario 6435", "data": {"sku": "SKU6435", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6435@example.com", "threshold": 350}},
    {"id": "CATALOG-6436", "title": "Catalog scenario 6436", "data": {"sku": "SKU6436", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6436@example.com", "threshold": 360}},
    {"id": "CATALOG-6437", "title": "Catalog scenario 6437", "data": {"sku": "SKU6437", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6437@example.com", "threshold": 370}},
    {"id": "CATALOG-6438", "title": "Catalog scenario 6438", "data": {"sku": "SKU6438", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6438@example.com", "threshold": 380}},
    {"id": "CATALOG-6439", "title": "Catalog scenario 6439", "data": {"sku": "SKU6439", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6439@example.com", "threshold": 390}},
    {"id": "CATALOG-6440", "title": "Catalog scenario 6440", "data": {"sku": "SKU6440", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6440@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
