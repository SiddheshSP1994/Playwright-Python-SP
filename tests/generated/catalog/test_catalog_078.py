import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4631", "title": "Catalog scenario 4631", "data": {"sku": "SKU4631", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4631@example.com", "threshold": 310}},
    {"id": "CATALOG-4632", "title": "Catalog scenario 4632", "data": {"sku": "SKU4632", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4632@example.com", "threshold": 320}},
    {"id": "CATALOG-4633", "title": "Catalog scenario 4633", "data": {"sku": "SKU4633", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4633@example.com", "threshold": 330}},
    {"id": "CATALOG-4634", "title": "Catalog scenario 4634", "data": {"sku": "SKU4634", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4634@example.com", "threshold": 340}},
    {"id": "CATALOG-4635", "title": "Catalog scenario 4635", "data": {"sku": "SKU4635", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4635@example.com", "threshold": 350}},
    {"id": "CATALOG-4636", "title": "Catalog scenario 4636", "data": {"sku": "SKU4636", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4636@example.com", "threshold": 360}},
    {"id": "CATALOG-4637", "title": "Catalog scenario 4637", "data": {"sku": "SKU4637", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4637@example.com", "threshold": 370}},
    {"id": "CATALOG-4638", "title": "Catalog scenario 4638", "data": {"sku": "SKU4638", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4638@example.com", "threshold": 380}},
    {"id": "CATALOG-4639", "title": "Catalog scenario 4639", "data": {"sku": "SKU4639", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4639@example.com", "threshold": 390}},
    {"id": "CATALOG-4640", "title": "Catalog scenario 4640", "data": {"sku": "SKU4640", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4640@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
