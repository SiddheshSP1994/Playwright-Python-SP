import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5231", "title": "Catalog scenario 5231", "data": {"sku": "SKU5231", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5231@example.com", "threshold": 310}},
    {"id": "CATALOG-5232", "title": "Catalog scenario 5232", "data": {"sku": "SKU5232", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5232@example.com", "threshold": 320}},
    {"id": "CATALOG-5233", "title": "Catalog scenario 5233", "data": {"sku": "SKU5233", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5233@example.com", "threshold": 330}},
    {"id": "CATALOG-5234", "title": "Catalog scenario 5234", "data": {"sku": "SKU5234", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5234@example.com", "threshold": 340}},
    {"id": "CATALOG-5235", "title": "Catalog scenario 5235", "data": {"sku": "SKU5235", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5235@example.com", "threshold": 350}},
    {"id": "CATALOG-5236", "title": "Catalog scenario 5236", "data": {"sku": "SKU5236", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5236@example.com", "threshold": 360}},
    {"id": "CATALOG-5237", "title": "Catalog scenario 5237", "data": {"sku": "SKU5237", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5237@example.com", "threshold": 370}},
    {"id": "CATALOG-5238", "title": "Catalog scenario 5238", "data": {"sku": "SKU5238", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5238@example.com", "threshold": 380}},
    {"id": "CATALOG-5239", "title": "Catalog scenario 5239", "data": {"sku": "SKU5239", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5239@example.com", "threshold": 390}},
    {"id": "CATALOG-5240", "title": "Catalog scenario 5240", "data": {"sku": "SKU5240", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5240@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
