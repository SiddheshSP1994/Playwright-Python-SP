import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4751", "title": "Catalog scenario 4751", "data": {"sku": "SKU4751", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4751@example.com", "threshold": 510}},
    {"id": "CATALOG-4752", "title": "Catalog scenario 4752", "data": {"sku": "SKU4752", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4752@example.com", "threshold": 520}},
    {"id": "CATALOG-4753", "title": "Catalog scenario 4753", "data": {"sku": "SKU4753", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4753@example.com", "threshold": 530}},
    {"id": "CATALOG-4754", "title": "Catalog scenario 4754", "data": {"sku": "SKU4754", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4754@example.com", "threshold": 540}},
    {"id": "CATALOG-4755", "title": "Catalog scenario 4755", "data": {"sku": "SKU4755", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4755@example.com", "threshold": 550}},
    {"id": "CATALOG-4756", "title": "Catalog scenario 4756", "data": {"sku": "SKU4756", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4756@example.com", "threshold": 560}},
    {"id": "CATALOG-4757", "title": "Catalog scenario 4757", "data": {"sku": "SKU4757", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4757@example.com", "threshold": 570}},
    {"id": "CATALOG-4758", "title": "Catalog scenario 4758", "data": {"sku": "SKU4758", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4758@example.com", "threshold": 580}},
    {"id": "CATALOG-4759", "title": "Catalog scenario 4759", "data": {"sku": "SKU4759", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4759@example.com", "threshold": 590}},
    {"id": "CATALOG-4760", "title": "Catalog scenario 4760", "data": {"sku": "SKU4760", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4760@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
