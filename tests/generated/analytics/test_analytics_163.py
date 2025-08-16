import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-9771", "title": "Analytics scenario 9771", "data": {"sku": "SKU9771", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9771@example.com", "threshold": 710}},
    {"id": "ANALYTICS-9772", "title": "Analytics scenario 9772", "data": {"sku": "SKU9772", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9772@example.com", "threshold": 720}},
    {"id": "ANALYTICS-9773", "title": "Analytics scenario 9773", "data": {"sku": "SKU9773", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9773@example.com", "threshold": 730}},
    {"id": "ANALYTICS-9774", "title": "Analytics scenario 9774", "data": {"sku": "SKU9774", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9774@example.com", "threshold": 740}},
    {"id": "ANALYTICS-9775", "title": "Analytics scenario 9775", "data": {"sku": "SKU9775", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9775@example.com", "threshold": 750}},
    {"id": "ANALYTICS-9776", "title": "Analytics scenario 9776", "data": {"sku": "SKU9776", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9776@example.com", "threshold": 760}},
    {"id": "ANALYTICS-9777", "title": "Analytics scenario 9777", "data": {"sku": "SKU9777", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9777@example.com", "threshold": 770}},
    {"id": "ANALYTICS-9778", "title": "Analytics scenario 9778", "data": {"sku": "SKU9778", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9778@example.com", "threshold": 780}},
    {"id": "ANALYTICS-9779", "title": "Analytics scenario 9779", "data": {"sku": "SKU9779", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9779@example.com", "threshold": 790}},
    {"id": "ANALYTICS-9780", "title": "Analytics scenario 9780", "data": {"sku": "SKU9780", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9780@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
