import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3631", "title": "Payments scenario 3631", "data": {"sku": "SKU3631", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3631@example.com", "threshold": 310}},
    {"id": "PAYMENTS-3632", "title": "Payments scenario 3632", "data": {"sku": "SKU3632", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3632@example.com", "threshold": 320}},
    {"id": "PAYMENTS-3633", "title": "Payments scenario 3633", "data": {"sku": "SKU3633", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3633@example.com", "threshold": 330}},
    {"id": "PAYMENTS-3634", "title": "Payments scenario 3634", "data": {"sku": "SKU3634", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3634@example.com", "threshold": 340}},
    {"id": "PAYMENTS-3635", "title": "Payments scenario 3635", "data": {"sku": "SKU3635", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3635@example.com", "threshold": 350}},
    {"id": "PAYMENTS-3636", "title": "Payments scenario 3636", "data": {"sku": "SKU3636", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3636@example.com", "threshold": 360}},
    {"id": "PAYMENTS-3637", "title": "Payments scenario 3637", "data": {"sku": "SKU3637", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3637@example.com", "threshold": 370}},
    {"id": "PAYMENTS-3638", "title": "Payments scenario 3638", "data": {"sku": "SKU3638", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3638@example.com", "threshold": 380}},
    {"id": "PAYMENTS-3639", "title": "Payments scenario 3639", "data": {"sku": "SKU3639", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3639@example.com", "threshold": 390}},
    {"id": "PAYMENTS-3640", "title": "Payments scenario 3640", "data": {"sku": "SKU3640", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3640@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
