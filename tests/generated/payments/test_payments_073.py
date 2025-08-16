import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4351", "title": "Payments scenario 4351", "data": {"sku": "SKU4351", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4351@example.com", "threshold": 510}},
    {"id": "PAYMENTS-4352", "title": "Payments scenario 4352", "data": {"sku": "SKU4352", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4352@example.com", "threshold": 520}},
    {"id": "PAYMENTS-4353", "title": "Payments scenario 4353", "data": {"sku": "SKU4353", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4353@example.com", "threshold": 530}},
    {"id": "PAYMENTS-4354", "title": "Payments scenario 4354", "data": {"sku": "SKU4354", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4354@example.com", "threshold": 540}},
    {"id": "PAYMENTS-4355", "title": "Payments scenario 4355", "data": {"sku": "SKU4355", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4355@example.com", "threshold": 550}},
    {"id": "PAYMENTS-4356", "title": "Payments scenario 4356", "data": {"sku": "SKU4356", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4356@example.com", "threshold": 560}},
    {"id": "PAYMENTS-4357", "title": "Payments scenario 4357", "data": {"sku": "SKU4357", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4357@example.com", "threshold": 570}},
    {"id": "PAYMENTS-4358", "title": "Payments scenario 4358", "data": {"sku": "SKU4358", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4358@example.com", "threshold": 580}},
    {"id": "PAYMENTS-4359", "title": "Payments scenario 4359", "data": {"sku": "SKU4359", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4359@example.com", "threshold": 590}},
    {"id": "PAYMENTS-4360", "title": "Payments scenario 4360", "data": {"sku": "SKU4360", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4360@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
