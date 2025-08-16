import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-0351", "title": "Analytics scenario 351", "data": {"sku": "SKU351", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user351@example.com", "threshold": 510}},
    {"id": "ANALYTICS-0352", "title": "Analytics scenario 352", "data": {"sku": "SKU352", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user352@example.com", "threshold": 520}},
    {"id": "ANALYTICS-0353", "title": "Analytics scenario 353", "data": {"sku": "SKU353", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user353@example.com", "threshold": 530}},
    {"id": "ANALYTICS-0354", "title": "Analytics scenario 354", "data": {"sku": "SKU354", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user354@example.com", "threshold": 540}},
    {"id": "ANALYTICS-0355", "title": "Analytics scenario 355", "data": {"sku": "SKU355", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user355@example.com", "threshold": 550}},
    {"id": "ANALYTICS-0356", "title": "Analytics scenario 356", "data": {"sku": "SKU356", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user356@example.com", "threshold": 560}},
    {"id": "ANALYTICS-0357", "title": "Analytics scenario 357", "data": {"sku": "SKU357", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user357@example.com", "threshold": 570}},
    {"id": "ANALYTICS-0358", "title": "Analytics scenario 358", "data": {"sku": "SKU358", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user358@example.com", "threshold": 580}},
    {"id": "ANALYTICS-0359", "title": "Analytics scenario 359", "data": {"sku": "SKU359", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user359@example.com", "threshold": 590}},
    {"id": "ANALYTICS-0360", "title": "Analytics scenario 360", "data": {"sku": "SKU360", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user360@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
