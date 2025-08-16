import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0431", "title": "Catalog scenario 431", "data": {"sku": "SKU431", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user431@example.com", "threshold": 310}},
    {"id": "CATALOG-0432", "title": "Catalog scenario 432", "data": {"sku": "SKU432", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user432@example.com", "threshold": 320}},
    {"id": "CATALOG-0433", "title": "Catalog scenario 433", "data": {"sku": "SKU433", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user433@example.com", "threshold": 330}},
    {"id": "CATALOG-0434", "title": "Catalog scenario 434", "data": {"sku": "SKU434", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user434@example.com", "threshold": 340}},
    {"id": "CATALOG-0435", "title": "Catalog scenario 435", "data": {"sku": "SKU435", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user435@example.com", "threshold": 350}},
    {"id": "CATALOG-0436", "title": "Catalog scenario 436", "data": {"sku": "SKU436", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user436@example.com", "threshold": 360}},
    {"id": "CATALOG-0437", "title": "Catalog scenario 437", "data": {"sku": "SKU437", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user437@example.com", "threshold": 370}},
    {"id": "CATALOG-0438", "title": "Catalog scenario 438", "data": {"sku": "SKU438", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user438@example.com", "threshold": 380}},
    {"id": "CATALOG-0439", "title": "Catalog scenario 439", "data": {"sku": "SKU439", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user439@example.com", "threshold": 390}},
    {"id": "CATALOG-0440", "title": "Catalog scenario 440", "data": {"sku": "SKU440", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user440@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
