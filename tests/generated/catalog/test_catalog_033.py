import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1931", "title": "Catalog scenario 1931", "data": {"sku": "SKU1931", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1931@example.com", "threshold": 310}},
    {"id": "CATALOG-1932", "title": "Catalog scenario 1932", "data": {"sku": "SKU1932", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1932@example.com", "threshold": 320}},
    {"id": "CATALOG-1933", "title": "Catalog scenario 1933", "data": {"sku": "SKU1933", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1933@example.com", "threshold": 330}},
    {"id": "CATALOG-1934", "title": "Catalog scenario 1934", "data": {"sku": "SKU1934", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1934@example.com", "threshold": 340}},
    {"id": "CATALOG-1935", "title": "Catalog scenario 1935", "data": {"sku": "SKU1935", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1935@example.com", "threshold": 350}},
    {"id": "CATALOG-1936", "title": "Catalog scenario 1936", "data": {"sku": "SKU1936", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1936@example.com", "threshold": 360}},
    {"id": "CATALOG-1937", "title": "Catalog scenario 1937", "data": {"sku": "SKU1937", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1937@example.com", "threshold": 370}},
    {"id": "CATALOG-1938", "title": "Catalog scenario 1938", "data": {"sku": "SKU1938", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1938@example.com", "threshold": 380}},
    {"id": "CATALOG-1939", "title": "Catalog scenario 1939", "data": {"sku": "SKU1939", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1939@example.com", "threshold": 390}},
    {"id": "CATALOG-1940", "title": "Catalog scenario 1940", "data": {"sku": "SKU1940", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1940@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
