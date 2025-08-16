import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4331", "title": "Catalog scenario 4331", "data": {"sku": "SKU4331", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4331@example.com", "threshold": 310}},
    {"id": "CATALOG-4332", "title": "Catalog scenario 4332", "data": {"sku": "SKU4332", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4332@example.com", "threshold": 320}},
    {"id": "CATALOG-4333", "title": "Catalog scenario 4333", "data": {"sku": "SKU4333", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4333@example.com", "threshold": 330}},
    {"id": "CATALOG-4334", "title": "Catalog scenario 4334", "data": {"sku": "SKU4334", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4334@example.com", "threshold": 340}},
    {"id": "CATALOG-4335", "title": "Catalog scenario 4335", "data": {"sku": "SKU4335", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4335@example.com", "threshold": 350}},
    {"id": "CATALOG-4336", "title": "Catalog scenario 4336", "data": {"sku": "SKU4336", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4336@example.com", "threshold": 360}},
    {"id": "CATALOG-4337", "title": "Catalog scenario 4337", "data": {"sku": "SKU4337", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4337@example.com", "threshold": 370}},
    {"id": "CATALOG-4338", "title": "Catalog scenario 4338", "data": {"sku": "SKU4338", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4338@example.com", "threshold": 380}},
    {"id": "CATALOG-4339", "title": "Catalog scenario 4339", "data": {"sku": "SKU4339", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4339@example.com", "threshold": 390}},
    {"id": "CATALOG-4340", "title": "Catalog scenario 4340", "data": {"sku": "SKU4340", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4340@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
