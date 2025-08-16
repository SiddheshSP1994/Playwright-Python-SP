import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8571", "title": "Analytics scenario 8571", "data": {"sku": "SKU8571", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8571@example.com", "threshold": 710}},
    {"id": "ANALYTICS-8572", "title": "Analytics scenario 8572", "data": {"sku": "SKU8572", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8572@example.com", "threshold": 720}},
    {"id": "ANALYTICS-8573", "title": "Analytics scenario 8573", "data": {"sku": "SKU8573", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8573@example.com", "threshold": 730}},
    {"id": "ANALYTICS-8574", "title": "Analytics scenario 8574", "data": {"sku": "SKU8574", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8574@example.com", "threshold": 740}},
    {"id": "ANALYTICS-8575", "title": "Analytics scenario 8575", "data": {"sku": "SKU8575", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8575@example.com", "threshold": 750}},
    {"id": "ANALYTICS-8576", "title": "Analytics scenario 8576", "data": {"sku": "SKU8576", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8576@example.com", "threshold": 760}},
    {"id": "ANALYTICS-8577", "title": "Analytics scenario 8577", "data": {"sku": "SKU8577", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8577@example.com", "threshold": 770}},
    {"id": "ANALYTICS-8578", "title": "Analytics scenario 8578", "data": {"sku": "SKU8578", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8578@example.com", "threshold": 780}},
    {"id": "ANALYTICS-8579", "title": "Analytics scenario 8579", "data": {"sku": "SKU8579", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8579@example.com", "threshold": 790}},
    {"id": "ANALYTICS-8580", "title": "Analytics scenario 8580", "data": {"sku": "SKU8580", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8580@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
