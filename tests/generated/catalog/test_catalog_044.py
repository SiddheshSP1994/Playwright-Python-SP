import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2591", "title": "Catalog scenario 2591", "data": {"sku": "SKU2591", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2591@example.com", "threshold": 910}},
    {"id": "CATALOG-2592", "title": "Catalog scenario 2592", "data": {"sku": "SKU2592", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2592@example.com", "threshold": 920}},
    {"id": "CATALOG-2593", "title": "Catalog scenario 2593", "data": {"sku": "SKU2593", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2593@example.com", "threshold": 930}},
    {"id": "CATALOG-2594", "title": "Catalog scenario 2594", "data": {"sku": "SKU2594", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2594@example.com", "threshold": 940}},
    {"id": "CATALOG-2595", "title": "Catalog scenario 2595", "data": {"sku": "SKU2595", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2595@example.com", "threshold": 950}},
    {"id": "CATALOG-2596", "title": "Catalog scenario 2596", "data": {"sku": "SKU2596", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2596@example.com", "threshold": 960}},
    {"id": "CATALOG-2597", "title": "Catalog scenario 2597", "data": {"sku": "SKU2597", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2597@example.com", "threshold": 970}},
    {"id": "CATALOG-2598", "title": "Catalog scenario 2598", "data": {"sku": "SKU2598", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2598@example.com", "threshold": 980}},
    {"id": "CATALOG-2599", "title": "Catalog scenario 2599", "data": {"sku": "SKU2599", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2599@example.com", "threshold": 990}},
    {"id": "CATALOG-2600", "title": "Catalog scenario 2600", "data": {"sku": "SKU2600", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2600@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
