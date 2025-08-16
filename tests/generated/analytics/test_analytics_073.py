import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-4371", "title": "Analytics scenario 4371", "data": {"sku": "SKU4371", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4371@example.com", "threshold": 710}},
    {"id": "ANALYTICS-4372", "title": "Analytics scenario 4372", "data": {"sku": "SKU4372", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4372@example.com", "threshold": 720}},
    {"id": "ANALYTICS-4373", "title": "Analytics scenario 4373", "data": {"sku": "SKU4373", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4373@example.com", "threshold": 730}},
    {"id": "ANALYTICS-4374", "title": "Analytics scenario 4374", "data": {"sku": "SKU4374", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4374@example.com", "threshold": 740}},
    {"id": "ANALYTICS-4375", "title": "Analytics scenario 4375", "data": {"sku": "SKU4375", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4375@example.com", "threshold": 750}},
    {"id": "ANALYTICS-4376", "title": "Analytics scenario 4376", "data": {"sku": "SKU4376", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4376@example.com", "threshold": 760}},
    {"id": "ANALYTICS-4377", "title": "Analytics scenario 4377", "data": {"sku": "SKU4377", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4377@example.com", "threshold": 770}},
    {"id": "ANALYTICS-4378", "title": "Analytics scenario 4378", "data": {"sku": "SKU4378", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4378@example.com", "threshold": 780}},
    {"id": "ANALYTICS-4379", "title": "Analytics scenario 4379", "data": {"sku": "SKU4379", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4379@example.com", "threshold": 790}},
    {"id": "ANALYTICS-4380", "title": "Analytics scenario 4380", "data": {"sku": "SKU4380", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4380@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
