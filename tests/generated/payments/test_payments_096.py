import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5731", "title": "Payments scenario 5731", "data": {"sku": "SKU5731", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5731@example.com", "threshold": 310}},
    {"id": "PAYMENTS-5732", "title": "Payments scenario 5732", "data": {"sku": "SKU5732", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5732@example.com", "threshold": 320}},
    {"id": "PAYMENTS-5733", "title": "Payments scenario 5733", "data": {"sku": "SKU5733", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5733@example.com", "threshold": 330}},
    {"id": "PAYMENTS-5734", "title": "Payments scenario 5734", "data": {"sku": "SKU5734", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5734@example.com", "threshold": 340}},
    {"id": "PAYMENTS-5735", "title": "Payments scenario 5735", "data": {"sku": "SKU5735", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5735@example.com", "threshold": 350}},
    {"id": "PAYMENTS-5736", "title": "Payments scenario 5736", "data": {"sku": "SKU5736", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5736@example.com", "threshold": 360}},
    {"id": "PAYMENTS-5737", "title": "Payments scenario 5737", "data": {"sku": "SKU5737", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5737@example.com", "threshold": 370}},
    {"id": "PAYMENTS-5738", "title": "Payments scenario 5738", "data": {"sku": "SKU5738", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5738@example.com", "threshold": 380}},
    {"id": "PAYMENTS-5739", "title": "Payments scenario 5739", "data": {"sku": "SKU5739", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5739@example.com", "threshold": 390}},
    {"id": "PAYMENTS-5740", "title": "Payments scenario 5740", "data": {"sku": "SKU5740", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5740@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
