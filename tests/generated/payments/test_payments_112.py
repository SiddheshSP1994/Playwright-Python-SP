import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6691", "title": "Payments scenario 6691", "data": {"sku": "SKU6691", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6691@example.com", "threshold": 910}},
    {"id": "PAYMENTS-6692", "title": "Payments scenario 6692", "data": {"sku": "SKU6692", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6692@example.com", "threshold": 920}},
    {"id": "PAYMENTS-6693", "title": "Payments scenario 6693", "data": {"sku": "SKU6693", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6693@example.com", "threshold": 930}},
    {"id": "PAYMENTS-6694", "title": "Payments scenario 6694", "data": {"sku": "SKU6694", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6694@example.com", "threshold": 940}},
    {"id": "PAYMENTS-6695", "title": "Payments scenario 6695", "data": {"sku": "SKU6695", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6695@example.com", "threshold": 950}},
    {"id": "PAYMENTS-6696", "title": "Payments scenario 6696", "data": {"sku": "SKU6696", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6696@example.com", "threshold": 960}},
    {"id": "PAYMENTS-6697", "title": "Payments scenario 6697", "data": {"sku": "SKU6697", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6697@example.com", "threshold": 970}},
    {"id": "PAYMENTS-6698", "title": "Payments scenario 6698", "data": {"sku": "SKU6698", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6698@example.com", "threshold": 980}},
    {"id": "PAYMENTS-6699", "title": "Payments scenario 6699", "data": {"sku": "SKU6699", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6699@example.com", "threshold": 990}},
    {"id": "PAYMENTS-6700", "title": "Payments scenario 6700", "data": {"sku": "SKU6700", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6700@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
