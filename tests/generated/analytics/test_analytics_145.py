import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8691", "title": "Analytics scenario 8691", "data": {"sku": "SKU8691", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8691@example.com", "threshold": 910}},
    {"id": "ANALYTICS-8692", "title": "Analytics scenario 8692", "data": {"sku": "SKU8692", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8692@example.com", "threshold": 920}},
    {"id": "ANALYTICS-8693", "title": "Analytics scenario 8693", "data": {"sku": "SKU8693", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8693@example.com", "threshold": 930}},
    {"id": "ANALYTICS-8694", "title": "Analytics scenario 8694", "data": {"sku": "SKU8694", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8694@example.com", "threshold": 940}},
    {"id": "ANALYTICS-8695", "title": "Analytics scenario 8695", "data": {"sku": "SKU8695", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8695@example.com", "threshold": 950}},
    {"id": "ANALYTICS-8696", "title": "Analytics scenario 8696", "data": {"sku": "SKU8696", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8696@example.com", "threshold": 960}},
    {"id": "ANALYTICS-8697", "title": "Analytics scenario 8697", "data": {"sku": "SKU8697", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8697@example.com", "threshold": 970}},
    {"id": "ANALYTICS-8698", "title": "Analytics scenario 8698", "data": {"sku": "SKU8698", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8698@example.com", "threshold": 980}},
    {"id": "ANALYTICS-8699", "title": "Analytics scenario 8699", "data": {"sku": "SKU8699", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8699@example.com", "threshold": 990}},
    {"id": "ANALYTICS-8700", "title": "Analytics scenario 8700", "data": {"sku": "SKU8700", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8700@example.com", "threshold": 0}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
