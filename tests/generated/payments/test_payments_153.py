import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-9151", "title": "Payments scenario 9151", "data": {"sku": "SKU9151", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9151@example.com", "threshold": 510}},
    {"id": "PAYMENTS-9152", "title": "Payments scenario 9152", "data": {"sku": "SKU9152", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9152@example.com", "threshold": 520}},
    {"id": "PAYMENTS-9153", "title": "Payments scenario 9153", "data": {"sku": "SKU9153", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9153@example.com", "threshold": 530}},
    {"id": "PAYMENTS-9154", "title": "Payments scenario 9154", "data": {"sku": "SKU9154", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9154@example.com", "threshold": 540}},
    {"id": "PAYMENTS-9155", "title": "Payments scenario 9155", "data": {"sku": "SKU9155", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9155@example.com", "threshold": 550}},
    {"id": "PAYMENTS-9156", "title": "Payments scenario 9156", "data": {"sku": "SKU9156", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9156@example.com", "threshold": 560}},
    {"id": "PAYMENTS-9157", "title": "Payments scenario 9157", "data": {"sku": "SKU9157", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9157@example.com", "threshold": 570}},
    {"id": "PAYMENTS-9158", "title": "Payments scenario 9158", "data": {"sku": "SKU9158", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9158@example.com", "threshold": 580}},
    {"id": "PAYMENTS-9159", "title": "Payments scenario 9159", "data": {"sku": "SKU9159", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9159@example.com", "threshold": 590}},
    {"id": "PAYMENTS-9160", "title": "Payments scenario 9160", "data": {"sku": "SKU9160", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9160@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
