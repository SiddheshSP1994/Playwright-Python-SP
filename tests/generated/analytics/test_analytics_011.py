import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-0651", "title": "Analytics scenario 651", "data": {"sku": "SKU651", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user651@example.com", "threshold": 510}},
    {"id": "ANALYTICS-0652", "title": "Analytics scenario 652", "data": {"sku": "SKU652", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user652@example.com", "threshold": 520}},
    {"id": "ANALYTICS-0653", "title": "Analytics scenario 653", "data": {"sku": "SKU653", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user653@example.com", "threshold": 530}},
    {"id": "ANALYTICS-0654", "title": "Analytics scenario 654", "data": {"sku": "SKU654", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user654@example.com", "threshold": 540}},
    {"id": "ANALYTICS-0655", "title": "Analytics scenario 655", "data": {"sku": "SKU655", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user655@example.com", "threshold": 550}},
    {"id": "ANALYTICS-0656", "title": "Analytics scenario 656", "data": {"sku": "SKU656", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user656@example.com", "threshold": 560}},
    {"id": "ANALYTICS-0657", "title": "Analytics scenario 657", "data": {"sku": "SKU657", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user657@example.com", "threshold": 570}},
    {"id": "ANALYTICS-0658", "title": "Analytics scenario 658", "data": {"sku": "SKU658", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user658@example.com", "threshold": 580}},
    {"id": "ANALYTICS-0659", "title": "Analytics scenario 659", "data": {"sku": "SKU659", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user659@example.com", "threshold": 590}},
    {"id": "ANALYTICS-0660", "title": "Analytics scenario 660", "data": {"sku": "SKU660", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user660@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
