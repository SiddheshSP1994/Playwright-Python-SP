import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2831", "title": "Catalog scenario 2831", "data": {"sku": "SKU2831", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2831@example.com", "threshold": 310}},
    {"id": "CATALOG-2832", "title": "Catalog scenario 2832", "data": {"sku": "SKU2832", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2832@example.com", "threshold": 320}},
    {"id": "CATALOG-2833", "title": "Catalog scenario 2833", "data": {"sku": "SKU2833", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2833@example.com", "threshold": 330}},
    {"id": "CATALOG-2834", "title": "Catalog scenario 2834", "data": {"sku": "SKU2834", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2834@example.com", "threshold": 340}},
    {"id": "CATALOG-2835", "title": "Catalog scenario 2835", "data": {"sku": "SKU2835", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2835@example.com", "threshold": 350}},
    {"id": "CATALOG-2836", "title": "Catalog scenario 2836", "data": {"sku": "SKU2836", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2836@example.com", "threshold": 360}},
    {"id": "CATALOG-2837", "title": "Catalog scenario 2837", "data": {"sku": "SKU2837", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2837@example.com", "threshold": 370}},
    {"id": "CATALOG-2838", "title": "Catalog scenario 2838", "data": {"sku": "SKU2838", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2838@example.com", "threshold": 380}},
    {"id": "CATALOG-2839", "title": "Catalog scenario 2839", "data": {"sku": "SKU2839", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2839@example.com", "threshold": 390}},
    {"id": "CATALOG-2840", "title": "Catalog scenario 2840", "data": {"sku": "SKU2840", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2840@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
