import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5411", "title": "Catalog scenario 5411", "data": {"sku": "SKU5411", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5411@example.com", "threshold": 110}},
    {"id": "CATALOG-5412", "title": "Catalog scenario 5412", "data": {"sku": "SKU5412", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5412@example.com", "threshold": 120}},
    {"id": "CATALOG-5413", "title": "Catalog scenario 5413", "data": {"sku": "SKU5413", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5413@example.com", "threshold": 130}},
    {"id": "CATALOG-5414", "title": "Catalog scenario 5414", "data": {"sku": "SKU5414", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5414@example.com", "threshold": 140}},
    {"id": "CATALOG-5415", "title": "Catalog scenario 5415", "data": {"sku": "SKU5415", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5415@example.com", "threshold": 150}},
    {"id": "CATALOG-5416", "title": "Catalog scenario 5416", "data": {"sku": "SKU5416", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5416@example.com", "threshold": 160}},
    {"id": "CATALOG-5417", "title": "Catalog scenario 5417", "data": {"sku": "SKU5417", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5417@example.com", "threshold": 170}},
    {"id": "CATALOG-5418", "title": "Catalog scenario 5418", "data": {"sku": "SKU5418", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5418@example.com", "threshold": 180}},
    {"id": "CATALOG-5419", "title": "Catalog scenario 5419", "data": {"sku": "SKU5419", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5419@example.com", "threshold": 190}},
    {"id": "CATALOG-5420", "title": "Catalog scenario 5420", "data": {"sku": "SKU5420", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5420@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
