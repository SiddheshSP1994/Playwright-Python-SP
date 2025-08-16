import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8891", "title": "Catalog scenario 8891", "data": {"sku": "SKU8891", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8891@example.com", "threshold": 910}},
    {"id": "CATALOG-8892", "title": "Catalog scenario 8892", "data": {"sku": "SKU8892", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8892@example.com", "threshold": 920}},
    {"id": "CATALOG-8893", "title": "Catalog scenario 8893", "data": {"sku": "SKU8893", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8893@example.com", "threshold": 930}},
    {"id": "CATALOG-8894", "title": "Catalog scenario 8894", "data": {"sku": "SKU8894", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8894@example.com", "threshold": 940}},
    {"id": "CATALOG-8895", "title": "Catalog scenario 8895", "data": {"sku": "SKU8895", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8895@example.com", "threshold": 950}},
    {"id": "CATALOG-8896", "title": "Catalog scenario 8896", "data": {"sku": "SKU8896", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8896@example.com", "threshold": 960}},
    {"id": "CATALOG-8897", "title": "Catalog scenario 8897", "data": {"sku": "SKU8897", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8897@example.com", "threshold": 970}},
    {"id": "CATALOG-8898", "title": "Catalog scenario 8898", "data": {"sku": "SKU8898", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8898@example.com", "threshold": 980}},
    {"id": "CATALOG-8899", "title": "Catalog scenario 8899", "data": {"sku": "SKU8899", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8899@example.com", "threshold": 990}},
    {"id": "CATALOG-8900", "title": "Catalog scenario 8900", "data": {"sku": "SKU8900", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8900@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
