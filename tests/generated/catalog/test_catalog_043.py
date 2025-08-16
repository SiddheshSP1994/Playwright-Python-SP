import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2531", "title": "Catalog scenario 2531", "data": {"sku": "SKU2531", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2531@example.com", "threshold": 310}},
    {"id": "CATALOG-2532", "title": "Catalog scenario 2532", "data": {"sku": "SKU2532", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2532@example.com", "threshold": 320}},
    {"id": "CATALOG-2533", "title": "Catalog scenario 2533", "data": {"sku": "SKU2533", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2533@example.com", "threshold": 330}},
    {"id": "CATALOG-2534", "title": "Catalog scenario 2534", "data": {"sku": "SKU2534", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2534@example.com", "threshold": 340}},
    {"id": "CATALOG-2535", "title": "Catalog scenario 2535", "data": {"sku": "SKU2535", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2535@example.com", "threshold": 350}},
    {"id": "CATALOG-2536", "title": "Catalog scenario 2536", "data": {"sku": "SKU2536", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2536@example.com", "threshold": 360}},
    {"id": "CATALOG-2537", "title": "Catalog scenario 2537", "data": {"sku": "SKU2537", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2537@example.com", "threshold": 370}},
    {"id": "CATALOG-2538", "title": "Catalog scenario 2538", "data": {"sku": "SKU2538", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2538@example.com", "threshold": 380}},
    {"id": "CATALOG-2539", "title": "Catalog scenario 2539", "data": {"sku": "SKU2539", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2539@example.com", "threshold": 390}},
    {"id": "CATALOG-2540", "title": "Catalog scenario 2540", "data": {"sku": "SKU2540", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2540@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
