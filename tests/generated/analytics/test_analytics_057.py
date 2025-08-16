import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-3411", "title": "Analytics scenario 3411", "data": {"sku": "SKU3411", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3411@example.com", "threshold": 110}},
    {"id": "ANALYTICS-3412", "title": "Analytics scenario 3412", "data": {"sku": "SKU3412", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3412@example.com", "threshold": 120}},
    {"id": "ANALYTICS-3413", "title": "Analytics scenario 3413", "data": {"sku": "SKU3413", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3413@example.com", "threshold": 130}},
    {"id": "ANALYTICS-3414", "title": "Analytics scenario 3414", "data": {"sku": "SKU3414", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3414@example.com", "threshold": 140}},
    {"id": "ANALYTICS-3415", "title": "Analytics scenario 3415", "data": {"sku": "SKU3415", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3415@example.com", "threshold": 150}},
    {"id": "ANALYTICS-3416", "title": "Analytics scenario 3416", "data": {"sku": "SKU3416", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3416@example.com", "threshold": 160}},
    {"id": "ANALYTICS-3417", "title": "Analytics scenario 3417", "data": {"sku": "SKU3417", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3417@example.com", "threshold": 170}},
    {"id": "ANALYTICS-3418", "title": "Analytics scenario 3418", "data": {"sku": "SKU3418", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3418@example.com", "threshold": 180}},
    {"id": "ANALYTICS-3419", "title": "Analytics scenario 3419", "data": {"sku": "SKU3419", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3419@example.com", "threshold": 190}},
    {"id": "ANALYTICS-3420", "title": "Analytics scenario 3420", "data": {"sku": "SKU3420", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3420@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
