import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-7331", "title": "Catalog scenario 7331", "data": {"sku": "SKU7331", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7331@example.com", "threshold": 310}},
    {"id": "CATALOG-7332", "title": "Catalog scenario 7332", "data": {"sku": "SKU7332", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7332@example.com", "threshold": 320}},
    {"id": "CATALOG-7333", "title": "Catalog scenario 7333", "data": {"sku": "SKU7333", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7333@example.com", "threshold": 330}},
    {"id": "CATALOG-7334", "title": "Catalog scenario 7334", "data": {"sku": "SKU7334", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7334@example.com", "threshold": 340}},
    {"id": "CATALOG-7335", "title": "Catalog scenario 7335", "data": {"sku": "SKU7335", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7335@example.com", "threshold": 350}},
    {"id": "CATALOG-7336", "title": "Catalog scenario 7336", "data": {"sku": "SKU7336", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7336@example.com", "threshold": 360}},
    {"id": "CATALOG-7337", "title": "Catalog scenario 7337", "data": {"sku": "SKU7337", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7337@example.com", "threshold": 370}},
    {"id": "CATALOG-7338", "title": "Catalog scenario 7338", "data": {"sku": "SKU7338", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7338@example.com", "threshold": 380}},
    {"id": "CATALOG-7339", "title": "Catalog scenario 7339", "data": {"sku": "SKU7339", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7339@example.com", "threshold": 390}},
    {"id": "CATALOG-7340", "title": "Catalog scenario 7340", "data": {"sku": "SKU7340", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7340@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
