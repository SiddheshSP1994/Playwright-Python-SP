import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0931", "title": "Payments scenario 931", "data": {"sku": "SKU931", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user931@example.com", "threshold": 310}},
    {"id": "PAYMENTS-0932", "title": "Payments scenario 932", "data": {"sku": "SKU932", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user932@example.com", "threshold": 320}},
    {"id": "PAYMENTS-0933", "title": "Payments scenario 933", "data": {"sku": "SKU933", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user933@example.com", "threshold": 330}},
    {"id": "PAYMENTS-0934", "title": "Payments scenario 934", "data": {"sku": "SKU934", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user934@example.com", "threshold": 340}},
    {"id": "PAYMENTS-0935", "title": "Payments scenario 935", "data": {"sku": "SKU935", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user935@example.com", "threshold": 350}},
    {"id": "PAYMENTS-0936", "title": "Payments scenario 936", "data": {"sku": "SKU936", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user936@example.com", "threshold": 360}},
    {"id": "PAYMENTS-0937", "title": "Payments scenario 937", "data": {"sku": "SKU937", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user937@example.com", "threshold": 370}},
    {"id": "PAYMENTS-0938", "title": "Payments scenario 938", "data": {"sku": "SKU938", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user938@example.com", "threshold": 380}},
    {"id": "PAYMENTS-0939", "title": "Payments scenario 939", "data": {"sku": "SKU939", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user939@example.com", "threshold": 390}},
    {"id": "PAYMENTS-0940", "title": "Payments scenario 940", "data": {"sku": "SKU940", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user940@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
