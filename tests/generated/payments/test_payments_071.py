import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4231", "title": "Payments scenario 4231", "data": {"sku": "SKU4231", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4231@example.com", "threshold": 310}},
    {"id": "PAYMENTS-4232", "title": "Payments scenario 4232", "data": {"sku": "SKU4232", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4232@example.com", "threshold": 320}},
    {"id": "PAYMENTS-4233", "title": "Payments scenario 4233", "data": {"sku": "SKU4233", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4233@example.com", "threshold": 330}},
    {"id": "PAYMENTS-4234", "title": "Payments scenario 4234", "data": {"sku": "SKU4234", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4234@example.com", "threshold": 340}},
    {"id": "PAYMENTS-4235", "title": "Payments scenario 4235", "data": {"sku": "SKU4235", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4235@example.com", "threshold": 350}},
    {"id": "PAYMENTS-4236", "title": "Payments scenario 4236", "data": {"sku": "SKU4236", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4236@example.com", "threshold": 360}},
    {"id": "PAYMENTS-4237", "title": "Payments scenario 4237", "data": {"sku": "SKU4237", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4237@example.com", "threshold": 370}},
    {"id": "PAYMENTS-4238", "title": "Payments scenario 4238", "data": {"sku": "SKU4238", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4238@example.com", "threshold": 380}},
    {"id": "PAYMENTS-4239", "title": "Payments scenario 4239", "data": {"sku": "SKU4239", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4239@example.com", "threshold": 390}},
    {"id": "PAYMENTS-4240", "title": "Payments scenario 4240", "data": {"sku": "SKU4240", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4240@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
