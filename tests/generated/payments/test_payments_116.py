import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6931", "title": "Payments scenario 6931", "data": {"sku": "SKU6931", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6931@example.com", "threshold": 310}},
    {"id": "PAYMENTS-6932", "title": "Payments scenario 6932", "data": {"sku": "SKU6932", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6932@example.com", "threshold": 320}},
    {"id": "PAYMENTS-6933", "title": "Payments scenario 6933", "data": {"sku": "SKU6933", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6933@example.com", "threshold": 330}},
    {"id": "PAYMENTS-6934", "title": "Payments scenario 6934", "data": {"sku": "SKU6934", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6934@example.com", "threshold": 340}},
    {"id": "PAYMENTS-6935", "title": "Payments scenario 6935", "data": {"sku": "SKU6935", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6935@example.com", "threshold": 350}},
    {"id": "PAYMENTS-6936", "title": "Payments scenario 6936", "data": {"sku": "SKU6936", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6936@example.com", "threshold": 360}},
    {"id": "PAYMENTS-6937", "title": "Payments scenario 6937", "data": {"sku": "SKU6937", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6937@example.com", "threshold": 370}},
    {"id": "PAYMENTS-6938", "title": "Payments scenario 6938", "data": {"sku": "SKU6938", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6938@example.com", "threshold": 380}},
    {"id": "PAYMENTS-6939", "title": "Payments scenario 6939", "data": {"sku": "SKU6939", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6939@example.com", "threshold": 390}},
    {"id": "PAYMENTS-6940", "title": "Payments scenario 6940", "data": {"sku": "SKU6940", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6940@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
