import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0491", "title": "Catalog scenario 491", "data": {"sku": "SKU491", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user491@example.com", "threshold": 910}},
    {"id": "CATALOG-0492", "title": "Catalog scenario 492", "data": {"sku": "SKU492", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user492@example.com", "threshold": 920}},
    {"id": "CATALOG-0493", "title": "Catalog scenario 493", "data": {"sku": "SKU493", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user493@example.com", "threshold": 930}},
    {"id": "CATALOG-0494", "title": "Catalog scenario 494", "data": {"sku": "SKU494", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user494@example.com", "threshold": 940}},
    {"id": "CATALOG-0495", "title": "Catalog scenario 495", "data": {"sku": "SKU495", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user495@example.com", "threshold": 950}},
    {"id": "CATALOG-0496", "title": "Catalog scenario 496", "data": {"sku": "SKU496", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user496@example.com", "threshold": 960}},
    {"id": "CATALOG-0497", "title": "Catalog scenario 497", "data": {"sku": "SKU497", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user497@example.com", "threshold": 970}},
    {"id": "CATALOG-0498", "title": "Catalog scenario 498", "data": {"sku": "SKU498", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user498@example.com", "threshold": 980}},
    {"id": "CATALOG-0499", "title": "Catalog scenario 499", "data": {"sku": "SKU499", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user499@example.com", "threshold": 990}},
    {"id": "CATALOG-0500", "title": "Catalog scenario 500", "data": {"sku": "SKU500", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user500@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
