import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-3711", "title": "Analytics scenario 3711", "data": {"sku": "SKU3711", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3711@example.com", "threshold": 110}},
    {"id": "ANALYTICS-3712", "title": "Analytics scenario 3712", "data": {"sku": "SKU3712", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3712@example.com", "threshold": 120}},
    {"id": "ANALYTICS-3713", "title": "Analytics scenario 3713", "data": {"sku": "SKU3713", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3713@example.com", "threshold": 130}},
    {"id": "ANALYTICS-3714", "title": "Analytics scenario 3714", "data": {"sku": "SKU3714", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3714@example.com", "threshold": 140}},
    {"id": "ANALYTICS-3715", "title": "Analytics scenario 3715", "data": {"sku": "SKU3715", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3715@example.com", "threshold": 150}},
    {"id": "ANALYTICS-3716", "title": "Analytics scenario 3716", "data": {"sku": "SKU3716", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3716@example.com", "threshold": 160}},
    {"id": "ANALYTICS-3717", "title": "Analytics scenario 3717", "data": {"sku": "SKU3717", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3717@example.com", "threshold": 170}},
    {"id": "ANALYTICS-3718", "title": "Analytics scenario 3718", "data": {"sku": "SKU3718", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3718@example.com", "threshold": 180}},
    {"id": "ANALYTICS-3719", "title": "Analytics scenario 3719", "data": {"sku": "SKU3719", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3719@example.com", "threshold": 190}},
    {"id": "ANALYTICS-3720", "title": "Analytics scenario 3720", "data": {"sku": "SKU3720", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3720@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
