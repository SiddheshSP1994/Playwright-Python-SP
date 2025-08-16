import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8831", "title": "Catalog scenario 8831", "data": {"sku": "SKU8831", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8831@example.com", "threshold": 310}},
    {"id": "CATALOG-8832", "title": "Catalog scenario 8832", "data": {"sku": "SKU8832", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8832@example.com", "threshold": 320}},
    {"id": "CATALOG-8833", "title": "Catalog scenario 8833", "data": {"sku": "SKU8833", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8833@example.com", "threshold": 330}},
    {"id": "CATALOG-8834", "title": "Catalog scenario 8834", "data": {"sku": "SKU8834", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8834@example.com", "threshold": 340}},
    {"id": "CATALOG-8835", "title": "Catalog scenario 8835", "data": {"sku": "SKU8835", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8835@example.com", "threshold": 350}},
    {"id": "CATALOG-8836", "title": "Catalog scenario 8836", "data": {"sku": "SKU8836", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8836@example.com", "threshold": 360}},
    {"id": "CATALOG-8837", "title": "Catalog scenario 8837", "data": {"sku": "SKU8837", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8837@example.com", "threshold": 370}},
    {"id": "CATALOG-8838", "title": "Catalog scenario 8838", "data": {"sku": "SKU8838", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8838@example.com", "threshold": 380}},
    {"id": "CATALOG-8839", "title": "Catalog scenario 8839", "data": {"sku": "SKU8839", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8839@example.com", "threshold": 390}},
    {"id": "CATALOG-8840", "title": "Catalog scenario 8840", "data": {"sku": "SKU8840", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8840@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
