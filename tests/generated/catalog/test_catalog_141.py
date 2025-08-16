import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8411", "title": "Catalog scenario 8411", "data": {"sku": "SKU8411", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8411@example.com", "threshold": 110}},
    {"id": "CATALOG-8412", "title": "Catalog scenario 8412", "data": {"sku": "SKU8412", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8412@example.com", "threshold": 120}},
    {"id": "CATALOG-8413", "title": "Catalog scenario 8413", "data": {"sku": "SKU8413", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8413@example.com", "threshold": 130}},
    {"id": "CATALOG-8414", "title": "Catalog scenario 8414", "data": {"sku": "SKU8414", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8414@example.com", "threshold": 140}},
    {"id": "CATALOG-8415", "title": "Catalog scenario 8415", "data": {"sku": "SKU8415", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8415@example.com", "threshold": 150}},
    {"id": "CATALOG-8416", "title": "Catalog scenario 8416", "data": {"sku": "SKU8416", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8416@example.com", "threshold": 160}},
    {"id": "CATALOG-8417", "title": "Catalog scenario 8417", "data": {"sku": "SKU8417", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8417@example.com", "threshold": 170}},
    {"id": "CATALOG-8418", "title": "Catalog scenario 8418", "data": {"sku": "SKU8418", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8418@example.com", "threshold": 180}},
    {"id": "CATALOG-8419", "title": "Catalog scenario 8419", "data": {"sku": "SKU8419", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8419@example.com", "threshold": 190}},
    {"id": "CATALOG-8420", "title": "Catalog scenario 8420", "data": {"sku": "SKU8420", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8420@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
