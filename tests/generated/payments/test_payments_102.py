import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6091", "title": "Payments scenario 6091", "data": {"sku": "SKU6091", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6091@example.com", "threshold": 910}},
    {"id": "PAYMENTS-6092", "title": "Payments scenario 6092", "data": {"sku": "SKU6092", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6092@example.com", "threshold": 920}},
    {"id": "PAYMENTS-6093", "title": "Payments scenario 6093", "data": {"sku": "SKU6093", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6093@example.com", "threshold": 930}},
    {"id": "PAYMENTS-6094", "title": "Payments scenario 6094", "data": {"sku": "SKU6094", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6094@example.com", "threshold": 940}},
    {"id": "PAYMENTS-6095", "title": "Payments scenario 6095", "data": {"sku": "SKU6095", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6095@example.com", "threshold": 950}},
    {"id": "PAYMENTS-6096", "title": "Payments scenario 6096", "data": {"sku": "SKU6096", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6096@example.com", "threshold": 960}},
    {"id": "PAYMENTS-6097", "title": "Payments scenario 6097", "data": {"sku": "SKU6097", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6097@example.com", "threshold": 970}},
    {"id": "PAYMENTS-6098", "title": "Payments scenario 6098", "data": {"sku": "SKU6098", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6098@example.com", "threshold": 980}},
    {"id": "PAYMENTS-6099", "title": "Payments scenario 6099", "data": {"sku": "SKU6099", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6099@example.com", "threshold": 990}},
    {"id": "PAYMENTS-6100", "title": "Payments scenario 6100", "data": {"sku": "SKU6100", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6100@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
