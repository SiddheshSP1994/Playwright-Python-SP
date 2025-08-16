import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4031", "title": "Catalog scenario 4031", "data": {"sku": "SKU4031", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4031@example.com", "threshold": 310}},
    {"id": "CATALOG-4032", "title": "Catalog scenario 4032", "data": {"sku": "SKU4032", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4032@example.com", "threshold": 320}},
    {"id": "CATALOG-4033", "title": "Catalog scenario 4033", "data": {"sku": "SKU4033", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4033@example.com", "threshold": 330}},
    {"id": "CATALOG-4034", "title": "Catalog scenario 4034", "data": {"sku": "SKU4034", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4034@example.com", "threshold": 340}},
    {"id": "CATALOG-4035", "title": "Catalog scenario 4035", "data": {"sku": "SKU4035", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4035@example.com", "threshold": 350}},
    {"id": "CATALOG-4036", "title": "Catalog scenario 4036", "data": {"sku": "SKU4036", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4036@example.com", "threshold": 360}},
    {"id": "CATALOG-4037", "title": "Catalog scenario 4037", "data": {"sku": "SKU4037", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4037@example.com", "threshold": 370}},
    {"id": "CATALOG-4038", "title": "Catalog scenario 4038", "data": {"sku": "SKU4038", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4038@example.com", "threshold": 380}},
    {"id": "CATALOG-4039", "title": "Catalog scenario 4039", "data": {"sku": "SKU4039", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4039@example.com", "threshold": 390}},
    {"id": "CATALOG-4040", "title": "Catalog scenario 4040", "data": {"sku": "SKU4040", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4040@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
