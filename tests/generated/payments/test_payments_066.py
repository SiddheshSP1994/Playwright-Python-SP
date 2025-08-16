import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3931", "title": "Payments scenario 3931", "data": {"sku": "SKU3931", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3931@example.com", "threshold": 310}},
    {"id": "PAYMENTS-3932", "title": "Payments scenario 3932", "data": {"sku": "SKU3932", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3932@example.com", "threshold": 320}},
    {"id": "PAYMENTS-3933", "title": "Payments scenario 3933", "data": {"sku": "SKU3933", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3933@example.com", "threshold": 330}},
    {"id": "PAYMENTS-3934", "title": "Payments scenario 3934", "data": {"sku": "SKU3934", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3934@example.com", "threshold": 340}},
    {"id": "PAYMENTS-3935", "title": "Payments scenario 3935", "data": {"sku": "SKU3935", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3935@example.com", "threshold": 350}},
    {"id": "PAYMENTS-3936", "title": "Payments scenario 3936", "data": {"sku": "SKU3936", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3936@example.com", "threshold": 360}},
    {"id": "PAYMENTS-3937", "title": "Payments scenario 3937", "data": {"sku": "SKU3937", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3937@example.com", "threshold": 370}},
    {"id": "PAYMENTS-3938", "title": "Payments scenario 3938", "data": {"sku": "SKU3938", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3938@example.com", "threshold": 380}},
    {"id": "PAYMENTS-3939", "title": "Payments scenario 3939", "data": {"sku": "SKU3939", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3939@example.com", "threshold": 390}},
    {"id": "PAYMENTS-3940", "title": "Payments scenario 3940", "data": {"sku": "SKU3940", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3940@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
