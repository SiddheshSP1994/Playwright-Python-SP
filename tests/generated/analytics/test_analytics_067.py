import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-4011", "title": "Analytics scenario 4011", "data": {"sku": "SKU4011", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4011@example.com", "threshold": 110}},
    {"id": "ANALYTICS-4012", "title": "Analytics scenario 4012", "data": {"sku": "SKU4012", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4012@example.com", "threshold": 120}},
    {"id": "ANALYTICS-4013", "title": "Analytics scenario 4013", "data": {"sku": "SKU4013", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4013@example.com", "threshold": 130}},
    {"id": "ANALYTICS-4014", "title": "Analytics scenario 4014", "data": {"sku": "SKU4014", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4014@example.com", "threshold": 140}},
    {"id": "ANALYTICS-4015", "title": "Analytics scenario 4015", "data": {"sku": "SKU4015", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4015@example.com", "threshold": 150}},
    {"id": "ANALYTICS-4016", "title": "Analytics scenario 4016", "data": {"sku": "SKU4016", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4016@example.com", "threshold": 160}},
    {"id": "ANALYTICS-4017", "title": "Analytics scenario 4017", "data": {"sku": "SKU4017", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4017@example.com", "threshold": 170}},
    {"id": "ANALYTICS-4018", "title": "Analytics scenario 4018", "data": {"sku": "SKU4018", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4018@example.com", "threshold": 180}},
    {"id": "ANALYTICS-4019", "title": "Analytics scenario 4019", "data": {"sku": "SKU4019", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4019@example.com", "threshold": 190}},
    {"id": "ANALYTICS-4020", "title": "Analytics scenario 4020", "data": {"sku": "SKU4020", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4020@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
