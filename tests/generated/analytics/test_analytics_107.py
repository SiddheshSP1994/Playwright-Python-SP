import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-6411", "title": "Analytics scenario 6411", "data": {"sku": "SKU6411", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6411@example.com", "threshold": 110}},
    {"id": "ANALYTICS-6412", "title": "Analytics scenario 6412", "data": {"sku": "SKU6412", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6412@example.com", "threshold": 120}},
    {"id": "ANALYTICS-6413", "title": "Analytics scenario 6413", "data": {"sku": "SKU6413", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6413@example.com", "threshold": 130}},
    {"id": "ANALYTICS-6414", "title": "Analytics scenario 6414", "data": {"sku": "SKU6414", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6414@example.com", "threshold": 140}},
    {"id": "ANALYTICS-6415", "title": "Analytics scenario 6415", "data": {"sku": "SKU6415", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6415@example.com", "threshold": 150}},
    {"id": "ANALYTICS-6416", "title": "Analytics scenario 6416", "data": {"sku": "SKU6416", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6416@example.com", "threshold": 160}},
    {"id": "ANALYTICS-6417", "title": "Analytics scenario 6417", "data": {"sku": "SKU6417", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6417@example.com", "threshold": 170}},
    {"id": "ANALYTICS-6418", "title": "Analytics scenario 6418", "data": {"sku": "SKU6418", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6418@example.com", "threshold": 180}},
    {"id": "ANALYTICS-6419", "title": "Analytics scenario 6419", "data": {"sku": "SKU6419", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6419@example.com", "threshold": 190}},
    {"id": "ANALYTICS-6420", "title": "Analytics scenario 6420", "data": {"sku": "SKU6420", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6420@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
