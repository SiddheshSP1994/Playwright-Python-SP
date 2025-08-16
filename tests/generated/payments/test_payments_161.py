import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-9631", "title": "Payments scenario 9631", "data": {"sku": "SKU9631", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9631@example.com", "threshold": 310}},
    {"id": "PAYMENTS-9632", "title": "Payments scenario 9632", "data": {"sku": "SKU9632", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9632@example.com", "threshold": 320}},
    {"id": "PAYMENTS-9633", "title": "Payments scenario 9633", "data": {"sku": "SKU9633", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9633@example.com", "threshold": 330}},
    {"id": "PAYMENTS-9634", "title": "Payments scenario 9634", "data": {"sku": "SKU9634", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9634@example.com", "threshold": 340}},
    {"id": "PAYMENTS-9635", "title": "Payments scenario 9635", "data": {"sku": "SKU9635", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9635@example.com", "threshold": 350}},
    {"id": "PAYMENTS-9636", "title": "Payments scenario 9636", "data": {"sku": "SKU9636", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9636@example.com", "threshold": 360}},
    {"id": "PAYMENTS-9637", "title": "Payments scenario 9637", "data": {"sku": "SKU9637", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9637@example.com", "threshold": 370}},
    {"id": "PAYMENTS-9638", "title": "Payments scenario 9638", "data": {"sku": "SKU9638", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9638@example.com", "threshold": 380}},
    {"id": "PAYMENTS-9639", "title": "Payments scenario 9639", "data": {"sku": "SKU9639", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9639@example.com", "threshold": 390}},
    {"id": "PAYMENTS-9640", "title": "Payments scenario 9640", "data": {"sku": "SKU9640", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9640@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
