import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3691", "title": "Payments scenario 3691", "data": {"sku": "SKU3691", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3691@example.com", "threshold": 910}},
    {"id": "PAYMENTS-3692", "title": "Payments scenario 3692", "data": {"sku": "SKU3692", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3692@example.com", "threshold": 920}},
    {"id": "PAYMENTS-3693", "title": "Payments scenario 3693", "data": {"sku": "SKU3693", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3693@example.com", "threshold": 930}},
    {"id": "PAYMENTS-3694", "title": "Payments scenario 3694", "data": {"sku": "SKU3694", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3694@example.com", "threshold": 940}},
    {"id": "PAYMENTS-3695", "title": "Payments scenario 3695", "data": {"sku": "SKU3695", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3695@example.com", "threshold": 950}},
    {"id": "PAYMENTS-3696", "title": "Payments scenario 3696", "data": {"sku": "SKU3696", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3696@example.com", "threshold": 960}},
    {"id": "PAYMENTS-3697", "title": "Payments scenario 3697", "data": {"sku": "SKU3697", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3697@example.com", "threshold": 970}},
    {"id": "PAYMENTS-3698", "title": "Payments scenario 3698", "data": {"sku": "SKU3698", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3698@example.com", "threshold": 980}},
    {"id": "PAYMENTS-3699", "title": "Payments scenario 3699", "data": {"sku": "SKU3699", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3699@example.com", "threshold": 990}},
    {"id": "PAYMENTS-3700", "title": "Payments scenario 3700", "data": {"sku": "SKU3700", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3700@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
