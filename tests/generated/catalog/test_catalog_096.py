import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5711", "title": "Catalog scenario 5711", "data": {"sku": "SKU5711", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5711@example.com", "threshold": 110}},
    {"id": "CATALOG-5712", "title": "Catalog scenario 5712", "data": {"sku": "SKU5712", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5712@example.com", "threshold": 120}},
    {"id": "CATALOG-5713", "title": "Catalog scenario 5713", "data": {"sku": "SKU5713", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5713@example.com", "threshold": 130}},
    {"id": "CATALOG-5714", "title": "Catalog scenario 5714", "data": {"sku": "SKU5714", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5714@example.com", "threshold": 140}},
    {"id": "CATALOG-5715", "title": "Catalog scenario 5715", "data": {"sku": "SKU5715", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5715@example.com", "threshold": 150}},
    {"id": "CATALOG-5716", "title": "Catalog scenario 5716", "data": {"sku": "SKU5716", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5716@example.com", "threshold": 160}},
    {"id": "CATALOG-5717", "title": "Catalog scenario 5717", "data": {"sku": "SKU5717", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5717@example.com", "threshold": 170}},
    {"id": "CATALOG-5718", "title": "Catalog scenario 5718", "data": {"sku": "SKU5718", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5718@example.com", "threshold": 180}},
    {"id": "CATALOG-5719", "title": "Catalog scenario 5719", "data": {"sku": "SKU5719", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5719@example.com", "threshold": 190}},
    {"id": "CATALOG-5720", "title": "Catalog scenario 5720", "data": {"sku": "SKU5720", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5720@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
