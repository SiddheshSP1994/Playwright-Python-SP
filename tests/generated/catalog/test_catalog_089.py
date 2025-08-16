import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5291", "title": "Catalog scenario 5291", "data": {"sku": "SKU5291", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5291@example.com", "threshold": 910}},
    {"id": "CATALOG-5292", "title": "Catalog scenario 5292", "data": {"sku": "SKU5292", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5292@example.com", "threshold": 920}},
    {"id": "CATALOG-5293", "title": "Catalog scenario 5293", "data": {"sku": "SKU5293", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5293@example.com", "threshold": 930}},
    {"id": "CATALOG-5294", "title": "Catalog scenario 5294", "data": {"sku": "SKU5294", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5294@example.com", "threshold": 940}},
    {"id": "CATALOG-5295", "title": "Catalog scenario 5295", "data": {"sku": "SKU5295", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5295@example.com", "threshold": 950}},
    {"id": "CATALOG-5296", "title": "Catalog scenario 5296", "data": {"sku": "SKU5296", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5296@example.com", "threshold": 960}},
    {"id": "CATALOG-5297", "title": "Catalog scenario 5297", "data": {"sku": "SKU5297", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5297@example.com", "threshold": 970}},
    {"id": "CATALOG-5298", "title": "Catalog scenario 5298", "data": {"sku": "SKU5298", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5298@example.com", "threshold": 980}},
    {"id": "CATALOG-5299", "title": "Catalog scenario 5299", "data": {"sku": "SKU5299", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5299@example.com", "threshold": 990}},
    {"id": "CATALOG-5300", "title": "Catalog scenario 5300", "data": {"sku": "SKU5300", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5300@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
