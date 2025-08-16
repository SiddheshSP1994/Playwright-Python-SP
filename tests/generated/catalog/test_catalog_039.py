import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2291", "title": "Catalog scenario 2291", "data": {"sku": "SKU2291", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2291@example.com", "threshold": 910}},
    {"id": "CATALOG-2292", "title": "Catalog scenario 2292", "data": {"sku": "SKU2292", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2292@example.com", "threshold": 920}},
    {"id": "CATALOG-2293", "title": "Catalog scenario 2293", "data": {"sku": "SKU2293", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2293@example.com", "threshold": 930}},
    {"id": "CATALOG-2294", "title": "Catalog scenario 2294", "data": {"sku": "SKU2294", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2294@example.com", "threshold": 940}},
    {"id": "CATALOG-2295", "title": "Catalog scenario 2295", "data": {"sku": "SKU2295", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2295@example.com", "threshold": 950}},
    {"id": "CATALOG-2296", "title": "Catalog scenario 2296", "data": {"sku": "SKU2296", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2296@example.com", "threshold": 960}},
    {"id": "CATALOG-2297", "title": "Catalog scenario 2297", "data": {"sku": "SKU2297", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2297@example.com", "threshold": 970}},
    {"id": "CATALOG-2298", "title": "Catalog scenario 2298", "data": {"sku": "SKU2298", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2298@example.com", "threshold": 980}},
    {"id": "CATALOG-2299", "title": "Catalog scenario 2299", "data": {"sku": "SKU2299", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2299@example.com", "threshold": 990}},
    {"id": "CATALOG-2300", "title": "Catalog scenario 2300", "data": {"sku": "SKU2300", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2300@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
