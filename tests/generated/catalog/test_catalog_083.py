import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4931", "title": "Catalog scenario 4931", "data": {"sku": "SKU4931", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4931@example.com", "threshold": 310}},
    {"id": "CATALOG-4932", "title": "Catalog scenario 4932", "data": {"sku": "SKU4932", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4932@example.com", "threshold": 320}},
    {"id": "CATALOG-4933", "title": "Catalog scenario 4933", "data": {"sku": "SKU4933", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4933@example.com", "threshold": 330}},
    {"id": "CATALOG-4934", "title": "Catalog scenario 4934", "data": {"sku": "SKU4934", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4934@example.com", "threshold": 340}},
    {"id": "CATALOG-4935", "title": "Catalog scenario 4935", "data": {"sku": "SKU4935", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4935@example.com", "threshold": 350}},
    {"id": "CATALOG-4936", "title": "Catalog scenario 4936", "data": {"sku": "SKU4936", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4936@example.com", "threshold": 360}},
    {"id": "CATALOG-4937", "title": "Catalog scenario 4937", "data": {"sku": "SKU4937", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4937@example.com", "threshold": 370}},
    {"id": "CATALOG-4938", "title": "Catalog scenario 4938", "data": {"sku": "SKU4938", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4938@example.com", "threshold": 380}},
    {"id": "CATALOG-4939", "title": "Catalog scenario 4939", "data": {"sku": "SKU4939", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4939@example.com", "threshold": 390}},
    {"id": "CATALOG-4940", "title": "Catalog scenario 4940", "data": {"sku": "SKU4940", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4940@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
