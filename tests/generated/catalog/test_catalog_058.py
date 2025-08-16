import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3431", "title": "Catalog scenario 3431", "data": {"sku": "SKU3431", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3431@example.com", "threshold": 310}},
    {"id": "CATALOG-3432", "title": "Catalog scenario 3432", "data": {"sku": "SKU3432", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3432@example.com", "threshold": 320}},
    {"id": "CATALOG-3433", "title": "Catalog scenario 3433", "data": {"sku": "SKU3433", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3433@example.com", "threshold": 330}},
    {"id": "CATALOG-3434", "title": "Catalog scenario 3434", "data": {"sku": "SKU3434", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3434@example.com", "threshold": 340}},
    {"id": "CATALOG-3435", "title": "Catalog scenario 3435", "data": {"sku": "SKU3435", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3435@example.com", "threshold": 350}},
    {"id": "CATALOG-3436", "title": "Catalog scenario 3436", "data": {"sku": "SKU3436", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3436@example.com", "threshold": 360}},
    {"id": "CATALOG-3437", "title": "Catalog scenario 3437", "data": {"sku": "SKU3437", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3437@example.com", "threshold": 370}},
    {"id": "CATALOG-3438", "title": "Catalog scenario 3438", "data": {"sku": "SKU3438", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3438@example.com", "threshold": 380}},
    {"id": "CATALOG-3439", "title": "Catalog scenario 3439", "data": {"sku": "SKU3439", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3439@example.com", "threshold": 390}},
    {"id": "CATALOG-3440", "title": "Catalog scenario 3440", "data": {"sku": "SKU3440", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3440@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
