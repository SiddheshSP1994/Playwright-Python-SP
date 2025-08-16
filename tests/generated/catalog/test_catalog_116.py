import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6911", "title": "Catalog scenario 6911", "data": {"sku": "SKU6911", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6911@example.com", "threshold": 110}},
    {"id": "CATALOG-6912", "title": "Catalog scenario 6912", "data": {"sku": "SKU6912", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6912@example.com", "threshold": 120}},
    {"id": "CATALOG-6913", "title": "Catalog scenario 6913", "data": {"sku": "SKU6913", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6913@example.com", "threshold": 130}},
    {"id": "CATALOG-6914", "title": "Catalog scenario 6914", "data": {"sku": "SKU6914", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6914@example.com", "threshold": 140}},
    {"id": "CATALOG-6915", "title": "Catalog scenario 6915", "data": {"sku": "SKU6915", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6915@example.com", "threshold": 150}},
    {"id": "CATALOG-6916", "title": "Catalog scenario 6916", "data": {"sku": "SKU6916", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6916@example.com", "threshold": 160}},
    {"id": "CATALOG-6917", "title": "Catalog scenario 6917", "data": {"sku": "SKU6917", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6917@example.com", "threshold": 170}},
    {"id": "CATALOG-6918", "title": "Catalog scenario 6918", "data": {"sku": "SKU6918", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6918@example.com", "threshold": 180}},
    {"id": "CATALOG-6919", "title": "Catalog scenario 6919", "data": {"sku": "SKU6919", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6919@example.com", "threshold": 190}},
    {"id": "CATALOG-6920", "title": "Catalog scenario 6920", "data": {"sku": "SKU6920", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6920@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
