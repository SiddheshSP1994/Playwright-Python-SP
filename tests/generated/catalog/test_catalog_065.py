import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3851", "title": "Catalog scenario 3851", "data": {"sku": "SKU3851", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3851@example.com", "threshold": 510}},
    {"id": "CATALOG-3852", "title": "Catalog scenario 3852", "data": {"sku": "SKU3852", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3852@example.com", "threshold": 520}},
    {"id": "CATALOG-3853", "title": "Catalog scenario 3853", "data": {"sku": "SKU3853", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3853@example.com", "threshold": 530}},
    {"id": "CATALOG-3854", "title": "Catalog scenario 3854", "data": {"sku": "SKU3854", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3854@example.com", "threshold": 540}},
    {"id": "CATALOG-3855", "title": "Catalog scenario 3855", "data": {"sku": "SKU3855", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3855@example.com", "threshold": 550}},
    {"id": "CATALOG-3856", "title": "Catalog scenario 3856", "data": {"sku": "SKU3856", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3856@example.com", "threshold": 560}},
    {"id": "CATALOG-3857", "title": "Catalog scenario 3857", "data": {"sku": "SKU3857", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3857@example.com", "threshold": 570}},
    {"id": "CATALOG-3858", "title": "Catalog scenario 3858", "data": {"sku": "SKU3858", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3858@example.com", "threshold": 580}},
    {"id": "CATALOG-3859", "title": "Catalog scenario 3859", "data": {"sku": "SKU3859", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3859@example.com", "threshold": 590}},
    {"id": "CATALOG-3860", "title": "Catalog scenario 3860", "data": {"sku": "SKU3860", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3860@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
