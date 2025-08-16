import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2651", "title": "Catalog scenario 2651", "data": {"sku": "SKU2651", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2651@example.com", "threshold": 510}},
    {"id": "CATALOG-2652", "title": "Catalog scenario 2652", "data": {"sku": "SKU2652", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2652@example.com", "threshold": 520}},
    {"id": "CATALOG-2653", "title": "Catalog scenario 2653", "data": {"sku": "SKU2653", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2653@example.com", "threshold": 530}},
    {"id": "CATALOG-2654", "title": "Catalog scenario 2654", "data": {"sku": "SKU2654", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2654@example.com", "threshold": 540}},
    {"id": "CATALOG-2655", "title": "Catalog scenario 2655", "data": {"sku": "SKU2655", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2655@example.com", "threshold": 550}},
    {"id": "CATALOG-2656", "title": "Catalog scenario 2656", "data": {"sku": "SKU2656", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2656@example.com", "threshold": 560}},
    {"id": "CATALOG-2657", "title": "Catalog scenario 2657", "data": {"sku": "SKU2657", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2657@example.com", "threshold": 570}},
    {"id": "CATALOG-2658", "title": "Catalog scenario 2658", "data": {"sku": "SKU2658", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2658@example.com", "threshold": 580}},
    {"id": "CATALOG-2659", "title": "Catalog scenario 2659", "data": {"sku": "SKU2659", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2659@example.com", "threshold": 590}},
    {"id": "CATALOG-2660", "title": "Catalog scenario 2660", "data": {"sku": "SKU2660", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2660@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
