import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-9911", "title": "Catalog scenario 9911", "data": {"sku": "SKU9911", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9911@example.com", "threshold": 110}},
    {"id": "CATALOG-9912", "title": "Catalog scenario 9912", "data": {"sku": "SKU9912", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9912@example.com", "threshold": 120}},
    {"id": "CATALOG-9913", "title": "Catalog scenario 9913", "data": {"sku": "SKU9913", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9913@example.com", "threshold": 130}},
    {"id": "CATALOG-9914", "title": "Catalog scenario 9914", "data": {"sku": "SKU9914", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9914@example.com", "threshold": 140}},
    {"id": "CATALOG-9915", "title": "Catalog scenario 9915", "data": {"sku": "SKU9915", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9915@example.com", "threshold": 150}},
    {"id": "CATALOG-9916", "title": "Catalog scenario 9916", "data": {"sku": "SKU9916", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9916@example.com", "threshold": 160}},
    {"id": "CATALOG-9917", "title": "Catalog scenario 9917", "data": {"sku": "SKU9917", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9917@example.com", "threshold": 170}},
    {"id": "CATALOG-9918", "title": "Catalog scenario 9918", "data": {"sku": "SKU9918", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9918@example.com", "threshold": 180}},
    {"id": "CATALOG-9919", "title": "Catalog scenario 9919", "data": {"sku": "SKU9919", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9919@example.com", "threshold": 190}},
    {"id": "CATALOG-9920", "title": "Catalog scenario 9920", "data": {"sku": "SKU9920", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9920@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
