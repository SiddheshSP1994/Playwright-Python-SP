import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-2451", "title": "Analytics scenario 2451", "data": {"sku": "SKU2451", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2451@example.com", "threshold": 510}},
    {"id": "ANALYTICS-2452", "title": "Analytics scenario 2452", "data": {"sku": "SKU2452", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2452@example.com", "threshold": 520}},
    {"id": "ANALYTICS-2453", "title": "Analytics scenario 2453", "data": {"sku": "SKU2453", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2453@example.com", "threshold": 530}},
    {"id": "ANALYTICS-2454", "title": "Analytics scenario 2454", "data": {"sku": "SKU2454", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2454@example.com", "threshold": 540}},
    {"id": "ANALYTICS-2455", "title": "Analytics scenario 2455", "data": {"sku": "SKU2455", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2455@example.com", "threshold": 550}},
    {"id": "ANALYTICS-2456", "title": "Analytics scenario 2456", "data": {"sku": "SKU2456", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2456@example.com", "threshold": 560}},
    {"id": "ANALYTICS-2457", "title": "Analytics scenario 2457", "data": {"sku": "SKU2457", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2457@example.com", "threshold": 570}},
    {"id": "ANALYTICS-2458", "title": "Analytics scenario 2458", "data": {"sku": "SKU2458", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2458@example.com", "threshold": 580}},
    {"id": "ANALYTICS-2459", "title": "Analytics scenario 2459", "data": {"sku": "SKU2459", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2459@example.com", "threshold": 590}},
    {"id": "ANALYTICS-2460", "title": "Analytics scenario 2460", "data": {"sku": "SKU2460", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2460@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
