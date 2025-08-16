import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5831", "title": "Catalog scenario 5831", "data": {"sku": "SKU5831", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5831@example.com", "threshold": 310}},
    {"id": "CATALOG-5832", "title": "Catalog scenario 5832", "data": {"sku": "SKU5832", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5832@example.com", "threshold": 320}},
    {"id": "CATALOG-5833", "title": "Catalog scenario 5833", "data": {"sku": "SKU5833", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5833@example.com", "threshold": 330}},
    {"id": "CATALOG-5834", "title": "Catalog scenario 5834", "data": {"sku": "SKU5834", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5834@example.com", "threshold": 340}},
    {"id": "CATALOG-5835", "title": "Catalog scenario 5835", "data": {"sku": "SKU5835", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5835@example.com", "threshold": 350}},
    {"id": "CATALOG-5836", "title": "Catalog scenario 5836", "data": {"sku": "SKU5836", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5836@example.com", "threshold": 360}},
    {"id": "CATALOG-5837", "title": "Catalog scenario 5837", "data": {"sku": "SKU5837", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5837@example.com", "threshold": 370}},
    {"id": "CATALOG-5838", "title": "Catalog scenario 5838", "data": {"sku": "SKU5838", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5838@example.com", "threshold": 380}},
    {"id": "CATALOG-5839", "title": "Catalog scenario 5839", "data": {"sku": "SKU5839", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5839@example.com", "threshold": 390}},
    {"id": "CATALOG-5840", "title": "Catalog scenario 5840", "data": {"sku": "SKU5840", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5840@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
