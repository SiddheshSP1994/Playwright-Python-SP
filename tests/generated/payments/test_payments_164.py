import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-9811", "title": "Payments scenario 9811", "data": {"sku": "SKU9811", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9811@example.com", "threshold": 110}},
    {"id": "PAYMENTS-9812", "title": "Payments scenario 9812", "data": {"sku": "SKU9812", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9812@example.com", "threshold": 120}},
    {"id": "PAYMENTS-9813", "title": "Payments scenario 9813", "data": {"sku": "SKU9813", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9813@example.com", "threshold": 130}},
    {"id": "PAYMENTS-9814", "title": "Payments scenario 9814", "data": {"sku": "SKU9814", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9814@example.com", "threshold": 140}},
    {"id": "PAYMENTS-9815", "title": "Payments scenario 9815", "data": {"sku": "SKU9815", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9815@example.com", "threshold": 150}},
    {"id": "PAYMENTS-9816", "title": "Payments scenario 9816", "data": {"sku": "SKU9816", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9816@example.com", "threshold": 160}},
    {"id": "PAYMENTS-9817", "title": "Payments scenario 9817", "data": {"sku": "SKU9817", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9817@example.com", "threshold": 170}},
    {"id": "PAYMENTS-9818", "title": "Payments scenario 9818", "data": {"sku": "SKU9818", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9818@example.com", "threshold": 180}},
    {"id": "PAYMENTS-9819", "title": "Payments scenario 9819", "data": {"sku": "SKU9819", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9819@example.com", "threshold": 190}},
    {"id": "PAYMENTS-9820", "title": "Payments scenario 9820", "data": {"sku": "SKU9820", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9820@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
