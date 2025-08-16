import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6451", "title": "Payments scenario 6451", "data": {"sku": "SKU6451", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6451@example.com", "threshold": 510}},
    {"id": "PAYMENTS-6452", "title": "Payments scenario 6452", "data": {"sku": "SKU6452", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6452@example.com", "threshold": 520}},
    {"id": "PAYMENTS-6453", "title": "Payments scenario 6453", "data": {"sku": "SKU6453", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6453@example.com", "threshold": 530}},
    {"id": "PAYMENTS-6454", "title": "Payments scenario 6454", "data": {"sku": "SKU6454", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6454@example.com", "threshold": 540}},
    {"id": "PAYMENTS-6455", "title": "Payments scenario 6455", "data": {"sku": "SKU6455", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6455@example.com", "threshold": 550}},
    {"id": "PAYMENTS-6456", "title": "Payments scenario 6456", "data": {"sku": "SKU6456", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6456@example.com", "threshold": 560}},
    {"id": "PAYMENTS-6457", "title": "Payments scenario 6457", "data": {"sku": "SKU6457", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6457@example.com", "threshold": 570}},
    {"id": "PAYMENTS-6458", "title": "Payments scenario 6458", "data": {"sku": "SKU6458", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6458@example.com", "threshold": 580}},
    {"id": "PAYMENTS-6459", "title": "Payments scenario 6459", "data": {"sku": "SKU6459", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6459@example.com", "threshold": 590}},
    {"id": "PAYMENTS-6460", "title": "Payments scenario 6460", "data": {"sku": "SKU6460", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6460@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
