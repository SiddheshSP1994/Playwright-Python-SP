import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3151", "title": "Payments scenario 3151", "data": {"sku": "SKU3151", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3151@example.com", "threshold": 510}},
    {"id": "PAYMENTS-3152", "title": "Payments scenario 3152", "data": {"sku": "SKU3152", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3152@example.com", "threshold": 520}},
    {"id": "PAYMENTS-3153", "title": "Payments scenario 3153", "data": {"sku": "SKU3153", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3153@example.com", "threshold": 530}},
    {"id": "PAYMENTS-3154", "title": "Payments scenario 3154", "data": {"sku": "SKU3154", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3154@example.com", "threshold": 540}},
    {"id": "PAYMENTS-3155", "title": "Payments scenario 3155", "data": {"sku": "SKU3155", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3155@example.com", "threshold": 550}},
    {"id": "PAYMENTS-3156", "title": "Payments scenario 3156", "data": {"sku": "SKU3156", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3156@example.com", "threshold": 560}},
    {"id": "PAYMENTS-3157", "title": "Payments scenario 3157", "data": {"sku": "SKU3157", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3157@example.com", "threshold": 570}},
    {"id": "PAYMENTS-3158", "title": "Payments scenario 3158", "data": {"sku": "SKU3158", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3158@example.com", "threshold": 580}},
    {"id": "PAYMENTS-3159", "title": "Payments scenario 3159", "data": {"sku": "SKU3159", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3159@example.com", "threshold": 590}},
    {"id": "PAYMENTS-3160", "title": "Payments scenario 3160", "data": {"sku": "SKU3160", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3160@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
