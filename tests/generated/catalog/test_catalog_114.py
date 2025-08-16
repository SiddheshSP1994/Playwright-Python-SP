import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6791", "title": "Catalog scenario 6791", "data": {"sku": "SKU6791", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6791@example.com", "threshold": 910}},
    {"id": "CATALOG-6792", "title": "Catalog scenario 6792", "data": {"sku": "SKU6792", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6792@example.com", "threshold": 920}},
    {"id": "CATALOG-6793", "title": "Catalog scenario 6793", "data": {"sku": "SKU6793", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6793@example.com", "threshold": 930}},
    {"id": "CATALOG-6794", "title": "Catalog scenario 6794", "data": {"sku": "SKU6794", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6794@example.com", "threshold": 940}},
    {"id": "CATALOG-6795", "title": "Catalog scenario 6795", "data": {"sku": "SKU6795", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6795@example.com", "threshold": 950}},
    {"id": "CATALOG-6796", "title": "Catalog scenario 6796", "data": {"sku": "SKU6796", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6796@example.com", "threshold": 960}},
    {"id": "CATALOG-6797", "title": "Catalog scenario 6797", "data": {"sku": "SKU6797", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6797@example.com", "threshold": 970}},
    {"id": "CATALOG-6798", "title": "Catalog scenario 6798", "data": {"sku": "SKU6798", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6798@example.com", "threshold": 980}},
    {"id": "CATALOG-6799", "title": "Catalog scenario 6799", "data": {"sku": "SKU6799", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6799@example.com", "threshold": 990}},
    {"id": "CATALOG-6800", "title": "Catalog scenario 6800", "data": {"sku": "SKU6800", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6800@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
