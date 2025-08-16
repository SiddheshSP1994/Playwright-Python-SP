import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8531", "title": "Catalog scenario 8531", "data": {"sku": "SKU8531", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8531@example.com", "threshold": 310}},
    {"id": "CATALOG-8532", "title": "Catalog scenario 8532", "data": {"sku": "SKU8532", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8532@example.com", "threshold": 320}},
    {"id": "CATALOG-8533", "title": "Catalog scenario 8533", "data": {"sku": "SKU8533", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8533@example.com", "threshold": 330}},
    {"id": "CATALOG-8534", "title": "Catalog scenario 8534", "data": {"sku": "SKU8534", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8534@example.com", "threshold": 340}},
    {"id": "CATALOG-8535", "title": "Catalog scenario 8535", "data": {"sku": "SKU8535", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8535@example.com", "threshold": 350}},
    {"id": "CATALOG-8536", "title": "Catalog scenario 8536", "data": {"sku": "SKU8536", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8536@example.com", "threshold": 360}},
    {"id": "CATALOG-8537", "title": "Catalog scenario 8537", "data": {"sku": "SKU8537", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8537@example.com", "threshold": 370}},
    {"id": "CATALOG-8538", "title": "Catalog scenario 8538", "data": {"sku": "SKU8538", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8538@example.com", "threshold": 380}},
    {"id": "CATALOG-8539", "title": "Catalog scenario 8539", "data": {"sku": "SKU8539", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8539@example.com", "threshold": 390}},
    {"id": "CATALOG-8540", "title": "Catalog scenario 8540", "data": {"sku": "SKU8540", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8540@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
