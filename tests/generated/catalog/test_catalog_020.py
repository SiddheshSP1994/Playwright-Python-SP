import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1151", "title": "Catalog scenario 1151", "data": {"sku": "SKU1151", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1151@example.com", "threshold": 510}},
    {"id": "CATALOG-1152", "title": "Catalog scenario 1152", "data": {"sku": "SKU1152", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1152@example.com", "threshold": 520}},
    {"id": "CATALOG-1153", "title": "Catalog scenario 1153", "data": {"sku": "SKU1153", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1153@example.com", "threshold": 530}},
    {"id": "CATALOG-1154", "title": "Catalog scenario 1154", "data": {"sku": "SKU1154", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1154@example.com", "threshold": 540}},
    {"id": "CATALOG-1155", "title": "Catalog scenario 1155", "data": {"sku": "SKU1155", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1155@example.com", "threshold": 550}},
    {"id": "CATALOG-1156", "title": "Catalog scenario 1156", "data": {"sku": "SKU1156", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1156@example.com", "threshold": 560}},
    {"id": "CATALOG-1157", "title": "Catalog scenario 1157", "data": {"sku": "SKU1157", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1157@example.com", "threshold": 570}},
    {"id": "CATALOG-1158", "title": "Catalog scenario 1158", "data": {"sku": "SKU1158", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1158@example.com", "threshold": 580}},
    {"id": "CATALOG-1159", "title": "Catalog scenario 1159", "data": {"sku": "SKU1159", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1159@example.com", "threshold": 590}},
    {"id": "CATALOG-1160", "title": "Catalog scenario 1160", "data": {"sku": "SKU1160", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1160@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
