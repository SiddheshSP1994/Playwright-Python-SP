import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-5211", "title": "Analytics scenario 5211", "data": {"sku": "SKU5211", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5211@example.com", "threshold": 110}},
    {"id": "ANALYTICS-5212", "title": "Analytics scenario 5212", "data": {"sku": "SKU5212", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5212@example.com", "threshold": 120}},
    {"id": "ANALYTICS-5213", "title": "Analytics scenario 5213", "data": {"sku": "SKU5213", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5213@example.com", "threshold": 130}},
    {"id": "ANALYTICS-5214", "title": "Analytics scenario 5214", "data": {"sku": "SKU5214", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5214@example.com", "threshold": 140}},
    {"id": "ANALYTICS-5215", "title": "Analytics scenario 5215", "data": {"sku": "SKU5215", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5215@example.com", "threshold": 150}},
    {"id": "ANALYTICS-5216", "title": "Analytics scenario 5216", "data": {"sku": "SKU5216", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5216@example.com", "threshold": 160}},
    {"id": "ANALYTICS-5217", "title": "Analytics scenario 5217", "data": {"sku": "SKU5217", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5217@example.com", "threshold": 170}},
    {"id": "ANALYTICS-5218", "title": "Analytics scenario 5218", "data": {"sku": "SKU5218", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5218@example.com", "threshold": 180}},
    {"id": "ANALYTICS-5219", "title": "Analytics scenario 5219", "data": {"sku": "SKU5219", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5219@example.com", "threshold": 190}},
    {"id": "ANALYTICS-5220", "title": "Analytics scenario 5220", "data": {"sku": "SKU5220", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5220@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
