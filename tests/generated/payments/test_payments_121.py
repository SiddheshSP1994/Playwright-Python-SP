import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-7231", "title": "Payments scenario 7231", "data": {"sku": "SKU7231", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7231@example.com", "threshold": 310}},
    {"id": "PAYMENTS-7232", "title": "Payments scenario 7232", "data": {"sku": "SKU7232", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7232@example.com", "threshold": 320}},
    {"id": "PAYMENTS-7233", "title": "Payments scenario 7233", "data": {"sku": "SKU7233", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7233@example.com", "threshold": 330}},
    {"id": "PAYMENTS-7234", "title": "Payments scenario 7234", "data": {"sku": "SKU7234", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7234@example.com", "threshold": 340}},
    {"id": "PAYMENTS-7235", "title": "Payments scenario 7235", "data": {"sku": "SKU7235", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7235@example.com", "threshold": 350}},
    {"id": "PAYMENTS-7236", "title": "Payments scenario 7236", "data": {"sku": "SKU7236", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7236@example.com", "threshold": 360}},
    {"id": "PAYMENTS-7237", "title": "Payments scenario 7237", "data": {"sku": "SKU7237", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7237@example.com", "threshold": 370}},
    {"id": "PAYMENTS-7238", "title": "Payments scenario 7238", "data": {"sku": "SKU7238", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7238@example.com", "threshold": 380}},
    {"id": "PAYMENTS-7239", "title": "Payments scenario 7239", "data": {"sku": "SKU7239", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7239@example.com", "threshold": 390}},
    {"id": "PAYMENTS-7240", "title": "Payments scenario 7240", "data": {"sku": "SKU7240", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7240@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
