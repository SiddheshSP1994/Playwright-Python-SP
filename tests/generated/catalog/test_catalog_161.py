import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-9611", "title": "Catalog scenario 9611", "data": {"sku": "SKU9611", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9611@example.com", "threshold": 110}},
    {"id": "CATALOG-9612", "title": "Catalog scenario 9612", "data": {"sku": "SKU9612", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9612@example.com", "threshold": 120}},
    {"id": "CATALOG-9613", "title": "Catalog scenario 9613", "data": {"sku": "SKU9613", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9613@example.com", "threshold": 130}},
    {"id": "CATALOG-9614", "title": "Catalog scenario 9614", "data": {"sku": "SKU9614", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9614@example.com", "threshold": 140}},
    {"id": "CATALOG-9615", "title": "Catalog scenario 9615", "data": {"sku": "SKU9615", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9615@example.com", "threshold": 150}},
    {"id": "CATALOG-9616", "title": "Catalog scenario 9616", "data": {"sku": "SKU9616", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9616@example.com", "threshold": 160}},
    {"id": "CATALOG-9617", "title": "Catalog scenario 9617", "data": {"sku": "SKU9617", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9617@example.com", "threshold": 170}},
    {"id": "CATALOG-9618", "title": "Catalog scenario 9618", "data": {"sku": "SKU9618", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9618@example.com", "threshold": 180}},
    {"id": "CATALOG-9619", "title": "Catalog scenario 9619", "data": {"sku": "SKU9619", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9619@example.com", "threshold": 190}},
    {"id": "CATALOG-9620", "title": "Catalog scenario 9620", "data": {"sku": "SKU9620", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9620@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
