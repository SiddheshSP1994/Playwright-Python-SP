import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-9931", "title": "Payments scenario 9931", "data": {"sku": "SKU9931", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9931@example.com", "threshold": 310}},
    {"id": "PAYMENTS-9932", "title": "Payments scenario 9932", "data": {"sku": "SKU9932", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9932@example.com", "threshold": 320}},
    {"id": "PAYMENTS-9933", "title": "Payments scenario 9933", "data": {"sku": "SKU9933", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9933@example.com", "threshold": 330}},
    {"id": "PAYMENTS-9934", "title": "Payments scenario 9934", "data": {"sku": "SKU9934", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9934@example.com", "threshold": 340}},
    {"id": "PAYMENTS-9935", "title": "Payments scenario 9935", "data": {"sku": "SKU9935", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9935@example.com", "threshold": 350}},
    {"id": "PAYMENTS-9936", "title": "Payments scenario 9936", "data": {"sku": "SKU9936", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9936@example.com", "threshold": 360}},
    {"id": "PAYMENTS-9937", "title": "Payments scenario 9937", "data": {"sku": "SKU9937", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9937@example.com", "threshold": 370}},
    {"id": "PAYMENTS-9938", "title": "Payments scenario 9938", "data": {"sku": "SKU9938", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9938@example.com", "threshold": 380}},
    {"id": "PAYMENTS-9939", "title": "Payments scenario 9939", "data": {"sku": "SKU9939", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9939@example.com", "threshold": 390}},
    {"id": "PAYMENTS-9940", "title": "Payments scenario 9940", "data": {"sku": "SKU9940", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9940@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
