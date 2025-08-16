import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2731", "title": "Payments scenario 2731", "data": {"sku": "SKU2731", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2731@example.com", "threshold": 310}},
    {"id": "PAYMENTS-2732", "title": "Payments scenario 2732", "data": {"sku": "SKU2732", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2732@example.com", "threshold": 320}},
    {"id": "PAYMENTS-2733", "title": "Payments scenario 2733", "data": {"sku": "SKU2733", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2733@example.com", "threshold": 330}},
    {"id": "PAYMENTS-2734", "title": "Payments scenario 2734", "data": {"sku": "SKU2734", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2734@example.com", "threshold": 340}},
    {"id": "PAYMENTS-2735", "title": "Payments scenario 2735", "data": {"sku": "SKU2735", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2735@example.com", "threshold": 350}},
    {"id": "PAYMENTS-2736", "title": "Payments scenario 2736", "data": {"sku": "SKU2736", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2736@example.com", "threshold": 360}},
    {"id": "PAYMENTS-2737", "title": "Payments scenario 2737", "data": {"sku": "SKU2737", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2737@example.com", "threshold": 370}},
    {"id": "PAYMENTS-2738", "title": "Payments scenario 2738", "data": {"sku": "SKU2738", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2738@example.com", "threshold": 380}},
    {"id": "PAYMENTS-2739", "title": "Payments scenario 2739", "data": {"sku": "SKU2739", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2739@example.com", "threshold": 390}},
    {"id": "PAYMENTS-2740", "title": "Payments scenario 2740", "data": {"sku": "SKU2740", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2740@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
