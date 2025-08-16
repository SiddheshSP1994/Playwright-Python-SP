import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-7711", "title": "Payments scenario 7711", "data": {"sku": "SKU7711", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7711@example.com", "threshold": 110}},
    {"id": "PAYMENTS-7712", "title": "Payments scenario 7712", "data": {"sku": "SKU7712", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7712@example.com", "threshold": 120}},
    {"id": "PAYMENTS-7713", "title": "Payments scenario 7713", "data": {"sku": "SKU7713", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7713@example.com", "threshold": 130}},
    {"id": "PAYMENTS-7714", "title": "Payments scenario 7714", "data": {"sku": "SKU7714", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7714@example.com", "threshold": 140}},
    {"id": "PAYMENTS-7715", "title": "Payments scenario 7715", "data": {"sku": "SKU7715", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7715@example.com", "threshold": 150}},
    {"id": "PAYMENTS-7716", "title": "Payments scenario 7716", "data": {"sku": "SKU7716", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7716@example.com", "threshold": 160}},
    {"id": "PAYMENTS-7717", "title": "Payments scenario 7717", "data": {"sku": "SKU7717", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7717@example.com", "threshold": 170}},
    {"id": "PAYMENTS-7718", "title": "Payments scenario 7718", "data": {"sku": "SKU7718", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7718@example.com", "threshold": 180}},
    {"id": "PAYMENTS-7719", "title": "Payments scenario 7719", "data": {"sku": "SKU7719", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7719@example.com", "threshold": 190}},
    {"id": "PAYMENTS-7720", "title": "Payments scenario 7720", "data": {"sku": "SKU7720", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7720@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
