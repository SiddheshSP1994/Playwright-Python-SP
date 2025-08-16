import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-9851", "title": "Catalog scenario 9851", "data": {"sku": "SKU9851", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9851@example.com", "threshold": 510}},
    {"id": "CATALOG-9852", "title": "Catalog scenario 9852", "data": {"sku": "SKU9852", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9852@example.com", "threshold": 520}},
    {"id": "CATALOG-9853", "title": "Catalog scenario 9853", "data": {"sku": "SKU9853", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9853@example.com", "threshold": 530}},
    {"id": "CATALOG-9854", "title": "Catalog scenario 9854", "data": {"sku": "SKU9854", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9854@example.com", "threshold": 540}},
    {"id": "CATALOG-9855", "title": "Catalog scenario 9855", "data": {"sku": "SKU9855", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9855@example.com", "threshold": 550}},
    {"id": "CATALOG-9856", "title": "Catalog scenario 9856", "data": {"sku": "SKU9856", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9856@example.com", "threshold": 560}},
    {"id": "CATALOG-9857", "title": "Catalog scenario 9857", "data": {"sku": "SKU9857", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9857@example.com", "threshold": 570}},
    {"id": "CATALOG-9858", "title": "Catalog scenario 9858", "data": {"sku": "SKU9858", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9858@example.com", "threshold": 580}},
    {"id": "CATALOG-9859", "title": "Catalog scenario 9859", "data": {"sku": "SKU9859", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9859@example.com", "threshold": 590}},
    {"id": "CATALOG-9860", "title": "Catalog scenario 9860", "data": {"sku": "SKU9860", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9860@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
