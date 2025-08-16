import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1231", "title": "Payments scenario 1231", "data": {"sku": "SKU1231", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1231@example.com", "threshold": 310}},
    {"id": "PAYMENTS-1232", "title": "Payments scenario 1232", "data": {"sku": "SKU1232", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1232@example.com", "threshold": 320}},
    {"id": "PAYMENTS-1233", "title": "Payments scenario 1233", "data": {"sku": "SKU1233", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1233@example.com", "threshold": 330}},
    {"id": "PAYMENTS-1234", "title": "Payments scenario 1234", "data": {"sku": "SKU1234", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1234@example.com", "threshold": 340}},
    {"id": "PAYMENTS-1235", "title": "Payments scenario 1235", "data": {"sku": "SKU1235", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1235@example.com", "threshold": 350}},
    {"id": "PAYMENTS-1236", "title": "Payments scenario 1236", "data": {"sku": "SKU1236", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1236@example.com", "threshold": 360}},
    {"id": "PAYMENTS-1237", "title": "Payments scenario 1237", "data": {"sku": "SKU1237", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1237@example.com", "threshold": 370}},
    {"id": "PAYMENTS-1238", "title": "Payments scenario 1238", "data": {"sku": "SKU1238", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1238@example.com", "threshold": 380}},
    {"id": "PAYMENTS-1239", "title": "Payments scenario 1239", "data": {"sku": "SKU1239", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1239@example.com", "threshold": 390}},
    {"id": "PAYMENTS-1240", "title": "Payments scenario 1240", "data": {"sku": "SKU1240", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1240@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
