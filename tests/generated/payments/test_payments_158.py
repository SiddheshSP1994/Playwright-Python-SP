import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-9451", "title": "Payments scenario 9451", "data": {"sku": "SKU9451", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9451@example.com", "threshold": 510}},
    {"id": "PAYMENTS-9452", "title": "Payments scenario 9452", "data": {"sku": "SKU9452", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9452@example.com", "threshold": 520}},
    {"id": "PAYMENTS-9453", "title": "Payments scenario 9453", "data": {"sku": "SKU9453", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9453@example.com", "threshold": 530}},
    {"id": "PAYMENTS-9454", "title": "Payments scenario 9454", "data": {"sku": "SKU9454", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9454@example.com", "threshold": 540}},
    {"id": "PAYMENTS-9455", "title": "Payments scenario 9455", "data": {"sku": "SKU9455", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9455@example.com", "threshold": 550}},
    {"id": "PAYMENTS-9456", "title": "Payments scenario 9456", "data": {"sku": "SKU9456", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9456@example.com", "threshold": 560}},
    {"id": "PAYMENTS-9457", "title": "Payments scenario 9457", "data": {"sku": "SKU9457", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9457@example.com", "threshold": 570}},
    {"id": "PAYMENTS-9458", "title": "Payments scenario 9458", "data": {"sku": "SKU9458", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9458@example.com", "threshold": 580}},
    {"id": "PAYMENTS-9459", "title": "Payments scenario 9459", "data": {"sku": "SKU9459", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9459@example.com", "threshold": 590}},
    {"id": "PAYMENTS-9460", "title": "Payments scenario 9460", "data": {"sku": "SKU9460", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9460@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
