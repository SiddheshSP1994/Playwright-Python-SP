import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8151", "title": "Analytics scenario 8151", "data": {"sku": "SKU8151", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8151@example.com", "threshold": 510}},
    {"id": "ANALYTICS-8152", "title": "Analytics scenario 8152", "data": {"sku": "SKU8152", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8152@example.com", "threshold": 520}},
    {"id": "ANALYTICS-8153", "title": "Analytics scenario 8153", "data": {"sku": "SKU8153", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8153@example.com", "threshold": 530}},
    {"id": "ANALYTICS-8154", "title": "Analytics scenario 8154", "data": {"sku": "SKU8154", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8154@example.com", "threshold": 540}},
    {"id": "ANALYTICS-8155", "title": "Analytics scenario 8155", "data": {"sku": "SKU8155", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8155@example.com", "threshold": 550}},
    {"id": "ANALYTICS-8156", "title": "Analytics scenario 8156", "data": {"sku": "SKU8156", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8156@example.com", "threshold": 560}},
    {"id": "ANALYTICS-8157", "title": "Analytics scenario 8157", "data": {"sku": "SKU8157", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8157@example.com", "threshold": 570}},
    {"id": "ANALYTICS-8158", "title": "Analytics scenario 8158", "data": {"sku": "SKU8158", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8158@example.com", "threshold": 580}},
    {"id": "ANALYTICS-8159", "title": "Analytics scenario 8159", "data": {"sku": "SKU8159", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8159@example.com", "threshold": 590}},
    {"id": "ANALYTICS-8160", "title": "Analytics scenario 8160", "data": {"sku": "SKU8160", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8160@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
