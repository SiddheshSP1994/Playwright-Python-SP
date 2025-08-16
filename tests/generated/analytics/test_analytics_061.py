import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-3651", "title": "Analytics scenario 3651", "data": {"sku": "SKU3651", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3651@example.com", "threshold": 510}},
    {"id": "ANALYTICS-3652", "title": "Analytics scenario 3652", "data": {"sku": "SKU3652", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3652@example.com", "threshold": 520}},
    {"id": "ANALYTICS-3653", "title": "Analytics scenario 3653", "data": {"sku": "SKU3653", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3653@example.com", "threshold": 530}},
    {"id": "ANALYTICS-3654", "title": "Analytics scenario 3654", "data": {"sku": "SKU3654", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3654@example.com", "threshold": 540}},
    {"id": "ANALYTICS-3655", "title": "Analytics scenario 3655", "data": {"sku": "SKU3655", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3655@example.com", "threshold": 550}},
    {"id": "ANALYTICS-3656", "title": "Analytics scenario 3656", "data": {"sku": "SKU3656", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3656@example.com", "threshold": 560}},
    {"id": "ANALYTICS-3657", "title": "Analytics scenario 3657", "data": {"sku": "SKU3657", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3657@example.com", "threshold": 570}},
    {"id": "ANALYTICS-3658", "title": "Analytics scenario 3658", "data": {"sku": "SKU3658", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3658@example.com", "threshold": 580}},
    {"id": "ANALYTICS-3659", "title": "Analytics scenario 3659", "data": {"sku": "SKU3659", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3659@example.com", "threshold": 590}},
    {"id": "ANALYTICS-3660", "title": "Analytics scenario 3660", "data": {"sku": "SKU3660", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3660@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
