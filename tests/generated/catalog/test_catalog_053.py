import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3131", "title": "Catalog scenario 3131", "data": {"sku": "SKU3131", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3131@example.com", "threshold": 310}},
    {"id": "CATALOG-3132", "title": "Catalog scenario 3132", "data": {"sku": "SKU3132", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3132@example.com", "threshold": 320}},
    {"id": "CATALOG-3133", "title": "Catalog scenario 3133", "data": {"sku": "SKU3133", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3133@example.com", "threshold": 330}},
    {"id": "CATALOG-3134", "title": "Catalog scenario 3134", "data": {"sku": "SKU3134", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3134@example.com", "threshold": 340}},
    {"id": "CATALOG-3135", "title": "Catalog scenario 3135", "data": {"sku": "SKU3135", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3135@example.com", "threshold": 350}},
    {"id": "CATALOG-3136", "title": "Catalog scenario 3136", "data": {"sku": "SKU3136", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3136@example.com", "threshold": 360}},
    {"id": "CATALOG-3137", "title": "Catalog scenario 3137", "data": {"sku": "SKU3137", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3137@example.com", "threshold": 370}},
    {"id": "CATALOG-3138", "title": "Catalog scenario 3138", "data": {"sku": "SKU3138", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3138@example.com", "threshold": 380}},
    {"id": "CATALOG-3139", "title": "Catalog scenario 3139", "data": {"sku": "SKU3139", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3139@example.com", "threshold": 390}},
    {"id": "CATALOG-3140", "title": "Catalog scenario 3140", "data": {"sku": "SKU3140", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3140@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
