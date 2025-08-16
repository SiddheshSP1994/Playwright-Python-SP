import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-9011", "title": "Catalog scenario 9011", "data": {"sku": "SKU9011", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9011@example.com", "threshold": 110}},
    {"id": "CATALOG-9012", "title": "Catalog scenario 9012", "data": {"sku": "SKU9012", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9012@example.com", "threshold": 120}},
    {"id": "CATALOG-9013", "title": "Catalog scenario 9013", "data": {"sku": "SKU9013", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9013@example.com", "threshold": 130}},
    {"id": "CATALOG-9014", "title": "Catalog scenario 9014", "data": {"sku": "SKU9014", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9014@example.com", "threshold": 140}},
    {"id": "CATALOG-9015", "title": "Catalog scenario 9015", "data": {"sku": "SKU9015", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9015@example.com", "threshold": 150}},
    {"id": "CATALOG-9016", "title": "Catalog scenario 9016", "data": {"sku": "SKU9016", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9016@example.com", "threshold": 160}},
    {"id": "CATALOG-9017", "title": "Catalog scenario 9017", "data": {"sku": "SKU9017", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9017@example.com", "threshold": 170}},
    {"id": "CATALOG-9018", "title": "Catalog scenario 9018", "data": {"sku": "SKU9018", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9018@example.com", "threshold": 180}},
    {"id": "CATALOG-9019", "title": "Catalog scenario 9019", "data": {"sku": "SKU9019", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9019@example.com", "threshold": 190}},
    {"id": "CATALOG-9020", "title": "Catalog scenario 9020", "data": {"sku": "SKU9020", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9020@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
