import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-7351", "title": "Payments scenario 7351", "data": {"sku": "SKU7351", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7351@example.com", "threshold": 510}},
    {"id": "PAYMENTS-7352", "title": "Payments scenario 7352", "data": {"sku": "SKU7352", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7352@example.com", "threshold": 520}},
    {"id": "PAYMENTS-7353", "title": "Payments scenario 7353", "data": {"sku": "SKU7353", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7353@example.com", "threshold": 530}},
    {"id": "PAYMENTS-7354", "title": "Payments scenario 7354", "data": {"sku": "SKU7354", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7354@example.com", "threshold": 540}},
    {"id": "PAYMENTS-7355", "title": "Payments scenario 7355", "data": {"sku": "SKU7355", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7355@example.com", "threshold": 550}},
    {"id": "PAYMENTS-7356", "title": "Payments scenario 7356", "data": {"sku": "SKU7356", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7356@example.com", "threshold": 560}},
    {"id": "PAYMENTS-7357", "title": "Payments scenario 7357", "data": {"sku": "SKU7357", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7357@example.com", "threshold": 570}},
    {"id": "PAYMENTS-7358", "title": "Payments scenario 7358", "data": {"sku": "SKU7358", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7358@example.com", "threshold": 580}},
    {"id": "PAYMENTS-7359", "title": "Payments scenario 7359", "data": {"sku": "SKU7359", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7359@example.com", "threshold": 590}},
    {"id": "PAYMENTS-7360", "title": "Payments scenario 7360", "data": {"sku": "SKU7360", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7360@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
