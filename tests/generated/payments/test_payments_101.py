import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6031", "title": "Payments scenario 6031", "data": {"sku": "SKU6031", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6031@example.com", "threshold": 310}},
    {"id": "PAYMENTS-6032", "title": "Payments scenario 6032", "data": {"sku": "SKU6032", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6032@example.com", "threshold": 320}},
    {"id": "PAYMENTS-6033", "title": "Payments scenario 6033", "data": {"sku": "SKU6033", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6033@example.com", "threshold": 330}},
    {"id": "PAYMENTS-6034", "title": "Payments scenario 6034", "data": {"sku": "SKU6034", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6034@example.com", "threshold": 340}},
    {"id": "PAYMENTS-6035", "title": "Payments scenario 6035", "data": {"sku": "SKU6035", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6035@example.com", "threshold": 350}},
    {"id": "PAYMENTS-6036", "title": "Payments scenario 6036", "data": {"sku": "SKU6036", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6036@example.com", "threshold": 360}},
    {"id": "PAYMENTS-6037", "title": "Payments scenario 6037", "data": {"sku": "SKU6037", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6037@example.com", "threshold": 370}},
    {"id": "PAYMENTS-6038", "title": "Payments scenario 6038", "data": {"sku": "SKU6038", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6038@example.com", "threshold": 380}},
    {"id": "PAYMENTS-6039", "title": "Payments scenario 6039", "data": {"sku": "SKU6039", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6039@example.com", "threshold": 390}},
    {"id": "PAYMENTS-6040", "title": "Payments scenario 6040", "data": {"sku": "SKU6040", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6040@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
