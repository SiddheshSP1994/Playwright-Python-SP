import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-0951", "title": "Analytics scenario 951", "data": {"sku": "SKU951", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user951@example.com", "threshold": 510}},
    {"id": "ANALYTICS-0952", "title": "Analytics scenario 952", "data": {"sku": "SKU952", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user952@example.com", "threshold": 520}},
    {"id": "ANALYTICS-0953", "title": "Analytics scenario 953", "data": {"sku": "SKU953", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user953@example.com", "threshold": 530}},
    {"id": "ANALYTICS-0954", "title": "Analytics scenario 954", "data": {"sku": "SKU954", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user954@example.com", "threshold": 540}},
    {"id": "ANALYTICS-0955", "title": "Analytics scenario 955", "data": {"sku": "SKU955", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user955@example.com", "threshold": 550}},
    {"id": "ANALYTICS-0956", "title": "Analytics scenario 956", "data": {"sku": "SKU956", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user956@example.com", "threshold": 560}},
    {"id": "ANALYTICS-0957", "title": "Analytics scenario 957", "data": {"sku": "SKU957", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user957@example.com", "threshold": 570}},
    {"id": "ANALYTICS-0958", "title": "Analytics scenario 958", "data": {"sku": "SKU958", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user958@example.com", "threshold": 580}},
    {"id": "ANALYTICS-0959", "title": "Analytics scenario 959", "data": {"sku": "SKU959", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user959@example.com", "threshold": 590}},
    {"id": "ANALYTICS-0960", "title": "Analytics scenario 960", "data": {"sku": "SKU960", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user960@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
