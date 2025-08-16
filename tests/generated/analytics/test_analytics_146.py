import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8751", "title": "Analytics scenario 8751", "data": {"sku": "SKU8751", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8751@example.com", "threshold": 510}},
    {"id": "ANALYTICS-8752", "title": "Analytics scenario 8752", "data": {"sku": "SKU8752", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8752@example.com", "threshold": 520}},
    {"id": "ANALYTICS-8753", "title": "Analytics scenario 8753", "data": {"sku": "SKU8753", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8753@example.com", "threshold": 530}},
    {"id": "ANALYTICS-8754", "title": "Analytics scenario 8754", "data": {"sku": "SKU8754", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8754@example.com", "threshold": 540}},
    {"id": "ANALYTICS-8755", "title": "Analytics scenario 8755", "data": {"sku": "SKU8755", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8755@example.com", "threshold": 550}},
    {"id": "ANALYTICS-8756", "title": "Analytics scenario 8756", "data": {"sku": "SKU8756", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8756@example.com", "threshold": 560}},
    {"id": "ANALYTICS-8757", "title": "Analytics scenario 8757", "data": {"sku": "SKU8757", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8757@example.com", "threshold": 570}},
    {"id": "ANALYTICS-8758", "title": "Analytics scenario 8758", "data": {"sku": "SKU8758", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8758@example.com", "threshold": 580}},
    {"id": "ANALYTICS-8759", "title": "Analytics scenario 8759", "data": {"sku": "SKU8759", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8759@example.com", "threshold": 590}},
    {"id": "ANALYTICS-8760", "title": "Analytics scenario 8760", "data": {"sku": "SKU8760", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8760@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
