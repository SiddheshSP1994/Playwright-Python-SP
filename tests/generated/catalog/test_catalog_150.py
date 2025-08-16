import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8951", "title": "Catalog scenario 8951", "data": {"sku": "SKU8951", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8951@example.com", "threshold": 510}},
    {"id": "CATALOG-8952", "title": "Catalog scenario 8952", "data": {"sku": "SKU8952", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8952@example.com", "threshold": 520}},
    {"id": "CATALOG-8953", "title": "Catalog scenario 8953", "data": {"sku": "SKU8953", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8953@example.com", "threshold": 530}},
    {"id": "CATALOG-8954", "title": "Catalog scenario 8954", "data": {"sku": "SKU8954", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8954@example.com", "threshold": 540}},
    {"id": "CATALOG-8955", "title": "Catalog scenario 8955", "data": {"sku": "SKU8955", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8955@example.com", "threshold": 550}},
    {"id": "CATALOG-8956", "title": "Catalog scenario 8956", "data": {"sku": "SKU8956", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8956@example.com", "threshold": 560}},
    {"id": "CATALOG-8957", "title": "Catalog scenario 8957", "data": {"sku": "SKU8957", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8957@example.com", "threshold": 570}},
    {"id": "CATALOG-8958", "title": "Catalog scenario 8958", "data": {"sku": "SKU8958", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8958@example.com", "threshold": 580}},
    {"id": "CATALOG-8959", "title": "Catalog scenario 8959", "data": {"sku": "SKU8959", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8959@example.com", "threshold": 590}},
    {"id": "CATALOG-8960", "title": "Catalog scenario 8960", "data": {"sku": "SKU8960", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8960@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
