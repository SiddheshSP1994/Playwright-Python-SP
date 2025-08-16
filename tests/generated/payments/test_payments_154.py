import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-9211", "title": "Payments scenario 9211", "data": {"sku": "SKU9211", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9211@example.com", "threshold": 110}},
    {"id": "PAYMENTS-9212", "title": "Payments scenario 9212", "data": {"sku": "SKU9212", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9212@example.com", "threshold": 120}},
    {"id": "PAYMENTS-9213", "title": "Payments scenario 9213", "data": {"sku": "SKU9213", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9213@example.com", "threshold": 130}},
    {"id": "PAYMENTS-9214", "title": "Payments scenario 9214", "data": {"sku": "SKU9214", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9214@example.com", "threshold": 140}},
    {"id": "PAYMENTS-9215", "title": "Payments scenario 9215", "data": {"sku": "SKU9215", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9215@example.com", "threshold": 150}},
    {"id": "PAYMENTS-9216", "title": "Payments scenario 9216", "data": {"sku": "SKU9216", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9216@example.com", "threshold": 160}},
    {"id": "PAYMENTS-9217", "title": "Payments scenario 9217", "data": {"sku": "SKU9217", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9217@example.com", "threshold": 170}},
    {"id": "PAYMENTS-9218", "title": "Payments scenario 9218", "data": {"sku": "SKU9218", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9218@example.com", "threshold": 180}},
    {"id": "PAYMENTS-9219", "title": "Payments scenario 9219", "data": {"sku": "SKU9219", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9219@example.com", "threshold": 190}},
    {"id": "PAYMENTS-9220", "title": "Payments scenario 9220", "data": {"sku": "SKU9220", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9220@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
