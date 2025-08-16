import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3511", "title": "Payments scenario 3511", "data": {"sku": "SKU3511", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3511@example.com", "threshold": 110}},
    {"id": "PAYMENTS-3512", "title": "Payments scenario 3512", "data": {"sku": "SKU3512", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3512@example.com", "threshold": 120}},
    {"id": "PAYMENTS-3513", "title": "Payments scenario 3513", "data": {"sku": "SKU3513", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3513@example.com", "threshold": 130}},
    {"id": "PAYMENTS-3514", "title": "Payments scenario 3514", "data": {"sku": "SKU3514", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3514@example.com", "threshold": 140}},
    {"id": "PAYMENTS-3515", "title": "Payments scenario 3515", "data": {"sku": "SKU3515", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3515@example.com", "threshold": 150}},
    {"id": "PAYMENTS-3516", "title": "Payments scenario 3516", "data": {"sku": "SKU3516", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3516@example.com", "threshold": 160}},
    {"id": "PAYMENTS-3517", "title": "Payments scenario 3517", "data": {"sku": "SKU3517", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3517@example.com", "threshold": 170}},
    {"id": "PAYMENTS-3518", "title": "Payments scenario 3518", "data": {"sku": "SKU3518", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3518@example.com", "threshold": 180}},
    {"id": "PAYMENTS-3519", "title": "Payments scenario 3519", "data": {"sku": "SKU3519", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3519@example.com", "threshold": 190}},
    {"id": "PAYMENTS-3520", "title": "Payments scenario 3520", "data": {"sku": "SKU3520", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3520@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
