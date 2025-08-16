import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-6351", "title": "Analytics scenario 6351", "data": {"sku": "SKU6351", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6351@example.com", "threshold": 510}},
    {"id": "ANALYTICS-6352", "title": "Analytics scenario 6352", "data": {"sku": "SKU6352", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6352@example.com", "threshold": 520}},
    {"id": "ANALYTICS-6353", "title": "Analytics scenario 6353", "data": {"sku": "SKU6353", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6353@example.com", "threshold": 530}},
    {"id": "ANALYTICS-6354", "title": "Analytics scenario 6354", "data": {"sku": "SKU6354", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6354@example.com", "threshold": 540}},
    {"id": "ANALYTICS-6355", "title": "Analytics scenario 6355", "data": {"sku": "SKU6355", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6355@example.com", "threshold": 550}},
    {"id": "ANALYTICS-6356", "title": "Analytics scenario 6356", "data": {"sku": "SKU6356", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6356@example.com", "threshold": 560}},
    {"id": "ANALYTICS-6357", "title": "Analytics scenario 6357", "data": {"sku": "SKU6357", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6357@example.com", "threshold": 570}},
    {"id": "ANALYTICS-6358", "title": "Analytics scenario 6358", "data": {"sku": "SKU6358", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6358@example.com", "threshold": 580}},
    {"id": "ANALYTICS-6359", "title": "Analytics scenario 6359", "data": {"sku": "SKU6359", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6359@example.com", "threshold": 590}},
    {"id": "ANALYTICS-6360", "title": "Analytics scenario 6360", "data": {"sku": "SKU6360", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6360@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
