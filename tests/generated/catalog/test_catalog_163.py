import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-9731", "title": "Catalog scenario 9731", "data": {"sku": "SKU9731", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9731@example.com", "threshold": 310}},
    {"id": "CATALOG-9732", "title": "Catalog scenario 9732", "data": {"sku": "SKU9732", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9732@example.com", "threshold": 320}},
    {"id": "CATALOG-9733", "title": "Catalog scenario 9733", "data": {"sku": "SKU9733", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9733@example.com", "threshold": 330}},
    {"id": "CATALOG-9734", "title": "Catalog scenario 9734", "data": {"sku": "SKU9734", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9734@example.com", "threshold": 340}},
    {"id": "CATALOG-9735", "title": "Catalog scenario 9735", "data": {"sku": "SKU9735", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9735@example.com", "threshold": 350}},
    {"id": "CATALOG-9736", "title": "Catalog scenario 9736", "data": {"sku": "SKU9736", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9736@example.com", "threshold": 360}},
    {"id": "CATALOG-9737", "title": "Catalog scenario 9737", "data": {"sku": "SKU9737", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9737@example.com", "threshold": 370}},
    {"id": "CATALOG-9738", "title": "Catalog scenario 9738", "data": {"sku": "SKU9738", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9738@example.com", "threshold": 380}},
    {"id": "CATALOG-9739", "title": "Catalog scenario 9739", "data": {"sku": "SKU9739", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9739@example.com", "threshold": 390}},
    {"id": "CATALOG-9740", "title": "Catalog scenario 9740", "data": {"sku": "SKU9740", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9740@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
