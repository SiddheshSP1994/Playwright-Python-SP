import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1591", "title": "Payments scenario 1591", "data": {"sku": "SKU1591", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1591@example.com", "threshold": 910}},
    {"id": "PAYMENTS-1592", "title": "Payments scenario 1592", "data": {"sku": "SKU1592", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1592@example.com", "threshold": 920}},
    {"id": "PAYMENTS-1593", "title": "Payments scenario 1593", "data": {"sku": "SKU1593", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1593@example.com", "threshold": 930}},
    {"id": "PAYMENTS-1594", "title": "Payments scenario 1594", "data": {"sku": "SKU1594", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1594@example.com", "threshold": 940}},
    {"id": "PAYMENTS-1595", "title": "Payments scenario 1595", "data": {"sku": "SKU1595", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1595@example.com", "threshold": 950}},
    {"id": "PAYMENTS-1596", "title": "Payments scenario 1596", "data": {"sku": "SKU1596", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1596@example.com", "threshold": 960}},
    {"id": "PAYMENTS-1597", "title": "Payments scenario 1597", "data": {"sku": "SKU1597", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1597@example.com", "threshold": 970}},
    {"id": "PAYMENTS-1598", "title": "Payments scenario 1598", "data": {"sku": "SKU1598", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1598@example.com", "threshold": 980}},
    {"id": "PAYMENTS-1599", "title": "Payments scenario 1599", "data": {"sku": "SKU1599", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1599@example.com", "threshold": 990}},
    {"id": "PAYMENTS-1600", "title": "Payments scenario 1600", "data": {"sku": "SKU1600", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1600@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
