import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2051", "title": "Catalog scenario 2051", "data": {"sku": "SKU2051", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2051@example.com", "threshold": 510}},
    {"id": "CATALOG-2052", "title": "Catalog scenario 2052", "data": {"sku": "SKU2052", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2052@example.com", "threshold": 520}},
    {"id": "CATALOG-2053", "title": "Catalog scenario 2053", "data": {"sku": "SKU2053", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2053@example.com", "threshold": 530}},
    {"id": "CATALOG-2054", "title": "Catalog scenario 2054", "data": {"sku": "SKU2054", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2054@example.com", "threshold": 540}},
    {"id": "CATALOG-2055", "title": "Catalog scenario 2055", "data": {"sku": "SKU2055", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2055@example.com", "threshold": 550}},
    {"id": "CATALOG-2056", "title": "Catalog scenario 2056", "data": {"sku": "SKU2056", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2056@example.com", "threshold": 560}},
    {"id": "CATALOG-2057", "title": "Catalog scenario 2057", "data": {"sku": "SKU2057", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2057@example.com", "threshold": 570}},
    {"id": "CATALOG-2058", "title": "Catalog scenario 2058", "data": {"sku": "SKU2058", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2058@example.com", "threshold": 580}},
    {"id": "CATALOG-2059", "title": "Catalog scenario 2059", "data": {"sku": "SKU2059", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2059@example.com", "threshold": 590}},
    {"id": "CATALOG-2060", "title": "Catalog scenario 2060", "data": {"sku": "SKU2060", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2060@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
