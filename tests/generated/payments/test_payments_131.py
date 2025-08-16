import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-7831", "title": "Payments scenario 7831", "data": {"sku": "SKU7831", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7831@example.com", "threshold": 310}},
    {"id": "PAYMENTS-7832", "title": "Payments scenario 7832", "data": {"sku": "SKU7832", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7832@example.com", "threshold": 320}},
    {"id": "PAYMENTS-7833", "title": "Payments scenario 7833", "data": {"sku": "SKU7833", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7833@example.com", "threshold": 330}},
    {"id": "PAYMENTS-7834", "title": "Payments scenario 7834", "data": {"sku": "SKU7834", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7834@example.com", "threshold": 340}},
    {"id": "PAYMENTS-7835", "title": "Payments scenario 7835", "data": {"sku": "SKU7835", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7835@example.com", "threshold": 350}},
    {"id": "PAYMENTS-7836", "title": "Payments scenario 7836", "data": {"sku": "SKU7836", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7836@example.com", "threshold": 360}},
    {"id": "PAYMENTS-7837", "title": "Payments scenario 7837", "data": {"sku": "SKU7837", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7837@example.com", "threshold": 370}},
    {"id": "PAYMENTS-7838", "title": "Payments scenario 7838", "data": {"sku": "SKU7838", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7838@example.com", "threshold": 380}},
    {"id": "PAYMENTS-7839", "title": "Payments scenario 7839", "data": {"sku": "SKU7839", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7839@example.com", "threshold": 390}},
    {"id": "PAYMENTS-7840", "title": "Payments scenario 7840", "data": {"sku": "SKU7840", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7840@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
