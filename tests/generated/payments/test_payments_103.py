import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6151", "title": "Payments scenario 6151", "data": {"sku": "SKU6151", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6151@example.com", "threshold": 510}},
    {"id": "PAYMENTS-6152", "title": "Payments scenario 6152", "data": {"sku": "SKU6152", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6152@example.com", "threshold": 520}},
    {"id": "PAYMENTS-6153", "title": "Payments scenario 6153", "data": {"sku": "SKU6153", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6153@example.com", "threshold": 530}},
    {"id": "PAYMENTS-6154", "title": "Payments scenario 6154", "data": {"sku": "SKU6154", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6154@example.com", "threshold": 540}},
    {"id": "PAYMENTS-6155", "title": "Payments scenario 6155", "data": {"sku": "SKU6155", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6155@example.com", "threshold": 550}},
    {"id": "PAYMENTS-6156", "title": "Payments scenario 6156", "data": {"sku": "SKU6156", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6156@example.com", "threshold": 560}},
    {"id": "PAYMENTS-6157", "title": "Payments scenario 6157", "data": {"sku": "SKU6157", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6157@example.com", "threshold": 570}},
    {"id": "PAYMENTS-6158", "title": "Payments scenario 6158", "data": {"sku": "SKU6158", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6158@example.com", "threshold": 580}},
    {"id": "PAYMENTS-6159", "title": "Payments scenario 6159", "data": {"sku": "SKU6159", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6159@example.com", "threshold": 590}},
    {"id": "PAYMENTS-6160", "title": "Payments scenario 6160", "data": {"sku": "SKU6160", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6160@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
