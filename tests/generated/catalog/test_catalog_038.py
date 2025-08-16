import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2231", "title": "Catalog scenario 2231", "data": {"sku": "SKU2231", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2231@example.com", "threshold": 310}},
    {"id": "CATALOG-2232", "title": "Catalog scenario 2232", "data": {"sku": "SKU2232", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2232@example.com", "threshold": 320}},
    {"id": "CATALOG-2233", "title": "Catalog scenario 2233", "data": {"sku": "SKU2233", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2233@example.com", "threshold": 330}},
    {"id": "CATALOG-2234", "title": "Catalog scenario 2234", "data": {"sku": "SKU2234", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2234@example.com", "threshold": 340}},
    {"id": "CATALOG-2235", "title": "Catalog scenario 2235", "data": {"sku": "SKU2235", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2235@example.com", "threshold": 350}},
    {"id": "CATALOG-2236", "title": "Catalog scenario 2236", "data": {"sku": "SKU2236", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2236@example.com", "threshold": 360}},
    {"id": "CATALOG-2237", "title": "Catalog scenario 2237", "data": {"sku": "SKU2237", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2237@example.com", "threshold": 370}},
    {"id": "CATALOG-2238", "title": "Catalog scenario 2238", "data": {"sku": "SKU2238", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2238@example.com", "threshold": 380}},
    {"id": "CATALOG-2239", "title": "Catalog scenario 2239", "data": {"sku": "SKU2239", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2239@example.com", "threshold": 390}},
    {"id": "CATALOG-2240", "title": "Catalog scenario 2240", "data": {"sku": "SKU2240", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2240@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
