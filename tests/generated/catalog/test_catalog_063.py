import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3731", "title": "Catalog scenario 3731", "data": {"sku": "SKU3731", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3731@example.com", "threshold": 310}},
    {"id": "CATALOG-3732", "title": "Catalog scenario 3732", "data": {"sku": "SKU3732", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3732@example.com", "threshold": 320}},
    {"id": "CATALOG-3733", "title": "Catalog scenario 3733", "data": {"sku": "SKU3733", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3733@example.com", "threshold": 330}},
    {"id": "CATALOG-3734", "title": "Catalog scenario 3734", "data": {"sku": "SKU3734", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3734@example.com", "threshold": 340}},
    {"id": "CATALOG-3735", "title": "Catalog scenario 3735", "data": {"sku": "SKU3735", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3735@example.com", "threshold": 350}},
    {"id": "CATALOG-3736", "title": "Catalog scenario 3736", "data": {"sku": "SKU3736", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3736@example.com", "threshold": 360}},
    {"id": "CATALOG-3737", "title": "Catalog scenario 3737", "data": {"sku": "SKU3737", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3737@example.com", "threshold": 370}},
    {"id": "CATALOG-3738", "title": "Catalog scenario 3738", "data": {"sku": "SKU3738", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3738@example.com", "threshold": 380}},
    {"id": "CATALOG-3739", "title": "Catalog scenario 3739", "data": {"sku": "SKU3739", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3739@example.com", "threshold": 390}},
    {"id": "CATALOG-3740", "title": "Catalog scenario 3740", "data": {"sku": "SKU3740", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3740@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
