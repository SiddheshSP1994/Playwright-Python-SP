import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3611", "title": "Catalog scenario 3611", "data": {"sku": "SKU3611", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3611@example.com", "threshold": 110}},
    {"id": "CATALOG-3612", "title": "Catalog scenario 3612", "data": {"sku": "SKU3612", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3612@example.com", "threshold": 120}},
    {"id": "CATALOG-3613", "title": "Catalog scenario 3613", "data": {"sku": "SKU3613", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3613@example.com", "threshold": 130}},
    {"id": "CATALOG-3614", "title": "Catalog scenario 3614", "data": {"sku": "SKU3614", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3614@example.com", "threshold": 140}},
    {"id": "CATALOG-3615", "title": "Catalog scenario 3615", "data": {"sku": "SKU3615", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3615@example.com", "threshold": 150}},
    {"id": "CATALOG-3616", "title": "Catalog scenario 3616", "data": {"sku": "SKU3616", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3616@example.com", "threshold": 160}},
    {"id": "CATALOG-3617", "title": "Catalog scenario 3617", "data": {"sku": "SKU3617", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3617@example.com", "threshold": 170}},
    {"id": "CATALOG-3618", "title": "Catalog scenario 3618", "data": {"sku": "SKU3618", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3618@example.com", "threshold": 180}},
    {"id": "CATALOG-3619", "title": "Catalog scenario 3619", "data": {"sku": "SKU3619", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3619@example.com", "threshold": 190}},
    {"id": "CATALOG-3620", "title": "Catalog scenario 3620", "data": {"sku": "SKU3620", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3620@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
