import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4711", "title": "Payments scenario 4711", "data": {"sku": "SKU4711", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4711@example.com", "threshold": 110}},
    {"id": "PAYMENTS-4712", "title": "Payments scenario 4712", "data": {"sku": "SKU4712", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4712@example.com", "threshold": 120}},
    {"id": "PAYMENTS-4713", "title": "Payments scenario 4713", "data": {"sku": "SKU4713", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4713@example.com", "threshold": 130}},
    {"id": "PAYMENTS-4714", "title": "Payments scenario 4714", "data": {"sku": "SKU4714", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4714@example.com", "threshold": 140}},
    {"id": "PAYMENTS-4715", "title": "Payments scenario 4715", "data": {"sku": "SKU4715", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4715@example.com", "threshold": 150}},
    {"id": "PAYMENTS-4716", "title": "Payments scenario 4716", "data": {"sku": "SKU4716", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4716@example.com", "threshold": 160}},
    {"id": "PAYMENTS-4717", "title": "Payments scenario 4717", "data": {"sku": "SKU4717", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4717@example.com", "threshold": 170}},
    {"id": "PAYMENTS-4718", "title": "Payments scenario 4718", "data": {"sku": "SKU4718", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4718@example.com", "threshold": 180}},
    {"id": "PAYMENTS-4719", "title": "Payments scenario 4719", "data": {"sku": "SKU4719", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4719@example.com", "threshold": 190}},
    {"id": "PAYMENTS-4720", "title": "Payments scenario 4720", "data": {"sku": "SKU4720", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4720@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
