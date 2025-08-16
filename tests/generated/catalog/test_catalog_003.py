import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0131", "title": "Catalog scenario 131", "data": {"sku": "SKU131", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user131@example.com", "threshold": 310}},
    {"id": "CATALOG-0132", "title": "Catalog scenario 132", "data": {"sku": "SKU132", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user132@example.com", "threshold": 320}},
    {"id": "CATALOG-0133", "title": "Catalog scenario 133", "data": {"sku": "SKU133", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user133@example.com", "threshold": 330}},
    {"id": "CATALOG-0134", "title": "Catalog scenario 134", "data": {"sku": "SKU134", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user134@example.com", "threshold": 340}},
    {"id": "CATALOG-0135", "title": "Catalog scenario 135", "data": {"sku": "SKU135", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user135@example.com", "threshold": 350}},
    {"id": "CATALOG-0136", "title": "Catalog scenario 136", "data": {"sku": "SKU136", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user136@example.com", "threshold": 360}},
    {"id": "CATALOG-0137", "title": "Catalog scenario 137", "data": {"sku": "SKU137", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user137@example.com", "threshold": 370}},
    {"id": "CATALOG-0138", "title": "Catalog scenario 138", "data": {"sku": "SKU138", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user138@example.com", "threshold": 380}},
    {"id": "CATALOG-0139", "title": "Catalog scenario 139", "data": {"sku": "SKU139", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user139@example.com", "threshold": 390}},
    {"id": "CATALOG-0140", "title": "Catalog scenario 140", "data": {"sku": "SKU140", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user140@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
