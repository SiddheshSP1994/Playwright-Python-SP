import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8991", "title": "Analytics scenario 8991", "data": {"sku": "SKU8991", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8991@example.com", "threshold": 910}},
    {"id": "ANALYTICS-8992", "title": "Analytics scenario 8992", "data": {"sku": "SKU8992", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8992@example.com", "threshold": 920}},
    {"id": "ANALYTICS-8993", "title": "Analytics scenario 8993", "data": {"sku": "SKU8993", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8993@example.com", "threshold": 930}},
    {"id": "ANALYTICS-8994", "title": "Analytics scenario 8994", "data": {"sku": "SKU8994", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8994@example.com", "threshold": 940}},
    {"id": "ANALYTICS-8995", "title": "Analytics scenario 8995", "data": {"sku": "SKU8995", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8995@example.com", "threshold": 950}},
    {"id": "ANALYTICS-8996", "title": "Analytics scenario 8996", "data": {"sku": "SKU8996", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8996@example.com", "threshold": 960}},
    {"id": "ANALYTICS-8997", "title": "Analytics scenario 8997", "data": {"sku": "SKU8997", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8997@example.com", "threshold": 970}},
    {"id": "ANALYTICS-8998", "title": "Analytics scenario 8998", "data": {"sku": "SKU8998", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8998@example.com", "threshold": 980}},
    {"id": "ANALYTICS-8999", "title": "Analytics scenario 8999", "data": {"sku": "SKU8999", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8999@example.com", "threshold": 990}},
    {"id": "ANALYTICS-9000", "title": "Analytics scenario 9000", "data": {"sku": "SKU9000", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9000@example.com", "threshold": 0}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
