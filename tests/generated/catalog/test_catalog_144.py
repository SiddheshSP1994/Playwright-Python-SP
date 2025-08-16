import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8591", "title": "Catalog scenario 8591", "data": {"sku": "SKU8591", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8591@example.com", "threshold": 910}},
    {"id": "CATALOG-8592", "title": "Catalog scenario 8592", "data": {"sku": "SKU8592", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8592@example.com", "threshold": 920}},
    {"id": "CATALOG-8593", "title": "Catalog scenario 8593", "data": {"sku": "SKU8593", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8593@example.com", "threshold": 930}},
    {"id": "CATALOG-8594", "title": "Catalog scenario 8594", "data": {"sku": "SKU8594", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8594@example.com", "threshold": 940}},
    {"id": "CATALOG-8595", "title": "Catalog scenario 8595", "data": {"sku": "SKU8595", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8595@example.com", "threshold": 950}},
    {"id": "CATALOG-8596", "title": "Catalog scenario 8596", "data": {"sku": "SKU8596", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8596@example.com", "threshold": 960}},
    {"id": "CATALOG-8597", "title": "Catalog scenario 8597", "data": {"sku": "SKU8597", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8597@example.com", "threshold": 970}},
    {"id": "CATALOG-8598", "title": "Catalog scenario 8598", "data": {"sku": "SKU8598", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8598@example.com", "threshold": 980}},
    {"id": "CATALOG-8599", "title": "Catalog scenario 8599", "data": {"sku": "SKU8599", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8599@example.com", "threshold": 990}},
    {"id": "CATALOG-8600", "title": "Catalog scenario 8600", "data": {"sku": "SKU8600", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8600@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
