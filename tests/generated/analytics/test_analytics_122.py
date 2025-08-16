import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-7311", "title": "Analytics scenario 7311", "data": {"sku": "SKU7311", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7311@example.com", "threshold": 110}},
    {"id": "ANALYTICS-7312", "title": "Analytics scenario 7312", "data": {"sku": "SKU7312", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7312@example.com", "threshold": 120}},
    {"id": "ANALYTICS-7313", "title": "Analytics scenario 7313", "data": {"sku": "SKU7313", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7313@example.com", "threshold": 130}},
    {"id": "ANALYTICS-7314", "title": "Analytics scenario 7314", "data": {"sku": "SKU7314", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7314@example.com", "threshold": 140}},
    {"id": "ANALYTICS-7315", "title": "Analytics scenario 7315", "data": {"sku": "SKU7315", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7315@example.com", "threshold": 150}},
    {"id": "ANALYTICS-7316", "title": "Analytics scenario 7316", "data": {"sku": "SKU7316", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7316@example.com", "threshold": 160}},
    {"id": "ANALYTICS-7317", "title": "Analytics scenario 7317", "data": {"sku": "SKU7317", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7317@example.com", "threshold": 170}},
    {"id": "ANALYTICS-7318", "title": "Analytics scenario 7318", "data": {"sku": "SKU7318", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7318@example.com", "threshold": 180}},
    {"id": "ANALYTICS-7319", "title": "Analytics scenario 7319", "data": {"sku": "SKU7319", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7319@example.com", "threshold": 190}},
    {"id": "ANALYTICS-7320", "title": "Analytics scenario 7320", "data": {"sku": "SKU7320", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7320@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
