import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-6651", "title": "Analytics scenario 6651", "data": {"sku": "SKU6651", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6651@example.com", "threshold": 510}},
    {"id": "ANALYTICS-6652", "title": "Analytics scenario 6652", "data": {"sku": "SKU6652", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6652@example.com", "threshold": 520}},
    {"id": "ANALYTICS-6653", "title": "Analytics scenario 6653", "data": {"sku": "SKU6653", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6653@example.com", "threshold": 530}},
    {"id": "ANALYTICS-6654", "title": "Analytics scenario 6654", "data": {"sku": "SKU6654", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6654@example.com", "threshold": 540}},
    {"id": "ANALYTICS-6655", "title": "Analytics scenario 6655", "data": {"sku": "SKU6655", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6655@example.com", "threshold": 550}},
    {"id": "ANALYTICS-6656", "title": "Analytics scenario 6656", "data": {"sku": "SKU6656", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6656@example.com", "threshold": 560}},
    {"id": "ANALYTICS-6657", "title": "Analytics scenario 6657", "data": {"sku": "SKU6657", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6657@example.com", "threshold": 570}},
    {"id": "ANALYTICS-6658", "title": "Analytics scenario 6658", "data": {"sku": "SKU6658", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6658@example.com", "threshold": 580}},
    {"id": "ANALYTICS-6659", "title": "Analytics scenario 6659", "data": {"sku": "SKU6659", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6659@example.com", "threshold": 590}},
    {"id": "ANALYTICS-6660", "title": "Analytics scenario 6660", "data": {"sku": "SKU6660", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6660@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
