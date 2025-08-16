import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0191", "title": "Catalog scenario 191", "data": {"sku": "SKU191", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user191@example.com", "threshold": 910}},
    {"id": "CATALOG-0192", "title": "Catalog scenario 192", "data": {"sku": "SKU192", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user192@example.com", "threshold": 920}},
    {"id": "CATALOG-0193", "title": "Catalog scenario 193", "data": {"sku": "SKU193", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user193@example.com", "threshold": 930}},
    {"id": "CATALOG-0194", "title": "Catalog scenario 194", "data": {"sku": "SKU194", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user194@example.com", "threshold": 940}},
    {"id": "CATALOG-0195", "title": "Catalog scenario 195", "data": {"sku": "SKU195", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user195@example.com", "threshold": 950}},
    {"id": "CATALOG-0196", "title": "Catalog scenario 196", "data": {"sku": "SKU196", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user196@example.com", "threshold": 960}},
    {"id": "CATALOG-0197", "title": "Catalog scenario 197", "data": {"sku": "SKU197", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user197@example.com", "threshold": 970}},
    {"id": "CATALOG-0198", "title": "Catalog scenario 198", "data": {"sku": "SKU198", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user198@example.com", "threshold": 980}},
    {"id": "CATALOG-0199", "title": "Catalog scenario 199", "data": {"sku": "SKU199", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user199@example.com", "threshold": 990}},
    {"id": "CATALOG-0200", "title": "Catalog scenario 200", "data": {"sku": "SKU200", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user200@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
