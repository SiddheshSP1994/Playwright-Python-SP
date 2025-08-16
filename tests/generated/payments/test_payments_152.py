import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-9091", "title": "Payments scenario 9091", "data": {"sku": "SKU9091", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9091@example.com", "threshold": 910}},
    {"id": "PAYMENTS-9092", "title": "Payments scenario 9092", "data": {"sku": "SKU9092", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9092@example.com", "threshold": 920}},
    {"id": "PAYMENTS-9093", "title": "Payments scenario 9093", "data": {"sku": "SKU9093", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9093@example.com", "threshold": 930}},
    {"id": "PAYMENTS-9094", "title": "Payments scenario 9094", "data": {"sku": "SKU9094", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9094@example.com", "threshold": 940}},
    {"id": "PAYMENTS-9095", "title": "Payments scenario 9095", "data": {"sku": "SKU9095", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9095@example.com", "threshold": 950}},
    {"id": "PAYMENTS-9096", "title": "Payments scenario 9096", "data": {"sku": "SKU9096", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9096@example.com", "threshold": 960}},
    {"id": "PAYMENTS-9097", "title": "Payments scenario 9097", "data": {"sku": "SKU9097", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9097@example.com", "threshold": 970}},
    {"id": "PAYMENTS-9098", "title": "Payments scenario 9098", "data": {"sku": "SKU9098", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9098@example.com", "threshold": 980}},
    {"id": "PAYMENTS-9099", "title": "Payments scenario 9099", "data": {"sku": "SKU9099", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9099@example.com", "threshold": 990}},
    {"id": "PAYMENTS-9100", "title": "Payments scenario 9100", "data": {"sku": "SKU9100", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9100@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
