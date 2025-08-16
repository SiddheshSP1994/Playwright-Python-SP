import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-5271", "title": "Analytics scenario 5271", "data": {"sku": "SKU5271", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5271@example.com", "threshold": 710}},
    {"id": "ANALYTICS-5272", "title": "Analytics scenario 5272", "data": {"sku": "SKU5272", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5272@example.com", "threshold": 720}},
    {"id": "ANALYTICS-5273", "title": "Analytics scenario 5273", "data": {"sku": "SKU5273", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5273@example.com", "threshold": 730}},
    {"id": "ANALYTICS-5274", "title": "Analytics scenario 5274", "data": {"sku": "SKU5274", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5274@example.com", "threshold": 740}},
    {"id": "ANALYTICS-5275", "title": "Analytics scenario 5275", "data": {"sku": "SKU5275", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5275@example.com", "threshold": 750}},
    {"id": "ANALYTICS-5276", "title": "Analytics scenario 5276", "data": {"sku": "SKU5276", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5276@example.com", "threshold": 760}},
    {"id": "ANALYTICS-5277", "title": "Analytics scenario 5277", "data": {"sku": "SKU5277", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5277@example.com", "threshold": 770}},
    {"id": "ANALYTICS-5278", "title": "Analytics scenario 5278", "data": {"sku": "SKU5278", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5278@example.com", "threshold": 780}},
    {"id": "ANALYTICS-5279", "title": "Analytics scenario 5279", "data": {"sku": "SKU5279", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5279@example.com", "threshold": 790}},
    {"id": "ANALYTICS-5280", "title": "Analytics scenario 5280", "data": {"sku": "SKU5280", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5280@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
