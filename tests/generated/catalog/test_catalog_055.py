import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3251", "title": "Catalog scenario 3251", "data": {"sku": "SKU3251", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3251@example.com", "threshold": 510}},
    {"id": "CATALOG-3252", "title": "Catalog scenario 3252", "data": {"sku": "SKU3252", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3252@example.com", "threshold": 520}},
    {"id": "CATALOG-3253", "title": "Catalog scenario 3253", "data": {"sku": "SKU3253", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3253@example.com", "threshold": 530}},
    {"id": "CATALOG-3254", "title": "Catalog scenario 3254", "data": {"sku": "SKU3254", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3254@example.com", "threshold": 540}},
    {"id": "CATALOG-3255", "title": "Catalog scenario 3255", "data": {"sku": "SKU3255", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3255@example.com", "threshold": 550}},
    {"id": "CATALOG-3256", "title": "Catalog scenario 3256", "data": {"sku": "SKU3256", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3256@example.com", "threshold": 560}},
    {"id": "CATALOG-3257", "title": "Catalog scenario 3257", "data": {"sku": "SKU3257", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3257@example.com", "threshold": 570}},
    {"id": "CATALOG-3258", "title": "Catalog scenario 3258", "data": {"sku": "SKU3258", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3258@example.com", "threshold": 580}},
    {"id": "CATALOG-3259", "title": "Catalog scenario 3259", "data": {"sku": "SKU3259", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3259@example.com", "threshold": 590}},
    {"id": "CATALOG-3260", "title": "Catalog scenario 3260", "data": {"sku": "SKU3260", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3260@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
