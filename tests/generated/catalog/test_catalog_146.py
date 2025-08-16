import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8711", "title": "Catalog scenario 8711", "data": {"sku": "SKU8711", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8711@example.com", "threshold": 110}},
    {"id": "CATALOG-8712", "title": "Catalog scenario 8712", "data": {"sku": "SKU8712", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8712@example.com", "threshold": 120}},
    {"id": "CATALOG-8713", "title": "Catalog scenario 8713", "data": {"sku": "SKU8713", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8713@example.com", "threshold": 130}},
    {"id": "CATALOG-8714", "title": "Catalog scenario 8714", "data": {"sku": "SKU8714", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8714@example.com", "threshold": 140}},
    {"id": "CATALOG-8715", "title": "Catalog scenario 8715", "data": {"sku": "SKU8715", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8715@example.com", "threshold": 150}},
    {"id": "CATALOG-8716", "title": "Catalog scenario 8716", "data": {"sku": "SKU8716", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8716@example.com", "threshold": 160}},
    {"id": "CATALOG-8717", "title": "Catalog scenario 8717", "data": {"sku": "SKU8717", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8717@example.com", "threshold": 170}},
    {"id": "CATALOG-8718", "title": "Catalog scenario 8718", "data": {"sku": "SKU8718", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8718@example.com", "threshold": 180}},
    {"id": "CATALOG-8719", "title": "Catalog scenario 8719", "data": {"sku": "SKU8719", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8719@example.com", "threshold": 190}},
    {"id": "CATALOG-8720", "title": "Catalog scenario 8720", "data": {"sku": "SKU8720", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8720@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
