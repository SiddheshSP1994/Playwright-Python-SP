import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4091", "title": "Catalog scenario 4091", "data": {"sku": "SKU4091", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4091@example.com", "threshold": 910}},
    {"id": "CATALOG-4092", "title": "Catalog scenario 4092", "data": {"sku": "SKU4092", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4092@example.com", "threshold": 920}},
    {"id": "CATALOG-4093", "title": "Catalog scenario 4093", "data": {"sku": "SKU4093", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4093@example.com", "threshold": 930}},
    {"id": "CATALOG-4094", "title": "Catalog scenario 4094", "data": {"sku": "SKU4094", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4094@example.com", "threshold": 940}},
    {"id": "CATALOG-4095", "title": "Catalog scenario 4095", "data": {"sku": "SKU4095", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4095@example.com", "threshold": 950}},
    {"id": "CATALOG-4096", "title": "Catalog scenario 4096", "data": {"sku": "SKU4096", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4096@example.com", "threshold": 960}},
    {"id": "CATALOG-4097", "title": "Catalog scenario 4097", "data": {"sku": "SKU4097", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4097@example.com", "threshold": 970}},
    {"id": "CATALOG-4098", "title": "Catalog scenario 4098", "data": {"sku": "SKU4098", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4098@example.com", "threshold": 980}},
    {"id": "CATALOG-4099", "title": "Catalog scenario 4099", "data": {"sku": "SKU4099", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4099@example.com", "threshold": 990}},
    {"id": "CATALOG-4100", "title": "Catalog scenario 4100", "data": {"sku": "SKU4100", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4100@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
