import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-0771", "title": "Analytics scenario 771", "data": {"sku": "SKU771", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user771@example.com", "threshold": 710}},
    {"id": "ANALYTICS-0772", "title": "Analytics scenario 772", "data": {"sku": "SKU772", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user772@example.com", "threshold": 720}},
    {"id": "ANALYTICS-0773", "title": "Analytics scenario 773", "data": {"sku": "SKU773", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user773@example.com", "threshold": 730}},
    {"id": "ANALYTICS-0774", "title": "Analytics scenario 774", "data": {"sku": "SKU774", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user774@example.com", "threshold": 740}},
    {"id": "ANALYTICS-0775", "title": "Analytics scenario 775", "data": {"sku": "SKU775", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user775@example.com", "threshold": 750}},
    {"id": "ANALYTICS-0776", "title": "Analytics scenario 776", "data": {"sku": "SKU776", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user776@example.com", "threshold": 760}},
    {"id": "ANALYTICS-0777", "title": "Analytics scenario 777", "data": {"sku": "SKU777", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user777@example.com", "threshold": 770}},
    {"id": "ANALYTICS-0778", "title": "Analytics scenario 778", "data": {"sku": "SKU778", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user778@example.com", "threshold": 780}},
    {"id": "ANALYTICS-0779", "title": "Analytics scenario 779", "data": {"sku": "SKU779", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user779@example.com", "threshold": 790}},
    {"id": "ANALYTICS-0780", "title": "Analytics scenario 780", "data": {"sku": "SKU780", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user780@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
