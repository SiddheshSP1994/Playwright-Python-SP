import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8731", "title": "Payments scenario 8731", "data": {"sku": "SKU8731", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8731@example.com", "threshold": 310}},
    {"id": "PAYMENTS-8732", "title": "Payments scenario 8732", "data": {"sku": "SKU8732", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8732@example.com", "threshold": 320}},
    {"id": "PAYMENTS-8733", "title": "Payments scenario 8733", "data": {"sku": "SKU8733", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8733@example.com", "threshold": 330}},
    {"id": "PAYMENTS-8734", "title": "Payments scenario 8734", "data": {"sku": "SKU8734", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8734@example.com", "threshold": 340}},
    {"id": "PAYMENTS-8735", "title": "Payments scenario 8735", "data": {"sku": "SKU8735", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8735@example.com", "threshold": 350}},
    {"id": "PAYMENTS-8736", "title": "Payments scenario 8736", "data": {"sku": "SKU8736", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8736@example.com", "threshold": 360}},
    {"id": "PAYMENTS-8737", "title": "Payments scenario 8737", "data": {"sku": "SKU8737", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8737@example.com", "threshold": 370}},
    {"id": "PAYMENTS-8738", "title": "Payments scenario 8738", "data": {"sku": "SKU8738", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8738@example.com", "threshold": 380}},
    {"id": "PAYMENTS-8739", "title": "Payments scenario 8739", "data": {"sku": "SKU8739", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8739@example.com", "threshold": 390}},
    {"id": "PAYMENTS-8740", "title": "Payments scenario 8740", "data": {"sku": "SKU8740", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8740@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
