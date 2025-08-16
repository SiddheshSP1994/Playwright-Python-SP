import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-6771", "title": "Analytics scenario 6771", "data": {"sku": "SKU6771", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6771@example.com", "threshold": 710}},
    {"id": "ANALYTICS-6772", "title": "Analytics scenario 6772", "data": {"sku": "SKU6772", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6772@example.com", "threshold": 720}},
    {"id": "ANALYTICS-6773", "title": "Analytics scenario 6773", "data": {"sku": "SKU6773", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6773@example.com", "threshold": 730}},
    {"id": "ANALYTICS-6774", "title": "Analytics scenario 6774", "data": {"sku": "SKU6774", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6774@example.com", "threshold": 740}},
    {"id": "ANALYTICS-6775", "title": "Analytics scenario 6775", "data": {"sku": "SKU6775", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6775@example.com", "threshold": 750}},
    {"id": "ANALYTICS-6776", "title": "Analytics scenario 6776", "data": {"sku": "SKU6776", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6776@example.com", "threshold": 760}},
    {"id": "ANALYTICS-6777", "title": "Analytics scenario 6777", "data": {"sku": "SKU6777", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6777@example.com", "threshold": 770}},
    {"id": "ANALYTICS-6778", "title": "Analytics scenario 6778", "data": {"sku": "SKU6778", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6778@example.com", "threshold": 780}},
    {"id": "ANALYTICS-6779", "title": "Analytics scenario 6779", "data": {"sku": "SKU6779", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6779@example.com", "threshold": 790}},
    {"id": "ANALYTICS-6780", "title": "Analytics scenario 6780", "data": {"sku": "SKU6780", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6780@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
