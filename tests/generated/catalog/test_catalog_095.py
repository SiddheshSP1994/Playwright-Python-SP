import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5651", "title": "Catalog scenario 5651", "data": {"sku": "SKU5651", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5651@example.com", "threshold": 510}},
    {"id": "CATALOG-5652", "title": "Catalog scenario 5652", "data": {"sku": "SKU5652", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5652@example.com", "threshold": 520}},
    {"id": "CATALOG-5653", "title": "Catalog scenario 5653", "data": {"sku": "SKU5653", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5653@example.com", "threshold": 530}},
    {"id": "CATALOG-5654", "title": "Catalog scenario 5654", "data": {"sku": "SKU5654", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5654@example.com", "threshold": 540}},
    {"id": "CATALOG-5655", "title": "Catalog scenario 5655", "data": {"sku": "SKU5655", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5655@example.com", "threshold": 550}},
    {"id": "CATALOG-5656", "title": "Catalog scenario 5656", "data": {"sku": "SKU5656", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5656@example.com", "threshold": 560}},
    {"id": "CATALOG-5657", "title": "Catalog scenario 5657", "data": {"sku": "SKU5657", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5657@example.com", "threshold": 570}},
    {"id": "CATALOG-5658", "title": "Catalog scenario 5658", "data": {"sku": "SKU5658", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5658@example.com", "threshold": 580}},
    {"id": "CATALOG-5659", "title": "Catalog scenario 5659", "data": {"sku": "SKU5659", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5659@example.com", "threshold": 590}},
    {"id": "CATALOG-5660", "title": "Catalog scenario 5660", "data": {"sku": "SKU5660", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5660@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
