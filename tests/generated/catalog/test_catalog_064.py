import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3791", "title": "Catalog scenario 3791", "data": {"sku": "SKU3791", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3791@example.com", "threshold": 910}},
    {"id": "CATALOG-3792", "title": "Catalog scenario 3792", "data": {"sku": "SKU3792", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3792@example.com", "threshold": 920}},
    {"id": "CATALOG-3793", "title": "Catalog scenario 3793", "data": {"sku": "SKU3793", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3793@example.com", "threshold": 930}},
    {"id": "CATALOG-3794", "title": "Catalog scenario 3794", "data": {"sku": "SKU3794", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3794@example.com", "threshold": 940}},
    {"id": "CATALOG-3795", "title": "Catalog scenario 3795", "data": {"sku": "SKU3795", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3795@example.com", "threshold": 950}},
    {"id": "CATALOG-3796", "title": "Catalog scenario 3796", "data": {"sku": "SKU3796", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3796@example.com", "threshold": 960}},
    {"id": "CATALOG-3797", "title": "Catalog scenario 3797", "data": {"sku": "SKU3797", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3797@example.com", "threshold": 970}},
    {"id": "CATALOG-3798", "title": "Catalog scenario 3798", "data": {"sku": "SKU3798", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3798@example.com", "threshold": 980}},
    {"id": "CATALOG-3799", "title": "Catalog scenario 3799", "data": {"sku": "SKU3799", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3799@example.com", "threshold": 990}},
    {"id": "CATALOG-3800", "title": "Catalog scenario 3800", "data": {"sku": "SKU3800", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3800@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
