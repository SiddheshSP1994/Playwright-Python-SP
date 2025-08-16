import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1631", "title": "Catalog scenario 1631", "data": {"sku": "SKU1631", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1631@example.com", "threshold": 310}},
    {"id": "CATALOG-1632", "title": "Catalog scenario 1632", "data": {"sku": "SKU1632", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1632@example.com", "threshold": 320}},
    {"id": "CATALOG-1633", "title": "Catalog scenario 1633", "data": {"sku": "SKU1633", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1633@example.com", "threshold": 330}},
    {"id": "CATALOG-1634", "title": "Catalog scenario 1634", "data": {"sku": "SKU1634", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1634@example.com", "threshold": 340}},
    {"id": "CATALOG-1635", "title": "Catalog scenario 1635", "data": {"sku": "SKU1635", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1635@example.com", "threshold": 350}},
    {"id": "CATALOG-1636", "title": "Catalog scenario 1636", "data": {"sku": "SKU1636", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1636@example.com", "threshold": 360}},
    {"id": "CATALOG-1637", "title": "Catalog scenario 1637", "data": {"sku": "SKU1637", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1637@example.com", "threshold": 370}},
    {"id": "CATALOG-1638", "title": "Catalog scenario 1638", "data": {"sku": "SKU1638", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1638@example.com", "threshold": 380}},
    {"id": "CATALOG-1639", "title": "Catalog scenario 1639", "data": {"sku": "SKU1639", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1639@example.com", "threshold": 390}},
    {"id": "CATALOG-1640", "title": "Catalog scenario 1640", "data": {"sku": "SKU1640", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1640@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
