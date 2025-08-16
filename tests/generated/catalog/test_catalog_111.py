import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6611", "title": "Catalog scenario 6611", "data": {"sku": "SKU6611", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6611@example.com", "threshold": 110}},
    {"id": "CATALOG-6612", "title": "Catalog scenario 6612", "data": {"sku": "SKU6612", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6612@example.com", "threshold": 120}},
    {"id": "CATALOG-6613", "title": "Catalog scenario 6613", "data": {"sku": "SKU6613", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6613@example.com", "threshold": 130}},
    {"id": "CATALOG-6614", "title": "Catalog scenario 6614", "data": {"sku": "SKU6614", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6614@example.com", "threshold": 140}},
    {"id": "CATALOG-6615", "title": "Catalog scenario 6615", "data": {"sku": "SKU6615", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6615@example.com", "threshold": 150}},
    {"id": "CATALOG-6616", "title": "Catalog scenario 6616", "data": {"sku": "SKU6616", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6616@example.com", "threshold": 160}},
    {"id": "CATALOG-6617", "title": "Catalog scenario 6617", "data": {"sku": "SKU6617", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6617@example.com", "threshold": 170}},
    {"id": "CATALOG-6618", "title": "Catalog scenario 6618", "data": {"sku": "SKU6618", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6618@example.com", "threshold": 180}},
    {"id": "CATALOG-6619", "title": "Catalog scenario 6619", "data": {"sku": "SKU6619", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6619@example.com", "threshold": 190}},
    {"id": "CATALOG-6620", "title": "Catalog scenario 6620", "data": {"sku": "SKU6620", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6620@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
