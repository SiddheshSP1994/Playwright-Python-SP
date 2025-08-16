import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-7751", "title": "Catalog scenario 7751", "data": {"sku": "SKU7751", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7751@example.com", "threshold": 510}},
    {"id": "CATALOG-7752", "title": "Catalog scenario 7752", "data": {"sku": "SKU7752", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7752@example.com", "threshold": 520}},
    {"id": "CATALOG-7753", "title": "Catalog scenario 7753", "data": {"sku": "SKU7753", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7753@example.com", "threshold": 530}},
    {"id": "CATALOG-7754", "title": "Catalog scenario 7754", "data": {"sku": "SKU7754", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7754@example.com", "threshold": 540}},
    {"id": "CATALOG-7755", "title": "Catalog scenario 7755", "data": {"sku": "SKU7755", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7755@example.com", "threshold": 550}},
    {"id": "CATALOG-7756", "title": "Catalog scenario 7756", "data": {"sku": "SKU7756", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7756@example.com", "threshold": 560}},
    {"id": "CATALOG-7757", "title": "Catalog scenario 7757", "data": {"sku": "SKU7757", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7757@example.com", "threshold": 570}},
    {"id": "CATALOG-7758", "title": "Catalog scenario 7758", "data": {"sku": "SKU7758", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7758@example.com", "threshold": 580}},
    {"id": "CATALOG-7759", "title": "Catalog scenario 7759", "data": {"sku": "SKU7759", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7759@example.com", "threshold": 590}},
    {"id": "CATALOG-7760", "title": "Catalog scenario 7760", "data": {"sku": "SKU7760", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7760@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
