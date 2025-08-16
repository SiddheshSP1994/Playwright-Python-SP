import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1091", "title": "Catalog scenario 1091", "data": {"sku": "SKU1091", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1091@example.com", "threshold": 910}},
    {"id": "CATALOG-1092", "title": "Catalog scenario 1092", "data": {"sku": "SKU1092", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1092@example.com", "threshold": 920}},
    {"id": "CATALOG-1093", "title": "Catalog scenario 1093", "data": {"sku": "SKU1093", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1093@example.com", "threshold": 930}},
    {"id": "CATALOG-1094", "title": "Catalog scenario 1094", "data": {"sku": "SKU1094", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1094@example.com", "threshold": 940}},
    {"id": "CATALOG-1095", "title": "Catalog scenario 1095", "data": {"sku": "SKU1095", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1095@example.com", "threshold": 950}},
    {"id": "CATALOG-1096", "title": "Catalog scenario 1096", "data": {"sku": "SKU1096", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1096@example.com", "threshold": 960}},
    {"id": "CATALOG-1097", "title": "Catalog scenario 1097", "data": {"sku": "SKU1097", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1097@example.com", "threshold": 970}},
    {"id": "CATALOG-1098", "title": "Catalog scenario 1098", "data": {"sku": "SKU1098", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1098@example.com", "threshold": 980}},
    {"id": "CATALOG-1099", "title": "Catalog scenario 1099", "data": {"sku": "SKU1099", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1099@example.com", "threshold": 990}},
    {"id": "CATALOG-1100", "title": "Catalog scenario 1100", "data": {"sku": "SKU1100", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1100@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
