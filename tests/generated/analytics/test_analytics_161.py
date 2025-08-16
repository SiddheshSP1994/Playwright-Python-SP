import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-9651", "title": "Analytics scenario 9651", "data": {"sku": "SKU9651", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9651@example.com", "threshold": 510}},
    {"id": "ANALYTICS-9652", "title": "Analytics scenario 9652", "data": {"sku": "SKU9652", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9652@example.com", "threshold": 520}},
    {"id": "ANALYTICS-9653", "title": "Analytics scenario 9653", "data": {"sku": "SKU9653", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9653@example.com", "threshold": 530}},
    {"id": "ANALYTICS-9654", "title": "Analytics scenario 9654", "data": {"sku": "SKU9654", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9654@example.com", "threshold": 540}},
    {"id": "ANALYTICS-9655", "title": "Analytics scenario 9655", "data": {"sku": "SKU9655", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9655@example.com", "threshold": 550}},
    {"id": "ANALYTICS-9656", "title": "Analytics scenario 9656", "data": {"sku": "SKU9656", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9656@example.com", "threshold": 560}},
    {"id": "ANALYTICS-9657", "title": "Analytics scenario 9657", "data": {"sku": "SKU9657", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9657@example.com", "threshold": 570}},
    {"id": "ANALYTICS-9658", "title": "Analytics scenario 9658", "data": {"sku": "SKU9658", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9658@example.com", "threshold": 580}},
    {"id": "ANALYTICS-9659", "title": "Analytics scenario 9659", "data": {"sku": "SKU9659", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9659@example.com", "threshold": 590}},
    {"id": "ANALYTICS-9660", "title": "Analytics scenario 9660", "data": {"sku": "SKU9660", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9660@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
