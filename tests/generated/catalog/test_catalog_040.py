import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2351", "title": "Catalog scenario 2351", "data": {"sku": "SKU2351", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2351@example.com", "threshold": 510}},
    {"id": "CATALOG-2352", "title": "Catalog scenario 2352", "data": {"sku": "SKU2352", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2352@example.com", "threshold": 520}},
    {"id": "CATALOG-2353", "title": "Catalog scenario 2353", "data": {"sku": "SKU2353", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2353@example.com", "threshold": 530}},
    {"id": "CATALOG-2354", "title": "Catalog scenario 2354", "data": {"sku": "SKU2354", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2354@example.com", "threshold": 540}},
    {"id": "CATALOG-2355", "title": "Catalog scenario 2355", "data": {"sku": "SKU2355", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2355@example.com", "threshold": 550}},
    {"id": "CATALOG-2356", "title": "Catalog scenario 2356", "data": {"sku": "SKU2356", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2356@example.com", "threshold": 560}},
    {"id": "CATALOG-2357", "title": "Catalog scenario 2357", "data": {"sku": "SKU2357", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2357@example.com", "threshold": 570}},
    {"id": "CATALOG-2358", "title": "Catalog scenario 2358", "data": {"sku": "SKU2358", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2358@example.com", "threshold": 580}},
    {"id": "CATALOG-2359", "title": "Catalog scenario 2359", "data": {"sku": "SKU2359", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2359@example.com", "threshold": 590}},
    {"id": "CATALOG-2360", "title": "Catalog scenario 2360", "data": {"sku": "SKU2360", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2360@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
