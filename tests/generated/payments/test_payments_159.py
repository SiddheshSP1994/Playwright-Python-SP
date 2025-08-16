import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-9511", "title": "Payments scenario 9511", "data": {"sku": "SKU9511", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9511@example.com", "threshold": 110}},
    {"id": "PAYMENTS-9512", "title": "Payments scenario 9512", "data": {"sku": "SKU9512", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9512@example.com", "threshold": 120}},
    {"id": "PAYMENTS-9513", "title": "Payments scenario 9513", "data": {"sku": "SKU9513", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9513@example.com", "threshold": 130}},
    {"id": "PAYMENTS-9514", "title": "Payments scenario 9514", "data": {"sku": "SKU9514", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9514@example.com", "threshold": 140}},
    {"id": "PAYMENTS-9515", "title": "Payments scenario 9515", "data": {"sku": "SKU9515", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9515@example.com", "threshold": 150}},
    {"id": "PAYMENTS-9516", "title": "Payments scenario 9516", "data": {"sku": "SKU9516", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9516@example.com", "threshold": 160}},
    {"id": "PAYMENTS-9517", "title": "Payments scenario 9517", "data": {"sku": "SKU9517", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9517@example.com", "threshold": 170}},
    {"id": "PAYMENTS-9518", "title": "Payments scenario 9518", "data": {"sku": "SKU9518", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9518@example.com", "threshold": 180}},
    {"id": "PAYMENTS-9519", "title": "Payments scenario 9519", "data": {"sku": "SKU9519", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9519@example.com", "threshold": 190}},
    {"id": "PAYMENTS-9520", "title": "Payments scenario 9520", "data": {"sku": "SKU9520", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9520@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
