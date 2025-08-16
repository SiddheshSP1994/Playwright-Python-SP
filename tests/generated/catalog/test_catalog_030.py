import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1751", "title": "Catalog scenario 1751", "data": {"sku": "SKU1751", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1751@example.com", "threshold": 510}},
    {"id": "CATALOG-1752", "title": "Catalog scenario 1752", "data": {"sku": "SKU1752", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1752@example.com", "threshold": 520}},
    {"id": "CATALOG-1753", "title": "Catalog scenario 1753", "data": {"sku": "SKU1753", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1753@example.com", "threshold": 530}},
    {"id": "CATALOG-1754", "title": "Catalog scenario 1754", "data": {"sku": "SKU1754", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1754@example.com", "threshold": 540}},
    {"id": "CATALOG-1755", "title": "Catalog scenario 1755", "data": {"sku": "SKU1755", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1755@example.com", "threshold": 550}},
    {"id": "CATALOG-1756", "title": "Catalog scenario 1756", "data": {"sku": "SKU1756", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1756@example.com", "threshold": 560}},
    {"id": "CATALOG-1757", "title": "Catalog scenario 1757", "data": {"sku": "SKU1757", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1757@example.com", "threshold": 570}},
    {"id": "CATALOG-1758", "title": "Catalog scenario 1758", "data": {"sku": "SKU1758", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1758@example.com", "threshold": 580}},
    {"id": "CATALOG-1759", "title": "Catalog scenario 1759", "data": {"sku": "SKU1759", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1759@example.com", "threshold": 590}},
    {"id": "CATALOG-1760", "title": "Catalog scenario 1760", "data": {"sku": "SKU1760", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1760@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
