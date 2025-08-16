import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6191", "title": "Catalog scenario 6191", "data": {"sku": "SKU6191", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6191@example.com", "threshold": 910}},
    {"id": "CATALOG-6192", "title": "Catalog scenario 6192", "data": {"sku": "SKU6192", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6192@example.com", "threshold": 920}},
    {"id": "CATALOG-6193", "title": "Catalog scenario 6193", "data": {"sku": "SKU6193", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6193@example.com", "threshold": 930}},
    {"id": "CATALOG-6194", "title": "Catalog scenario 6194", "data": {"sku": "SKU6194", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6194@example.com", "threshold": 940}},
    {"id": "CATALOG-6195", "title": "Catalog scenario 6195", "data": {"sku": "SKU6195", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6195@example.com", "threshold": 950}},
    {"id": "CATALOG-6196", "title": "Catalog scenario 6196", "data": {"sku": "SKU6196", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6196@example.com", "threshold": 960}},
    {"id": "CATALOG-6197", "title": "Catalog scenario 6197", "data": {"sku": "SKU6197", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6197@example.com", "threshold": 970}},
    {"id": "CATALOG-6198", "title": "Catalog scenario 6198", "data": {"sku": "SKU6198", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6198@example.com", "threshold": 980}},
    {"id": "CATALOG-6199", "title": "Catalog scenario 6199", "data": {"sku": "SKU6199", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6199@example.com", "threshold": 990}},
    {"id": "CATALOG-6200", "title": "Catalog scenario 6200", "data": {"sku": "SKU6200", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6200@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
