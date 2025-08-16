import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5951", "title": "Catalog scenario 5951", "data": {"sku": "SKU5951", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5951@example.com", "threshold": 510}},
    {"id": "CATALOG-5952", "title": "Catalog scenario 5952", "data": {"sku": "SKU5952", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5952@example.com", "threshold": 520}},
    {"id": "CATALOG-5953", "title": "Catalog scenario 5953", "data": {"sku": "SKU5953", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5953@example.com", "threshold": 530}},
    {"id": "CATALOG-5954", "title": "Catalog scenario 5954", "data": {"sku": "SKU5954", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5954@example.com", "threshold": 540}},
    {"id": "CATALOG-5955", "title": "Catalog scenario 5955", "data": {"sku": "SKU5955", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5955@example.com", "threshold": 550}},
    {"id": "CATALOG-5956", "title": "Catalog scenario 5956", "data": {"sku": "SKU5956", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5956@example.com", "threshold": 560}},
    {"id": "CATALOG-5957", "title": "Catalog scenario 5957", "data": {"sku": "SKU5957", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5957@example.com", "threshold": 570}},
    {"id": "CATALOG-5958", "title": "Catalog scenario 5958", "data": {"sku": "SKU5958", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5958@example.com", "threshold": 580}},
    {"id": "CATALOG-5959", "title": "Catalog scenario 5959", "data": {"sku": "SKU5959", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5959@example.com", "threshold": 590}},
    {"id": "CATALOG-5960", "title": "Catalog scenario 5960", "data": {"sku": "SKU5960", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5960@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
