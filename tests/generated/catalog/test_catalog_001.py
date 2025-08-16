import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0011", "title": "Catalog scenario 11", "data": {"sku": "SKU11", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user11@example.com", "threshold": 110}},
    {"id": "CATALOG-0012", "title": "Catalog scenario 12", "data": {"sku": "SKU12", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user12@example.com", "threshold": 120}},
    {"id": "CATALOG-0013", "title": "Catalog scenario 13", "data": {"sku": "SKU13", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user13@example.com", "threshold": 130}},
    {"id": "CATALOG-0014", "title": "Catalog scenario 14", "data": {"sku": "SKU14", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user14@example.com", "threshold": 140}},
    {"id": "CATALOG-0015", "title": "Catalog scenario 15", "data": {"sku": "SKU15", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user15@example.com", "threshold": 150}},
    {"id": "CATALOG-0016", "title": "Catalog scenario 16", "data": {"sku": "SKU16", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user16@example.com", "threshold": 160}},
    {"id": "CATALOG-0017", "title": "Catalog scenario 17", "data": {"sku": "SKU17", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user17@example.com", "threshold": 170}},
    {"id": "CATALOG-0018", "title": "Catalog scenario 18", "data": {"sku": "SKU18", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user18@example.com", "threshold": 180}},
    {"id": "CATALOG-0019", "title": "Catalog scenario 19", "data": {"sku": "SKU19", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user19@example.com", "threshold": 190}},
    {"id": "CATALOG-0020", "title": "Catalog scenario 20", "data": {"sku": "SKU20", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user20@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
