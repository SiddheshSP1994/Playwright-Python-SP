import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8351", "title": "Catalog scenario 8351", "data": {"sku": "SKU8351", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8351@example.com", "threshold": 510}},
    {"id": "CATALOG-8352", "title": "Catalog scenario 8352", "data": {"sku": "SKU8352", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8352@example.com", "threshold": 520}},
    {"id": "CATALOG-8353", "title": "Catalog scenario 8353", "data": {"sku": "SKU8353", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8353@example.com", "threshold": 530}},
    {"id": "CATALOG-8354", "title": "Catalog scenario 8354", "data": {"sku": "SKU8354", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8354@example.com", "threshold": 540}},
    {"id": "CATALOG-8355", "title": "Catalog scenario 8355", "data": {"sku": "SKU8355", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8355@example.com", "threshold": 550}},
    {"id": "CATALOG-8356", "title": "Catalog scenario 8356", "data": {"sku": "SKU8356", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8356@example.com", "threshold": 560}},
    {"id": "CATALOG-8357", "title": "Catalog scenario 8357", "data": {"sku": "SKU8357", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8357@example.com", "threshold": 570}},
    {"id": "CATALOG-8358", "title": "Catalog scenario 8358", "data": {"sku": "SKU8358", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8358@example.com", "threshold": 580}},
    {"id": "CATALOG-8359", "title": "Catalog scenario 8359", "data": {"sku": "SKU8359", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8359@example.com", "threshold": 590}},
    {"id": "CATALOG-8360", "title": "Catalog scenario 8360", "data": {"sku": "SKU8360", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8360@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
