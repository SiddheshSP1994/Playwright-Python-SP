import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6631", "title": "Payments scenario 6631", "data": {"sku": "SKU6631", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6631@example.com", "threshold": 310}},
    {"id": "PAYMENTS-6632", "title": "Payments scenario 6632", "data": {"sku": "SKU6632", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6632@example.com", "threshold": 320}},
    {"id": "PAYMENTS-6633", "title": "Payments scenario 6633", "data": {"sku": "SKU6633", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6633@example.com", "threshold": 330}},
    {"id": "PAYMENTS-6634", "title": "Payments scenario 6634", "data": {"sku": "SKU6634", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6634@example.com", "threshold": 340}},
    {"id": "PAYMENTS-6635", "title": "Payments scenario 6635", "data": {"sku": "SKU6635", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6635@example.com", "threshold": 350}},
    {"id": "PAYMENTS-6636", "title": "Payments scenario 6636", "data": {"sku": "SKU6636", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6636@example.com", "threshold": 360}},
    {"id": "PAYMENTS-6637", "title": "Payments scenario 6637", "data": {"sku": "SKU6637", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6637@example.com", "threshold": 370}},
    {"id": "PAYMENTS-6638", "title": "Payments scenario 6638", "data": {"sku": "SKU6638", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6638@example.com", "threshold": 380}},
    {"id": "PAYMENTS-6639", "title": "Payments scenario 6639", "data": {"sku": "SKU6639", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6639@example.com", "threshold": 390}},
    {"id": "PAYMENTS-6640", "title": "Payments scenario 6640", "data": {"sku": "SKU6640", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6640@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
