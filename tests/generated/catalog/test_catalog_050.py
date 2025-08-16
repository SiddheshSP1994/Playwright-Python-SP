import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2951", "title": "Catalog scenario 2951", "data": {"sku": "SKU2951", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2951@example.com", "threshold": 510}},
    {"id": "CATALOG-2952", "title": "Catalog scenario 2952", "data": {"sku": "SKU2952", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2952@example.com", "threshold": 520}},
    {"id": "CATALOG-2953", "title": "Catalog scenario 2953", "data": {"sku": "SKU2953", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2953@example.com", "threshold": 530}},
    {"id": "CATALOG-2954", "title": "Catalog scenario 2954", "data": {"sku": "SKU2954", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2954@example.com", "threshold": 540}},
    {"id": "CATALOG-2955", "title": "Catalog scenario 2955", "data": {"sku": "SKU2955", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2955@example.com", "threshold": 550}},
    {"id": "CATALOG-2956", "title": "Catalog scenario 2956", "data": {"sku": "SKU2956", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2956@example.com", "threshold": 560}},
    {"id": "CATALOG-2957", "title": "Catalog scenario 2957", "data": {"sku": "SKU2957", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2957@example.com", "threshold": 570}},
    {"id": "CATALOG-2958", "title": "Catalog scenario 2958", "data": {"sku": "SKU2958", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2958@example.com", "threshold": 580}},
    {"id": "CATALOG-2959", "title": "Catalog scenario 2959", "data": {"sku": "SKU2959", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2959@example.com", "threshold": 590}},
    {"id": "CATALOG-2960", "title": "Catalog scenario 2960", "data": {"sku": "SKU2960", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2960@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
