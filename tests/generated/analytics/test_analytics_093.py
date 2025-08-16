import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-5571", "title": "Analytics scenario 5571", "data": {"sku": "SKU5571", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5571@example.com", "threshold": 710}},
    {"id": "ANALYTICS-5572", "title": "Analytics scenario 5572", "data": {"sku": "SKU5572", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5572@example.com", "threshold": 720}},
    {"id": "ANALYTICS-5573", "title": "Analytics scenario 5573", "data": {"sku": "SKU5573", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5573@example.com", "threshold": 730}},
    {"id": "ANALYTICS-5574", "title": "Analytics scenario 5574", "data": {"sku": "SKU5574", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5574@example.com", "threshold": 740}},
    {"id": "ANALYTICS-5575", "title": "Analytics scenario 5575", "data": {"sku": "SKU5575", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5575@example.com", "threshold": 750}},
    {"id": "ANALYTICS-5576", "title": "Analytics scenario 5576", "data": {"sku": "SKU5576", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5576@example.com", "threshold": 760}},
    {"id": "ANALYTICS-5577", "title": "Analytics scenario 5577", "data": {"sku": "SKU5577", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5577@example.com", "threshold": 770}},
    {"id": "ANALYTICS-5578", "title": "Analytics scenario 5578", "data": {"sku": "SKU5578", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5578@example.com", "threshold": 780}},
    {"id": "ANALYTICS-5579", "title": "Analytics scenario 5579", "data": {"sku": "SKU5579", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5579@example.com", "threshold": 790}},
    {"id": "ANALYTICS-5580", "title": "Analytics scenario 5580", "data": {"sku": "SKU5580", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5580@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
