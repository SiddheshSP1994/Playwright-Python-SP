import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-7571", "title": "Catalog scenario 7571", "data": {"sku": "SKU7571", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7571@example.com", "threshold": 710}},
    {"id": "CATALOG-7572", "title": "Catalog scenario 7572", "data": {"sku": "SKU7572", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7572@example.com", "threshold": 720}},
    {"id": "CATALOG-7573", "title": "Catalog scenario 7573", "data": {"sku": "SKU7573", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7573@example.com", "threshold": 730}},
    {"id": "CATALOG-7574", "title": "Catalog scenario 7574", "data": {"sku": "SKU7574", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7574@example.com", "threshold": 740}},
    {"id": "CATALOG-7575", "title": "Catalog scenario 7575", "data": {"sku": "SKU7575", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7575@example.com", "threshold": 750}},
    {"id": "CATALOG-7576", "title": "Catalog scenario 7576", "data": {"sku": "SKU7576", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7576@example.com", "threshold": 760}},
    {"id": "CATALOG-7577", "title": "Catalog scenario 7577", "data": {"sku": "SKU7577", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7577@example.com", "threshold": 770}},
    {"id": "CATALOG-7578", "title": "Catalog scenario 7578", "data": {"sku": "SKU7578", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7578@example.com", "threshold": 780}},
    {"id": "CATALOG-7579", "title": "Catalog scenario 7579", "data": {"sku": "SKU7579", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7579@example.com", "threshold": 790}},
    {"id": "CATALOG-7580", "title": "Catalog scenario 7580", "data": {"sku": "SKU7580", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7580@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
