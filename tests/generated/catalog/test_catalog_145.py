import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8651", "title": "Catalog scenario 8651", "data": {"sku": "SKU8651", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8651@example.com", "threshold": 510}},
    {"id": "CATALOG-8652", "title": "Catalog scenario 8652", "data": {"sku": "SKU8652", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8652@example.com", "threshold": 520}},
    {"id": "CATALOG-8653", "title": "Catalog scenario 8653", "data": {"sku": "SKU8653", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8653@example.com", "threshold": 530}},
    {"id": "CATALOG-8654", "title": "Catalog scenario 8654", "data": {"sku": "SKU8654", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8654@example.com", "threshold": 540}},
    {"id": "CATALOG-8655", "title": "Catalog scenario 8655", "data": {"sku": "SKU8655", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8655@example.com", "threshold": 550}},
    {"id": "CATALOG-8656", "title": "Catalog scenario 8656", "data": {"sku": "SKU8656", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8656@example.com", "threshold": 560}},
    {"id": "CATALOG-8657", "title": "Catalog scenario 8657", "data": {"sku": "SKU8657", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8657@example.com", "threshold": 570}},
    {"id": "CATALOG-8658", "title": "Catalog scenario 8658", "data": {"sku": "SKU8658", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8658@example.com", "threshold": 580}},
    {"id": "CATALOG-8659", "title": "Catalog scenario 8659", "data": {"sku": "SKU8659", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8659@example.com", "threshold": 590}},
    {"id": "CATALOG-8660", "title": "Catalog scenario 8660", "data": {"sku": "SKU8660", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8660@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
