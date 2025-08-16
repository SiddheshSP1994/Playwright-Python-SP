import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-7111", "title": "Payments scenario 7111", "data": {"sku": "SKU7111", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7111@example.com", "threshold": 110}},
    {"id": "PAYMENTS-7112", "title": "Payments scenario 7112", "data": {"sku": "SKU7112", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7112@example.com", "threshold": 120}},
    {"id": "PAYMENTS-7113", "title": "Payments scenario 7113", "data": {"sku": "SKU7113", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7113@example.com", "threshold": 130}},
    {"id": "PAYMENTS-7114", "title": "Payments scenario 7114", "data": {"sku": "SKU7114", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7114@example.com", "threshold": 140}},
    {"id": "PAYMENTS-7115", "title": "Payments scenario 7115", "data": {"sku": "SKU7115", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7115@example.com", "threshold": 150}},
    {"id": "PAYMENTS-7116", "title": "Payments scenario 7116", "data": {"sku": "SKU7116", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7116@example.com", "threshold": 160}},
    {"id": "PAYMENTS-7117", "title": "Payments scenario 7117", "data": {"sku": "SKU7117", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7117@example.com", "threshold": 170}},
    {"id": "PAYMENTS-7118", "title": "Payments scenario 7118", "data": {"sku": "SKU7118", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7118@example.com", "threshold": 180}},
    {"id": "PAYMENTS-7119", "title": "Payments scenario 7119", "data": {"sku": "SKU7119", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7119@example.com", "threshold": 190}},
    {"id": "PAYMENTS-7120", "title": "Payments scenario 7120", "data": {"sku": "SKU7120", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7120@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
