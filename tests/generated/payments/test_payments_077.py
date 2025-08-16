import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4591", "title": "Payments scenario 4591", "data": {"sku": "SKU4591", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4591@example.com", "threshold": 910}},
    {"id": "PAYMENTS-4592", "title": "Payments scenario 4592", "data": {"sku": "SKU4592", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4592@example.com", "threshold": 920}},
    {"id": "PAYMENTS-4593", "title": "Payments scenario 4593", "data": {"sku": "SKU4593", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4593@example.com", "threshold": 930}},
    {"id": "PAYMENTS-4594", "title": "Payments scenario 4594", "data": {"sku": "SKU4594", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4594@example.com", "threshold": 940}},
    {"id": "PAYMENTS-4595", "title": "Payments scenario 4595", "data": {"sku": "SKU4595", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4595@example.com", "threshold": 950}},
    {"id": "PAYMENTS-4596", "title": "Payments scenario 4596", "data": {"sku": "SKU4596", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4596@example.com", "threshold": 960}},
    {"id": "PAYMENTS-4597", "title": "Payments scenario 4597", "data": {"sku": "SKU4597", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4597@example.com", "threshold": 970}},
    {"id": "PAYMENTS-4598", "title": "Payments scenario 4598", "data": {"sku": "SKU4598", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4598@example.com", "threshold": 980}},
    {"id": "PAYMENTS-4599", "title": "Payments scenario 4599", "data": {"sku": "SKU4599", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4599@example.com", "threshold": 990}},
    {"id": "PAYMENTS-4600", "title": "Payments scenario 4600", "data": {"sku": "SKU4600", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4600@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
