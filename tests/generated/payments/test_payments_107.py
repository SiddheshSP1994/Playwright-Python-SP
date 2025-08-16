import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6391", "title": "Payments scenario 6391", "data": {"sku": "SKU6391", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6391@example.com", "threshold": 910}},
    {"id": "PAYMENTS-6392", "title": "Payments scenario 6392", "data": {"sku": "SKU6392", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6392@example.com", "threshold": 920}},
    {"id": "PAYMENTS-6393", "title": "Payments scenario 6393", "data": {"sku": "SKU6393", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6393@example.com", "threshold": 930}},
    {"id": "PAYMENTS-6394", "title": "Payments scenario 6394", "data": {"sku": "SKU6394", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6394@example.com", "threshold": 940}},
    {"id": "PAYMENTS-6395", "title": "Payments scenario 6395", "data": {"sku": "SKU6395", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6395@example.com", "threshold": 950}},
    {"id": "PAYMENTS-6396", "title": "Payments scenario 6396", "data": {"sku": "SKU6396", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6396@example.com", "threshold": 960}},
    {"id": "PAYMENTS-6397", "title": "Payments scenario 6397", "data": {"sku": "SKU6397", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6397@example.com", "threshold": 970}},
    {"id": "PAYMENTS-6398", "title": "Payments scenario 6398", "data": {"sku": "SKU6398", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6398@example.com", "threshold": 980}},
    {"id": "PAYMENTS-6399", "title": "Payments scenario 6399", "data": {"sku": "SKU6399", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6399@example.com", "threshold": 990}},
    {"id": "PAYMENTS-6400", "title": "Payments scenario 6400", "data": {"sku": "SKU6400", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6400@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
