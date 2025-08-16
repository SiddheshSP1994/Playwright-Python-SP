import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6731", "title": "Catalog scenario 6731", "data": {"sku": "SKU6731", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6731@example.com", "threshold": 310}},
    {"id": "CATALOG-6732", "title": "Catalog scenario 6732", "data": {"sku": "SKU6732", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6732@example.com", "threshold": 320}},
    {"id": "CATALOG-6733", "title": "Catalog scenario 6733", "data": {"sku": "SKU6733", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6733@example.com", "threshold": 330}},
    {"id": "CATALOG-6734", "title": "Catalog scenario 6734", "data": {"sku": "SKU6734", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6734@example.com", "threshold": 340}},
    {"id": "CATALOG-6735", "title": "Catalog scenario 6735", "data": {"sku": "SKU6735", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6735@example.com", "threshold": 350}},
    {"id": "CATALOG-6736", "title": "Catalog scenario 6736", "data": {"sku": "SKU6736", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6736@example.com", "threshold": 360}},
    {"id": "CATALOG-6737", "title": "Catalog scenario 6737", "data": {"sku": "SKU6737", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6737@example.com", "threshold": 370}},
    {"id": "CATALOG-6738", "title": "Catalog scenario 6738", "data": {"sku": "SKU6738", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6738@example.com", "threshold": 380}},
    {"id": "CATALOG-6739", "title": "Catalog scenario 6739", "data": {"sku": "SKU6739", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6739@example.com", "threshold": 390}},
    {"id": "CATALOG-6740", "title": "Catalog scenario 6740", "data": {"sku": "SKU6740", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6740@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
