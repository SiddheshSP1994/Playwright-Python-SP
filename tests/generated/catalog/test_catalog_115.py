import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6851", "title": "Catalog scenario 6851", "data": {"sku": "SKU6851", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6851@example.com", "threshold": 510}},
    {"id": "CATALOG-6852", "title": "Catalog scenario 6852", "data": {"sku": "SKU6852", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6852@example.com", "threshold": 520}},
    {"id": "CATALOG-6853", "title": "Catalog scenario 6853", "data": {"sku": "SKU6853", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6853@example.com", "threshold": 530}},
    {"id": "CATALOG-6854", "title": "Catalog scenario 6854", "data": {"sku": "SKU6854", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6854@example.com", "threshold": 540}},
    {"id": "CATALOG-6855", "title": "Catalog scenario 6855", "data": {"sku": "SKU6855", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6855@example.com", "threshold": 550}},
    {"id": "CATALOG-6856", "title": "Catalog scenario 6856", "data": {"sku": "SKU6856", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6856@example.com", "threshold": 560}},
    {"id": "CATALOG-6857", "title": "Catalog scenario 6857", "data": {"sku": "SKU6857", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6857@example.com", "threshold": 570}},
    {"id": "CATALOG-6858", "title": "Catalog scenario 6858", "data": {"sku": "SKU6858", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6858@example.com", "threshold": 580}},
    {"id": "CATALOG-6859", "title": "Catalog scenario 6859", "data": {"sku": "SKU6859", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6859@example.com", "threshold": 590}},
    {"id": "CATALOG-6860", "title": "Catalog scenario 6860", "data": {"sku": "SKU6860", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6860@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
