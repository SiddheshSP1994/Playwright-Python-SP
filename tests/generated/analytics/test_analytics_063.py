import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-3771", "title": "Analytics scenario 3771", "data": {"sku": "SKU3771", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3771@example.com", "threshold": 710}},
    {"id": "ANALYTICS-3772", "title": "Analytics scenario 3772", "data": {"sku": "SKU3772", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3772@example.com", "threshold": 720}},
    {"id": "ANALYTICS-3773", "title": "Analytics scenario 3773", "data": {"sku": "SKU3773", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3773@example.com", "threshold": 730}},
    {"id": "ANALYTICS-3774", "title": "Analytics scenario 3774", "data": {"sku": "SKU3774", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3774@example.com", "threshold": 740}},
    {"id": "ANALYTICS-3775", "title": "Analytics scenario 3775", "data": {"sku": "SKU3775", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3775@example.com", "threshold": 750}},
    {"id": "ANALYTICS-3776", "title": "Analytics scenario 3776", "data": {"sku": "SKU3776", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3776@example.com", "threshold": 760}},
    {"id": "ANALYTICS-3777", "title": "Analytics scenario 3777", "data": {"sku": "SKU3777", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3777@example.com", "threshold": 770}},
    {"id": "ANALYTICS-3778", "title": "Analytics scenario 3778", "data": {"sku": "SKU3778", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3778@example.com", "threshold": 780}},
    {"id": "ANALYTICS-3779", "title": "Analytics scenario 3779", "data": {"sku": "SKU3779", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3779@example.com", "threshold": 790}},
    {"id": "ANALYTICS-3780", "title": "Analytics scenario 3780", "data": {"sku": "SKU3780", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3780@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
