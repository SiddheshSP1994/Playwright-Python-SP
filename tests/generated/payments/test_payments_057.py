import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3391", "title": "Payments scenario 3391", "data": {"sku": "SKU3391", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3391@example.com", "threshold": 910}},
    {"id": "PAYMENTS-3392", "title": "Payments scenario 3392", "data": {"sku": "SKU3392", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3392@example.com", "threshold": 920}},
    {"id": "PAYMENTS-3393", "title": "Payments scenario 3393", "data": {"sku": "SKU3393", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3393@example.com", "threshold": 930}},
    {"id": "PAYMENTS-3394", "title": "Payments scenario 3394", "data": {"sku": "SKU3394", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3394@example.com", "threshold": 940}},
    {"id": "PAYMENTS-3395", "title": "Payments scenario 3395", "data": {"sku": "SKU3395", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3395@example.com", "threshold": 950}},
    {"id": "PAYMENTS-3396", "title": "Payments scenario 3396", "data": {"sku": "SKU3396", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3396@example.com", "threshold": 960}},
    {"id": "PAYMENTS-3397", "title": "Payments scenario 3397", "data": {"sku": "SKU3397", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3397@example.com", "threshold": 970}},
    {"id": "PAYMENTS-3398", "title": "Payments scenario 3398", "data": {"sku": "SKU3398", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3398@example.com", "threshold": 980}},
    {"id": "PAYMENTS-3399", "title": "Payments scenario 3399", "data": {"sku": "SKU3399", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3399@example.com", "threshold": 990}},
    {"id": "PAYMENTS-3400", "title": "Payments scenario 3400", "data": {"sku": "SKU3400", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3400@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
