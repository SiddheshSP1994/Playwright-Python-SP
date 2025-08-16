import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-9391", "title": "Payments scenario 9391", "data": {"sku": "SKU9391", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9391@example.com", "threshold": 910}},
    {"id": "PAYMENTS-9392", "title": "Payments scenario 9392", "data": {"sku": "SKU9392", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9392@example.com", "threshold": 920}},
    {"id": "PAYMENTS-9393", "title": "Payments scenario 9393", "data": {"sku": "SKU9393", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9393@example.com", "threshold": 930}},
    {"id": "PAYMENTS-9394", "title": "Payments scenario 9394", "data": {"sku": "SKU9394", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9394@example.com", "threshold": 940}},
    {"id": "PAYMENTS-9395", "title": "Payments scenario 9395", "data": {"sku": "SKU9395", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9395@example.com", "threshold": 950}},
    {"id": "PAYMENTS-9396", "title": "Payments scenario 9396", "data": {"sku": "SKU9396", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9396@example.com", "threshold": 960}},
    {"id": "PAYMENTS-9397", "title": "Payments scenario 9397", "data": {"sku": "SKU9397", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9397@example.com", "threshold": 970}},
    {"id": "PAYMENTS-9398", "title": "Payments scenario 9398", "data": {"sku": "SKU9398", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9398@example.com", "threshold": 980}},
    {"id": "PAYMENTS-9399", "title": "Payments scenario 9399", "data": {"sku": "SKU9399", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9399@example.com", "threshold": 990}},
    {"id": "PAYMENTS-9400", "title": "Payments scenario 9400", "data": {"sku": "SKU9400", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9400@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
