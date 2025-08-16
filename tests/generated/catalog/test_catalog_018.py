import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1031", "title": "Catalog scenario 1031", "data": {"sku": "SKU1031", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1031@example.com", "threshold": 310}},
    {"id": "CATALOG-1032", "title": "Catalog scenario 1032", "data": {"sku": "SKU1032", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1032@example.com", "threshold": 320}},
    {"id": "CATALOG-1033", "title": "Catalog scenario 1033", "data": {"sku": "SKU1033", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1033@example.com", "threshold": 330}},
    {"id": "CATALOG-1034", "title": "Catalog scenario 1034", "data": {"sku": "SKU1034", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1034@example.com", "threshold": 340}},
    {"id": "CATALOG-1035", "title": "Catalog scenario 1035", "data": {"sku": "SKU1035", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1035@example.com", "threshold": 350}},
    {"id": "CATALOG-1036", "title": "Catalog scenario 1036", "data": {"sku": "SKU1036", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1036@example.com", "threshold": 360}},
    {"id": "CATALOG-1037", "title": "Catalog scenario 1037", "data": {"sku": "SKU1037", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1037@example.com", "threshold": 370}},
    {"id": "CATALOG-1038", "title": "Catalog scenario 1038", "data": {"sku": "SKU1038", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1038@example.com", "threshold": 380}},
    {"id": "CATALOG-1039", "title": "Catalog scenario 1039", "data": {"sku": "SKU1039", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1039@example.com", "threshold": 390}},
    {"id": "CATALOG-1040", "title": "Catalog scenario 1040", "data": {"sku": "SKU1040", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1040@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
