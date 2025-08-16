import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5591", "title": "Catalog scenario 5591", "data": {"sku": "SKU5591", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5591@example.com", "threshold": 910}},
    {"id": "CATALOG-5592", "title": "Catalog scenario 5592", "data": {"sku": "SKU5592", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5592@example.com", "threshold": 920}},
    {"id": "CATALOG-5593", "title": "Catalog scenario 5593", "data": {"sku": "SKU5593", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5593@example.com", "threshold": 930}},
    {"id": "CATALOG-5594", "title": "Catalog scenario 5594", "data": {"sku": "SKU5594", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5594@example.com", "threshold": 940}},
    {"id": "CATALOG-5595", "title": "Catalog scenario 5595", "data": {"sku": "SKU5595", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5595@example.com", "threshold": 950}},
    {"id": "CATALOG-5596", "title": "Catalog scenario 5596", "data": {"sku": "SKU5596", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5596@example.com", "threshold": 960}},
    {"id": "CATALOG-5597", "title": "Catalog scenario 5597", "data": {"sku": "SKU5597", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5597@example.com", "threshold": 970}},
    {"id": "CATALOG-5598", "title": "Catalog scenario 5598", "data": {"sku": "SKU5598", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5598@example.com", "threshold": 980}},
    {"id": "CATALOG-5599", "title": "Catalog scenario 5599", "data": {"sku": "SKU5599", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5599@example.com", "threshold": 990}},
    {"id": "CATALOG-5600", "title": "Catalog scenario 5600", "data": {"sku": "SKU5600", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5600@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
