import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0451", "title": "Payments scenario 451", "data": {"sku": "SKU451", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user451@example.com", "threshold": 510}},
    {"id": "PAYMENTS-0452", "title": "Payments scenario 452", "data": {"sku": "SKU452", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user452@example.com", "threshold": 520}},
    {"id": "PAYMENTS-0453", "title": "Payments scenario 453", "data": {"sku": "SKU453", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user453@example.com", "threshold": 530}},
    {"id": "PAYMENTS-0454", "title": "Payments scenario 454", "data": {"sku": "SKU454", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user454@example.com", "threshold": 540}},
    {"id": "PAYMENTS-0455", "title": "Payments scenario 455", "data": {"sku": "SKU455", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user455@example.com", "threshold": 550}},
    {"id": "PAYMENTS-0456", "title": "Payments scenario 456", "data": {"sku": "SKU456", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user456@example.com", "threshold": 560}},
    {"id": "PAYMENTS-0457", "title": "Payments scenario 457", "data": {"sku": "SKU457", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user457@example.com", "threshold": 570}},
    {"id": "PAYMENTS-0458", "title": "Payments scenario 458", "data": {"sku": "SKU458", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user458@example.com", "threshold": 580}},
    {"id": "PAYMENTS-0459", "title": "Payments scenario 459", "data": {"sku": "SKU459", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user459@example.com", "threshold": 590}},
    {"id": "PAYMENTS-0460", "title": "Payments scenario 460", "data": {"sku": "SKU460", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user460@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
