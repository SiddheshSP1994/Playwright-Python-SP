import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0151", "title": "Payments scenario 151", "data": {"sku": "SKU151", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user151@example.com", "threshold": 510}},
    {"id": "PAYMENTS-0152", "title": "Payments scenario 152", "data": {"sku": "SKU152", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user152@example.com", "threshold": 520}},
    {"id": "PAYMENTS-0153", "title": "Payments scenario 153", "data": {"sku": "SKU153", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user153@example.com", "threshold": 530}},
    {"id": "PAYMENTS-0154", "title": "Payments scenario 154", "data": {"sku": "SKU154", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user154@example.com", "threshold": 540}},
    {"id": "PAYMENTS-0155", "title": "Payments scenario 155", "data": {"sku": "SKU155", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user155@example.com", "threshold": 550}},
    {"id": "PAYMENTS-0156", "title": "Payments scenario 156", "data": {"sku": "SKU156", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user156@example.com", "threshold": 560}},
    {"id": "PAYMENTS-0157", "title": "Payments scenario 157", "data": {"sku": "SKU157", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user157@example.com", "threshold": 570}},
    {"id": "PAYMENTS-0158", "title": "Payments scenario 158", "data": {"sku": "SKU158", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user158@example.com", "threshold": 580}},
    {"id": "PAYMENTS-0159", "title": "Payments scenario 159", "data": {"sku": "SKU159", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user159@example.com", "threshold": 590}},
    {"id": "PAYMENTS-0160", "title": "Payments scenario 160", "data": {"sku": "SKU160", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user160@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
