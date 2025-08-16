import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-9431", "title": "Catalog scenario 9431", "data": {"sku": "SKU9431", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9431@example.com", "threshold": 310}},
    {"id": "CATALOG-9432", "title": "Catalog scenario 9432", "data": {"sku": "SKU9432", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9432@example.com", "threshold": 320}},
    {"id": "CATALOG-9433", "title": "Catalog scenario 9433", "data": {"sku": "SKU9433", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9433@example.com", "threshold": 330}},
    {"id": "CATALOG-9434", "title": "Catalog scenario 9434", "data": {"sku": "SKU9434", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9434@example.com", "threshold": 340}},
    {"id": "CATALOG-9435", "title": "Catalog scenario 9435", "data": {"sku": "SKU9435", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9435@example.com", "threshold": 350}},
    {"id": "CATALOG-9436", "title": "Catalog scenario 9436", "data": {"sku": "SKU9436", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9436@example.com", "threshold": 360}},
    {"id": "CATALOG-9437", "title": "Catalog scenario 9437", "data": {"sku": "SKU9437", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9437@example.com", "threshold": 370}},
    {"id": "CATALOG-9438", "title": "Catalog scenario 9438", "data": {"sku": "SKU9438", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9438@example.com", "threshold": 380}},
    {"id": "CATALOG-9439", "title": "Catalog scenario 9439", "data": {"sku": "SKU9439", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9439@example.com", "threshold": 390}},
    {"id": "CATALOG-9440", "title": "Catalog scenario 9440", "data": {"sku": "SKU9440", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9440@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
