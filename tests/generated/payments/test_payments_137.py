import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8191", "title": "Payments scenario 8191", "data": {"sku": "SKU8191", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8191@example.com", "threshold": 910}},
    {"id": "PAYMENTS-8192", "title": "Payments scenario 8192", "data": {"sku": "SKU8192", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8192@example.com", "threshold": 920}},
    {"id": "PAYMENTS-8193", "title": "Payments scenario 8193", "data": {"sku": "SKU8193", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8193@example.com", "threshold": 930}},
    {"id": "PAYMENTS-8194", "title": "Payments scenario 8194", "data": {"sku": "SKU8194", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8194@example.com", "threshold": 940}},
    {"id": "PAYMENTS-8195", "title": "Payments scenario 8195", "data": {"sku": "SKU8195", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8195@example.com", "threshold": 950}},
    {"id": "PAYMENTS-8196", "title": "Payments scenario 8196", "data": {"sku": "SKU8196", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8196@example.com", "threshold": 960}},
    {"id": "PAYMENTS-8197", "title": "Payments scenario 8197", "data": {"sku": "SKU8197", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8197@example.com", "threshold": 970}},
    {"id": "PAYMENTS-8198", "title": "Payments scenario 8198", "data": {"sku": "SKU8198", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8198@example.com", "threshold": 980}},
    {"id": "PAYMENTS-8199", "title": "Payments scenario 8199", "data": {"sku": "SKU8199", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8199@example.com", "threshold": 990}},
    {"id": "PAYMENTS-8200", "title": "Payments scenario 8200", "data": {"sku": "SKU8200", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8200@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
