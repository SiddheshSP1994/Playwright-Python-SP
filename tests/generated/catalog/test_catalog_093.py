import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5531", "title": "Catalog scenario 5531", "data": {"sku": "SKU5531", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5531@example.com", "threshold": 310}},
    {"id": "CATALOG-5532", "title": "Catalog scenario 5532", "data": {"sku": "SKU5532", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5532@example.com", "threshold": 320}},
    {"id": "CATALOG-5533", "title": "Catalog scenario 5533", "data": {"sku": "SKU5533", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5533@example.com", "threshold": 330}},
    {"id": "CATALOG-5534", "title": "Catalog scenario 5534", "data": {"sku": "SKU5534", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5534@example.com", "threshold": 340}},
    {"id": "CATALOG-5535", "title": "Catalog scenario 5535", "data": {"sku": "SKU5535", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5535@example.com", "threshold": 350}},
    {"id": "CATALOG-5536", "title": "Catalog scenario 5536", "data": {"sku": "SKU5536", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5536@example.com", "threshold": 360}},
    {"id": "CATALOG-5537", "title": "Catalog scenario 5537", "data": {"sku": "SKU5537", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5537@example.com", "threshold": 370}},
    {"id": "CATALOG-5538", "title": "Catalog scenario 5538", "data": {"sku": "SKU5538", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5538@example.com", "threshold": 380}},
    {"id": "CATALOG-5539", "title": "Catalog scenario 5539", "data": {"sku": "SKU5539", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5539@example.com", "threshold": 390}},
    {"id": "CATALOG-5540", "title": "Catalog scenario 5540", "data": {"sku": "SKU5540", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5540@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
