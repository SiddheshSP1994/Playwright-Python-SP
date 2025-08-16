import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-7891", "title": "Payments scenario 7891", "data": {"sku": "SKU7891", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7891@example.com", "threshold": 910}},
    {"id": "PAYMENTS-7892", "title": "Payments scenario 7892", "data": {"sku": "SKU7892", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7892@example.com", "threshold": 920}},
    {"id": "PAYMENTS-7893", "title": "Payments scenario 7893", "data": {"sku": "SKU7893", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7893@example.com", "threshold": 930}},
    {"id": "PAYMENTS-7894", "title": "Payments scenario 7894", "data": {"sku": "SKU7894", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7894@example.com", "threshold": 940}},
    {"id": "PAYMENTS-7895", "title": "Payments scenario 7895", "data": {"sku": "SKU7895", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7895@example.com", "threshold": 950}},
    {"id": "PAYMENTS-7896", "title": "Payments scenario 7896", "data": {"sku": "SKU7896", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7896@example.com", "threshold": 960}},
    {"id": "PAYMENTS-7897", "title": "Payments scenario 7897", "data": {"sku": "SKU7897", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7897@example.com", "threshold": 970}},
    {"id": "PAYMENTS-7898", "title": "Payments scenario 7898", "data": {"sku": "SKU7898", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7898@example.com", "threshold": 980}},
    {"id": "PAYMENTS-7899", "title": "Payments scenario 7899", "data": {"sku": "SKU7899", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7899@example.com", "threshold": 990}},
    {"id": "PAYMENTS-7900", "title": "Payments scenario 7900", "data": {"sku": "SKU7900", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7900@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
