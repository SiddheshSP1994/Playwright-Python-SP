import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-9791", "title": "Catalog scenario 9791", "data": {"sku": "SKU9791", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9791@example.com", "threshold": 910}},
    {"id": "CATALOG-9792", "title": "Catalog scenario 9792", "data": {"sku": "SKU9792", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9792@example.com", "threshold": 920}},
    {"id": "CATALOG-9793", "title": "Catalog scenario 9793", "data": {"sku": "SKU9793", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9793@example.com", "threshold": 930}},
    {"id": "CATALOG-9794", "title": "Catalog scenario 9794", "data": {"sku": "SKU9794", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9794@example.com", "threshold": 940}},
    {"id": "CATALOG-9795", "title": "Catalog scenario 9795", "data": {"sku": "SKU9795", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9795@example.com", "threshold": 950}},
    {"id": "CATALOG-9796", "title": "Catalog scenario 9796", "data": {"sku": "SKU9796", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9796@example.com", "threshold": 960}},
    {"id": "CATALOG-9797", "title": "Catalog scenario 9797", "data": {"sku": "SKU9797", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9797@example.com", "threshold": 970}},
    {"id": "CATALOG-9798", "title": "Catalog scenario 9798", "data": {"sku": "SKU9798", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9798@example.com", "threshold": 980}},
    {"id": "CATALOG-9799", "title": "Catalog scenario 9799", "data": {"sku": "SKU9799", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9799@example.com", "threshold": 990}},
    {"id": "CATALOG-9800", "title": "Catalog scenario 9800", "data": {"sku": "SKU9800", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9800@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
