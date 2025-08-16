import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-7631", "title": "Catalog scenario 7631", "data": {"sku": "SKU7631", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7631@example.com", "threshold": 310}},
    {"id": "CATALOG-7632", "title": "Catalog scenario 7632", "data": {"sku": "SKU7632", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7632@example.com", "threshold": 320}},
    {"id": "CATALOG-7633", "title": "Catalog scenario 7633", "data": {"sku": "SKU7633", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7633@example.com", "threshold": 330}},
    {"id": "CATALOG-7634", "title": "Catalog scenario 7634", "data": {"sku": "SKU7634", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7634@example.com", "threshold": 340}},
    {"id": "CATALOG-7635", "title": "Catalog scenario 7635", "data": {"sku": "SKU7635", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7635@example.com", "threshold": 350}},
    {"id": "CATALOG-7636", "title": "Catalog scenario 7636", "data": {"sku": "SKU7636", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7636@example.com", "threshold": 360}},
    {"id": "CATALOG-7637", "title": "Catalog scenario 7637", "data": {"sku": "SKU7637", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7637@example.com", "threshold": 370}},
    {"id": "CATALOG-7638", "title": "Catalog scenario 7638", "data": {"sku": "SKU7638", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7638@example.com", "threshold": 380}},
    {"id": "CATALOG-7639", "title": "Catalog scenario 7639", "data": {"sku": "SKU7639", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7639@example.com", "threshold": 390}},
    {"id": "CATALOG-7640", "title": "Catalog scenario 7640", "data": {"sku": "SKU7640", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7640@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
