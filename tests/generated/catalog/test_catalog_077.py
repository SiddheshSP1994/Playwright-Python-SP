import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4571", "title": "Catalog scenario 4571", "data": {"sku": "SKU4571", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4571@example.com", "threshold": 710}},
    {"id": "CATALOG-4572", "title": "Catalog scenario 4572", "data": {"sku": "SKU4572", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4572@example.com", "threshold": 720}},
    {"id": "CATALOG-4573", "title": "Catalog scenario 4573", "data": {"sku": "SKU4573", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4573@example.com", "threshold": 730}},
    {"id": "CATALOG-4574", "title": "Catalog scenario 4574", "data": {"sku": "SKU4574", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4574@example.com", "threshold": 740}},
    {"id": "CATALOG-4575", "title": "Catalog scenario 4575", "data": {"sku": "SKU4575", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4575@example.com", "threshold": 750}},
    {"id": "CATALOG-4576", "title": "Catalog scenario 4576", "data": {"sku": "SKU4576", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4576@example.com", "threshold": 760}},
    {"id": "CATALOG-4577", "title": "Catalog scenario 4577", "data": {"sku": "SKU4577", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4577@example.com", "threshold": 770}},
    {"id": "CATALOG-4578", "title": "Catalog scenario 4578", "data": {"sku": "SKU4578", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4578@example.com", "threshold": 780}},
    {"id": "CATALOG-4579", "title": "Catalog scenario 4579", "data": {"sku": "SKU4579", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4579@example.com", "threshold": 790}},
    {"id": "CATALOG-4580", "title": "Catalog scenario 4580", "data": {"sku": "SKU4580", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4580@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
