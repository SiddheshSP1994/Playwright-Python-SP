import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3451", "title": "Payments scenario 3451", "data": {"sku": "SKU3451", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3451@example.com", "threshold": 510}},
    {"id": "PAYMENTS-3452", "title": "Payments scenario 3452", "data": {"sku": "SKU3452", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3452@example.com", "threshold": 520}},
    {"id": "PAYMENTS-3453", "title": "Payments scenario 3453", "data": {"sku": "SKU3453", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3453@example.com", "threshold": 530}},
    {"id": "PAYMENTS-3454", "title": "Payments scenario 3454", "data": {"sku": "SKU3454", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3454@example.com", "threshold": 540}},
    {"id": "PAYMENTS-3455", "title": "Payments scenario 3455", "data": {"sku": "SKU3455", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3455@example.com", "threshold": 550}},
    {"id": "PAYMENTS-3456", "title": "Payments scenario 3456", "data": {"sku": "SKU3456", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3456@example.com", "threshold": 560}},
    {"id": "PAYMENTS-3457", "title": "Payments scenario 3457", "data": {"sku": "SKU3457", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3457@example.com", "threshold": 570}},
    {"id": "PAYMENTS-3458", "title": "Payments scenario 3458", "data": {"sku": "SKU3458", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3458@example.com", "threshold": 580}},
    {"id": "PAYMENTS-3459", "title": "Payments scenario 3459", "data": {"sku": "SKU3459", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3459@example.com", "threshold": 590}},
    {"id": "PAYMENTS-3460", "title": "Payments scenario 3460", "data": {"sku": "SKU3460", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3460@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
