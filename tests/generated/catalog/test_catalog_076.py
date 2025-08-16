import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4511", "title": "Catalog scenario 4511", "data": {"sku": "SKU4511", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4511@example.com", "threshold": 110}},
    {"id": "CATALOG-4512", "title": "Catalog scenario 4512", "data": {"sku": "SKU4512", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4512@example.com", "threshold": 120}},
    {"id": "CATALOG-4513", "title": "Catalog scenario 4513", "data": {"sku": "SKU4513", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4513@example.com", "threshold": 130}},
    {"id": "CATALOG-4514", "title": "Catalog scenario 4514", "data": {"sku": "SKU4514", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4514@example.com", "threshold": 140}},
    {"id": "CATALOG-4515", "title": "Catalog scenario 4515", "data": {"sku": "SKU4515", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4515@example.com", "threshold": 150}},
    {"id": "CATALOG-4516", "title": "Catalog scenario 4516", "data": {"sku": "SKU4516", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4516@example.com", "threshold": 160}},
    {"id": "CATALOG-4517", "title": "Catalog scenario 4517", "data": {"sku": "SKU4517", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4517@example.com", "threshold": 170}},
    {"id": "CATALOG-4518", "title": "Catalog scenario 4518", "data": {"sku": "SKU4518", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4518@example.com", "threshold": 180}},
    {"id": "CATALOG-4519", "title": "Catalog scenario 4519", "data": {"sku": "SKU4519", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4519@example.com", "threshold": 190}},
    {"id": "CATALOG-4520", "title": "Catalog scenario 4520", "data": {"sku": "SKU4520", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4520@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
