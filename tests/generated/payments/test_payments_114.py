import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6811", "title": "Payments scenario 6811", "data": {"sku": "SKU6811", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6811@example.com", "threshold": 110}},
    {"id": "PAYMENTS-6812", "title": "Payments scenario 6812", "data": {"sku": "SKU6812", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6812@example.com", "threshold": 120}},
    {"id": "PAYMENTS-6813", "title": "Payments scenario 6813", "data": {"sku": "SKU6813", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6813@example.com", "threshold": 130}},
    {"id": "PAYMENTS-6814", "title": "Payments scenario 6814", "data": {"sku": "SKU6814", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6814@example.com", "threshold": 140}},
    {"id": "PAYMENTS-6815", "title": "Payments scenario 6815", "data": {"sku": "SKU6815", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6815@example.com", "threshold": 150}},
    {"id": "PAYMENTS-6816", "title": "Payments scenario 6816", "data": {"sku": "SKU6816", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6816@example.com", "threshold": 160}},
    {"id": "PAYMENTS-6817", "title": "Payments scenario 6817", "data": {"sku": "SKU6817", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6817@example.com", "threshold": 170}},
    {"id": "PAYMENTS-6818", "title": "Payments scenario 6818", "data": {"sku": "SKU6818", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6818@example.com", "threshold": 180}},
    {"id": "PAYMENTS-6819", "title": "Payments scenario 6819", "data": {"sku": "SKU6819", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6819@example.com", "threshold": 190}},
    {"id": "PAYMENTS-6820", "title": "Payments scenario 6820", "data": {"sku": "SKU6820", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6820@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
