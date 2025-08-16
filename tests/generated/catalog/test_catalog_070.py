import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4151", "title": "Catalog scenario 4151", "data": {"sku": "SKU4151", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4151@example.com", "threshold": 510}},
    {"id": "CATALOG-4152", "title": "Catalog scenario 4152", "data": {"sku": "SKU4152", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4152@example.com", "threshold": 520}},
    {"id": "CATALOG-4153", "title": "Catalog scenario 4153", "data": {"sku": "SKU4153", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4153@example.com", "threshold": 530}},
    {"id": "CATALOG-4154", "title": "Catalog scenario 4154", "data": {"sku": "SKU4154", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4154@example.com", "threshold": 540}},
    {"id": "CATALOG-4155", "title": "Catalog scenario 4155", "data": {"sku": "SKU4155", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4155@example.com", "threshold": 550}},
    {"id": "CATALOG-4156", "title": "Catalog scenario 4156", "data": {"sku": "SKU4156", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4156@example.com", "threshold": 560}},
    {"id": "CATALOG-4157", "title": "Catalog scenario 4157", "data": {"sku": "SKU4157", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4157@example.com", "threshold": 570}},
    {"id": "CATALOG-4158", "title": "Catalog scenario 4158", "data": {"sku": "SKU4158", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4158@example.com", "threshold": 580}},
    {"id": "CATALOG-4159", "title": "Catalog scenario 4159", "data": {"sku": "SKU4159", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4159@example.com", "threshold": 590}},
    {"id": "CATALOG-4160", "title": "Catalog scenario 4160", "data": {"sku": "SKU4160", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4160@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
