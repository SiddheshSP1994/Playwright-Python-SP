import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6511", "title": "Payments scenario 6511", "data": {"sku": "SKU6511", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6511@example.com", "threshold": 110}},
    {"id": "PAYMENTS-6512", "title": "Payments scenario 6512", "data": {"sku": "SKU6512", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6512@example.com", "threshold": 120}},
    {"id": "PAYMENTS-6513", "title": "Payments scenario 6513", "data": {"sku": "SKU6513", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6513@example.com", "threshold": 130}},
    {"id": "PAYMENTS-6514", "title": "Payments scenario 6514", "data": {"sku": "SKU6514", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6514@example.com", "threshold": 140}},
    {"id": "PAYMENTS-6515", "title": "Payments scenario 6515", "data": {"sku": "SKU6515", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6515@example.com", "threshold": 150}},
    {"id": "PAYMENTS-6516", "title": "Payments scenario 6516", "data": {"sku": "SKU6516", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6516@example.com", "threshold": 160}},
    {"id": "PAYMENTS-6517", "title": "Payments scenario 6517", "data": {"sku": "SKU6517", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6517@example.com", "threshold": 170}},
    {"id": "PAYMENTS-6518", "title": "Payments scenario 6518", "data": {"sku": "SKU6518", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6518@example.com", "threshold": 180}},
    {"id": "PAYMENTS-6519", "title": "Payments scenario 6519", "data": {"sku": "SKU6519", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6519@example.com", "threshold": 190}},
    {"id": "PAYMENTS-6520", "title": "Payments scenario 6520", "data": {"sku": "SKU6520", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6520@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
