import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1571", "title": "Catalog scenario 1571", "data": {"sku": "SKU1571", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1571@example.com", "threshold": 710}},
    {"id": "CATALOG-1572", "title": "Catalog scenario 1572", "data": {"sku": "SKU1572", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1572@example.com", "threshold": 720}},
    {"id": "CATALOG-1573", "title": "Catalog scenario 1573", "data": {"sku": "SKU1573", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1573@example.com", "threshold": 730}},
    {"id": "CATALOG-1574", "title": "Catalog scenario 1574", "data": {"sku": "SKU1574", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1574@example.com", "threshold": 740}},
    {"id": "CATALOG-1575", "title": "Catalog scenario 1575", "data": {"sku": "SKU1575", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1575@example.com", "threshold": 750}},
    {"id": "CATALOG-1576", "title": "Catalog scenario 1576", "data": {"sku": "SKU1576", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1576@example.com", "threshold": 760}},
    {"id": "CATALOG-1577", "title": "Catalog scenario 1577", "data": {"sku": "SKU1577", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1577@example.com", "threshold": 770}},
    {"id": "CATALOG-1578", "title": "Catalog scenario 1578", "data": {"sku": "SKU1578", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1578@example.com", "threshold": 780}},
    {"id": "CATALOG-1579", "title": "Catalog scenario 1579", "data": {"sku": "SKU1579", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1579@example.com", "threshold": 790}},
    {"id": "CATALOG-1580", "title": "Catalog scenario 1580", "data": {"sku": "SKU1580", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1580@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
