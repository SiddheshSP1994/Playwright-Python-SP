import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1071", "title": "Analytics scenario 1071", "data": {"sku": "SKU1071", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1071@example.com", "threshold": 710}},
    {"id": "ANALYTICS-1072", "title": "Analytics scenario 1072", "data": {"sku": "SKU1072", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1072@example.com", "threshold": 720}},
    {"id": "ANALYTICS-1073", "title": "Analytics scenario 1073", "data": {"sku": "SKU1073", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1073@example.com", "threshold": 730}},
    {"id": "ANALYTICS-1074", "title": "Analytics scenario 1074", "data": {"sku": "SKU1074", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1074@example.com", "threshold": 740}},
    {"id": "ANALYTICS-1075", "title": "Analytics scenario 1075", "data": {"sku": "SKU1075", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1075@example.com", "threshold": 750}},
    {"id": "ANALYTICS-1076", "title": "Analytics scenario 1076", "data": {"sku": "SKU1076", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1076@example.com", "threshold": 760}},
    {"id": "ANALYTICS-1077", "title": "Analytics scenario 1077", "data": {"sku": "SKU1077", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1077@example.com", "threshold": 770}},
    {"id": "ANALYTICS-1078", "title": "Analytics scenario 1078", "data": {"sku": "SKU1078", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1078@example.com", "threshold": 780}},
    {"id": "ANALYTICS-1079", "title": "Analytics scenario 1079", "data": {"sku": "SKU1079", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1079@example.com", "threshold": 790}},
    {"id": "ANALYTICS-1080", "title": "Analytics scenario 1080", "data": {"sku": "SKU1080", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1080@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
