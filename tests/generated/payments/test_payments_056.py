import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3331", "title": "Payments scenario 3331", "data": {"sku": "SKU3331", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3331@example.com", "threshold": 310}},
    {"id": "PAYMENTS-3332", "title": "Payments scenario 3332", "data": {"sku": "SKU3332", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3332@example.com", "threshold": 320}},
    {"id": "PAYMENTS-3333", "title": "Payments scenario 3333", "data": {"sku": "SKU3333", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3333@example.com", "threshold": 330}},
    {"id": "PAYMENTS-3334", "title": "Payments scenario 3334", "data": {"sku": "SKU3334", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3334@example.com", "threshold": 340}},
    {"id": "PAYMENTS-3335", "title": "Payments scenario 3335", "data": {"sku": "SKU3335", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3335@example.com", "threshold": 350}},
    {"id": "PAYMENTS-3336", "title": "Payments scenario 3336", "data": {"sku": "SKU3336", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3336@example.com", "threshold": 360}},
    {"id": "PAYMENTS-3337", "title": "Payments scenario 3337", "data": {"sku": "SKU3337", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3337@example.com", "threshold": 370}},
    {"id": "PAYMENTS-3338", "title": "Payments scenario 3338", "data": {"sku": "SKU3338", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3338@example.com", "threshold": 380}},
    {"id": "PAYMENTS-3339", "title": "Payments scenario 3339", "data": {"sku": "SKU3339", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3339@example.com", "threshold": 390}},
    {"id": "PAYMENTS-3340", "title": "Payments scenario 3340", "data": {"sku": "SKU3340", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3340@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
