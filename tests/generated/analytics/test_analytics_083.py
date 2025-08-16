import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-4971", "title": "Analytics scenario 4971", "data": {"sku": "SKU4971", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4971@example.com", "threshold": 710}},
    {"id": "ANALYTICS-4972", "title": "Analytics scenario 4972", "data": {"sku": "SKU4972", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4972@example.com", "threshold": 720}},
    {"id": "ANALYTICS-4973", "title": "Analytics scenario 4973", "data": {"sku": "SKU4973", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4973@example.com", "threshold": 730}},
    {"id": "ANALYTICS-4974", "title": "Analytics scenario 4974", "data": {"sku": "SKU4974", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4974@example.com", "threshold": 740}},
    {"id": "ANALYTICS-4975", "title": "Analytics scenario 4975", "data": {"sku": "SKU4975", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4975@example.com", "threshold": 750}},
    {"id": "ANALYTICS-4976", "title": "Analytics scenario 4976", "data": {"sku": "SKU4976", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4976@example.com", "threshold": 760}},
    {"id": "ANALYTICS-4977", "title": "Analytics scenario 4977", "data": {"sku": "SKU4977", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4977@example.com", "threshold": 770}},
    {"id": "ANALYTICS-4978", "title": "Analytics scenario 4978", "data": {"sku": "SKU4978", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4978@example.com", "threshold": 780}},
    {"id": "ANALYTICS-4979", "title": "Analytics scenario 4979", "data": {"sku": "SKU4979", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4979@example.com", "threshold": 790}},
    {"id": "ANALYTICS-4980", "title": "Analytics scenario 4980", "data": {"sku": "SKU4980", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4980@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
