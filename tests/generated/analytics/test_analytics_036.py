import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-2151", "title": "Analytics scenario 2151", "data": {"sku": "SKU2151", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2151@example.com", "threshold": 510}},
    {"id": "ANALYTICS-2152", "title": "Analytics scenario 2152", "data": {"sku": "SKU2152", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2152@example.com", "threshold": 520}},
    {"id": "ANALYTICS-2153", "title": "Analytics scenario 2153", "data": {"sku": "SKU2153", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2153@example.com", "threshold": 530}},
    {"id": "ANALYTICS-2154", "title": "Analytics scenario 2154", "data": {"sku": "SKU2154", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2154@example.com", "threshold": 540}},
    {"id": "ANALYTICS-2155", "title": "Analytics scenario 2155", "data": {"sku": "SKU2155", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2155@example.com", "threshold": 550}},
    {"id": "ANALYTICS-2156", "title": "Analytics scenario 2156", "data": {"sku": "SKU2156", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2156@example.com", "threshold": 560}},
    {"id": "ANALYTICS-2157", "title": "Analytics scenario 2157", "data": {"sku": "SKU2157", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2157@example.com", "threshold": 570}},
    {"id": "ANALYTICS-2158", "title": "Analytics scenario 2158", "data": {"sku": "SKU2158", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2158@example.com", "threshold": 580}},
    {"id": "ANALYTICS-2159", "title": "Analytics scenario 2159", "data": {"sku": "SKU2159", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2159@example.com", "threshold": 590}},
    {"id": "ANALYTICS-2160", "title": "Analytics scenario 2160", "data": {"sku": "SKU2160", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2160@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
