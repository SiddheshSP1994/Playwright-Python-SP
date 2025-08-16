import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8211", "title": "Analytics scenario 8211", "data": {"sku": "SKU8211", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8211@example.com", "threshold": 110}},
    {"id": "ANALYTICS-8212", "title": "Analytics scenario 8212", "data": {"sku": "SKU8212", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8212@example.com", "threshold": 120}},
    {"id": "ANALYTICS-8213", "title": "Analytics scenario 8213", "data": {"sku": "SKU8213", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8213@example.com", "threshold": 130}},
    {"id": "ANALYTICS-8214", "title": "Analytics scenario 8214", "data": {"sku": "SKU8214", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8214@example.com", "threshold": 140}},
    {"id": "ANALYTICS-8215", "title": "Analytics scenario 8215", "data": {"sku": "SKU8215", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8215@example.com", "threshold": 150}},
    {"id": "ANALYTICS-8216", "title": "Analytics scenario 8216", "data": {"sku": "SKU8216", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8216@example.com", "threshold": 160}},
    {"id": "ANALYTICS-8217", "title": "Analytics scenario 8217", "data": {"sku": "SKU8217", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8217@example.com", "threshold": 170}},
    {"id": "ANALYTICS-8218", "title": "Analytics scenario 8218", "data": {"sku": "SKU8218", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8218@example.com", "threshold": 180}},
    {"id": "ANALYTICS-8219", "title": "Analytics scenario 8219", "data": {"sku": "SKU8219", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8219@example.com", "threshold": 190}},
    {"id": "ANALYTICS-8220", "title": "Analytics scenario 8220", "data": {"sku": "SKU8220", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8220@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
