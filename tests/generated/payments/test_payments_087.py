import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5191", "title": "Payments scenario 5191", "data": {"sku": "SKU5191", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5191@example.com", "threshold": 910}},
    {"id": "PAYMENTS-5192", "title": "Payments scenario 5192", "data": {"sku": "SKU5192", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5192@example.com", "threshold": 920}},
    {"id": "PAYMENTS-5193", "title": "Payments scenario 5193", "data": {"sku": "SKU5193", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5193@example.com", "threshold": 930}},
    {"id": "PAYMENTS-5194", "title": "Payments scenario 5194", "data": {"sku": "SKU5194", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5194@example.com", "threshold": 940}},
    {"id": "PAYMENTS-5195", "title": "Payments scenario 5195", "data": {"sku": "SKU5195", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5195@example.com", "threshold": 950}},
    {"id": "PAYMENTS-5196", "title": "Payments scenario 5196", "data": {"sku": "SKU5196", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5196@example.com", "threshold": 960}},
    {"id": "PAYMENTS-5197", "title": "Payments scenario 5197", "data": {"sku": "SKU5197", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5197@example.com", "threshold": 970}},
    {"id": "PAYMENTS-5198", "title": "Payments scenario 5198", "data": {"sku": "SKU5198", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5198@example.com", "threshold": 980}},
    {"id": "PAYMENTS-5199", "title": "Payments scenario 5199", "data": {"sku": "SKU5199", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5199@example.com", "threshold": 990}},
    {"id": "PAYMENTS-5200", "title": "Payments scenario 5200", "data": {"sku": "SKU5200", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5200@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
