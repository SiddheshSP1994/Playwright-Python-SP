import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-7991", "title": "Catalog scenario 7991", "data": {"sku": "SKU7991", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7991@example.com", "threshold": 910}},
    {"id": "CATALOG-7992", "title": "Catalog scenario 7992", "data": {"sku": "SKU7992", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7992@example.com", "threshold": 920}},
    {"id": "CATALOG-7993", "title": "Catalog scenario 7993", "data": {"sku": "SKU7993", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7993@example.com", "threshold": 930}},
    {"id": "CATALOG-7994", "title": "Catalog scenario 7994", "data": {"sku": "SKU7994", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7994@example.com", "threshold": 940}},
    {"id": "CATALOG-7995", "title": "Catalog scenario 7995", "data": {"sku": "SKU7995", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7995@example.com", "threshold": 950}},
    {"id": "CATALOG-7996", "title": "Catalog scenario 7996", "data": {"sku": "SKU7996", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7996@example.com", "threshold": 960}},
    {"id": "CATALOG-7997", "title": "Catalog scenario 7997", "data": {"sku": "SKU7997", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7997@example.com", "threshold": 970}},
    {"id": "CATALOG-7998", "title": "Catalog scenario 7998", "data": {"sku": "SKU7998", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7998@example.com", "threshold": 980}},
    {"id": "CATALOG-7999", "title": "Catalog scenario 7999", "data": {"sku": "SKU7999", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7999@example.com", "threshold": 990}},
    {"id": "CATALOG-8000", "title": "Catalog scenario 8000", "data": {"sku": "SKU8000", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8000@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
