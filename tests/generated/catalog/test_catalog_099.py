import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5891", "title": "Catalog scenario 5891", "data": {"sku": "SKU5891", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5891@example.com", "threshold": 910}},
    {"id": "CATALOG-5892", "title": "Catalog scenario 5892", "data": {"sku": "SKU5892", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5892@example.com", "threshold": 920}},
    {"id": "CATALOG-5893", "title": "Catalog scenario 5893", "data": {"sku": "SKU5893", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5893@example.com", "threshold": 930}},
    {"id": "CATALOG-5894", "title": "Catalog scenario 5894", "data": {"sku": "SKU5894", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5894@example.com", "threshold": 940}},
    {"id": "CATALOG-5895", "title": "Catalog scenario 5895", "data": {"sku": "SKU5895", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5895@example.com", "threshold": 950}},
    {"id": "CATALOG-5896", "title": "Catalog scenario 5896", "data": {"sku": "SKU5896", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5896@example.com", "threshold": 960}},
    {"id": "CATALOG-5897", "title": "Catalog scenario 5897", "data": {"sku": "SKU5897", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5897@example.com", "threshold": 970}},
    {"id": "CATALOG-5898", "title": "Catalog scenario 5898", "data": {"sku": "SKU5898", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5898@example.com", "threshold": 980}},
    {"id": "CATALOG-5899", "title": "Catalog scenario 5899", "data": {"sku": "SKU5899", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5899@example.com", "threshold": 990}},
    {"id": "CATALOG-5900", "title": "Catalog scenario 5900", "data": {"sku": "SKU5900", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5900@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
