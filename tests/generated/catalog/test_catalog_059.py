import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3491", "title": "Catalog scenario 3491", "data": {"sku": "SKU3491", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3491@example.com", "threshold": 910}},
    {"id": "CATALOG-3492", "title": "Catalog scenario 3492", "data": {"sku": "SKU3492", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3492@example.com", "threshold": 920}},
    {"id": "CATALOG-3493", "title": "Catalog scenario 3493", "data": {"sku": "SKU3493", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3493@example.com", "threshold": 930}},
    {"id": "CATALOG-3494", "title": "Catalog scenario 3494", "data": {"sku": "SKU3494", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3494@example.com", "threshold": 940}},
    {"id": "CATALOG-3495", "title": "Catalog scenario 3495", "data": {"sku": "SKU3495", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3495@example.com", "threshold": 950}},
    {"id": "CATALOG-3496", "title": "Catalog scenario 3496", "data": {"sku": "SKU3496", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3496@example.com", "threshold": 960}},
    {"id": "CATALOG-3497", "title": "Catalog scenario 3497", "data": {"sku": "SKU3497", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3497@example.com", "threshold": 970}},
    {"id": "CATALOG-3498", "title": "Catalog scenario 3498", "data": {"sku": "SKU3498", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3498@example.com", "threshold": 980}},
    {"id": "CATALOG-3499", "title": "Catalog scenario 3499", "data": {"sku": "SKU3499", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3499@example.com", "threshold": 990}},
    {"id": "CATALOG-3500", "title": "Catalog scenario 3500", "data": {"sku": "SKU3500", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3500@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
