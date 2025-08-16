import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6011", "title": "Catalog scenario 6011", "data": {"sku": "SKU6011", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6011@example.com", "threshold": 110}},
    {"id": "CATALOG-6012", "title": "Catalog scenario 6012", "data": {"sku": "SKU6012", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6012@example.com", "threshold": 120}},
    {"id": "CATALOG-6013", "title": "Catalog scenario 6013", "data": {"sku": "SKU6013", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6013@example.com", "threshold": 130}},
    {"id": "CATALOG-6014", "title": "Catalog scenario 6014", "data": {"sku": "SKU6014", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6014@example.com", "threshold": 140}},
    {"id": "CATALOG-6015", "title": "Catalog scenario 6015", "data": {"sku": "SKU6015", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6015@example.com", "threshold": 150}},
    {"id": "CATALOG-6016", "title": "Catalog scenario 6016", "data": {"sku": "SKU6016", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6016@example.com", "threshold": 160}},
    {"id": "CATALOG-6017", "title": "Catalog scenario 6017", "data": {"sku": "SKU6017", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6017@example.com", "threshold": 170}},
    {"id": "CATALOG-6018", "title": "Catalog scenario 6018", "data": {"sku": "SKU6018", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6018@example.com", "threshold": 180}},
    {"id": "CATALOG-6019", "title": "Catalog scenario 6019", "data": {"sku": "SKU6019", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6019@example.com", "threshold": 190}},
    {"id": "CATALOG-6020", "title": "Catalog scenario 6020", "data": {"sku": "SKU6020", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6020@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
