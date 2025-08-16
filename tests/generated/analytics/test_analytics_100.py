import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-5991", "title": "Analytics scenario 5991", "data": {"sku": "SKU5991", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5991@example.com", "threshold": 910}},
    {"id": "ANALYTICS-5992", "title": "Analytics scenario 5992", "data": {"sku": "SKU5992", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5992@example.com", "threshold": 920}},
    {"id": "ANALYTICS-5993", "title": "Analytics scenario 5993", "data": {"sku": "SKU5993", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5993@example.com", "threshold": 930}},
    {"id": "ANALYTICS-5994", "title": "Analytics scenario 5994", "data": {"sku": "SKU5994", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5994@example.com", "threshold": 940}},
    {"id": "ANALYTICS-5995", "title": "Analytics scenario 5995", "data": {"sku": "SKU5995", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5995@example.com", "threshold": 950}},
    {"id": "ANALYTICS-5996", "title": "Analytics scenario 5996", "data": {"sku": "SKU5996", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5996@example.com", "threshold": 960}},
    {"id": "ANALYTICS-5997", "title": "Analytics scenario 5997", "data": {"sku": "SKU5997", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5997@example.com", "threshold": 970}},
    {"id": "ANALYTICS-5998", "title": "Analytics scenario 5998", "data": {"sku": "SKU5998", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5998@example.com", "threshold": 980}},
    {"id": "ANALYTICS-5999", "title": "Analytics scenario 5999", "data": {"sku": "SKU5999", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5999@example.com", "threshold": 990}},
    {"id": "ANALYTICS-6000", "title": "Analytics scenario 6000", "data": {"sku": "SKU6000", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6000@example.com", "threshold": 0}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
