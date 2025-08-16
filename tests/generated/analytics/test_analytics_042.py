import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-2511", "title": "Analytics scenario 2511", "data": {"sku": "SKU2511", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2511@example.com", "threshold": 110}},
    {"id": "ANALYTICS-2512", "title": "Analytics scenario 2512", "data": {"sku": "SKU2512", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2512@example.com", "threshold": 120}},
    {"id": "ANALYTICS-2513", "title": "Analytics scenario 2513", "data": {"sku": "SKU2513", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2513@example.com", "threshold": 130}},
    {"id": "ANALYTICS-2514", "title": "Analytics scenario 2514", "data": {"sku": "SKU2514", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2514@example.com", "threshold": 140}},
    {"id": "ANALYTICS-2515", "title": "Analytics scenario 2515", "data": {"sku": "SKU2515", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2515@example.com", "threshold": 150}},
    {"id": "ANALYTICS-2516", "title": "Analytics scenario 2516", "data": {"sku": "SKU2516", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2516@example.com", "threshold": 160}},
    {"id": "ANALYTICS-2517", "title": "Analytics scenario 2517", "data": {"sku": "SKU2517", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2517@example.com", "threshold": 170}},
    {"id": "ANALYTICS-2518", "title": "Analytics scenario 2518", "data": {"sku": "SKU2518", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2518@example.com", "threshold": 180}},
    {"id": "ANALYTICS-2519", "title": "Analytics scenario 2519", "data": {"sku": "SKU2519", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2519@example.com", "threshold": 190}},
    {"id": "ANALYTICS-2520", "title": "Analytics scenario 2520", "data": {"sku": "SKU2520", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2520@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
