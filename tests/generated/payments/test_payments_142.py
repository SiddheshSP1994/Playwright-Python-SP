import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8491", "title": "Payments scenario 8491", "data": {"sku": "SKU8491", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8491@example.com", "threshold": 910}},
    {"id": "PAYMENTS-8492", "title": "Payments scenario 8492", "data": {"sku": "SKU8492", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8492@example.com", "threshold": 920}},
    {"id": "PAYMENTS-8493", "title": "Payments scenario 8493", "data": {"sku": "SKU8493", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8493@example.com", "threshold": 930}},
    {"id": "PAYMENTS-8494", "title": "Payments scenario 8494", "data": {"sku": "SKU8494", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8494@example.com", "threshold": 940}},
    {"id": "PAYMENTS-8495", "title": "Payments scenario 8495", "data": {"sku": "SKU8495", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8495@example.com", "threshold": 950}},
    {"id": "PAYMENTS-8496", "title": "Payments scenario 8496", "data": {"sku": "SKU8496", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8496@example.com", "threshold": 960}},
    {"id": "PAYMENTS-8497", "title": "Payments scenario 8497", "data": {"sku": "SKU8497", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8497@example.com", "threshold": 970}},
    {"id": "PAYMENTS-8498", "title": "Payments scenario 8498", "data": {"sku": "SKU8498", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8498@example.com", "threshold": 980}},
    {"id": "PAYMENTS-8499", "title": "Payments scenario 8499", "data": {"sku": "SKU8499", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8499@example.com", "threshold": 990}},
    {"id": "PAYMENTS-8500", "title": "Payments scenario 8500", "data": {"sku": "SKU8500", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8500@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
