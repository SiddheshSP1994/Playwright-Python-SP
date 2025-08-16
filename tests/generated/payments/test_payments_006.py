import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0331", "title": "Payments scenario 331", "data": {"sku": "SKU331", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user331@example.com", "threshold": 310}},
    {"id": "PAYMENTS-0332", "title": "Payments scenario 332", "data": {"sku": "SKU332", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user332@example.com", "threshold": 320}},
    {"id": "PAYMENTS-0333", "title": "Payments scenario 333", "data": {"sku": "SKU333", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user333@example.com", "threshold": 330}},
    {"id": "PAYMENTS-0334", "title": "Payments scenario 334", "data": {"sku": "SKU334", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user334@example.com", "threshold": 340}},
    {"id": "PAYMENTS-0335", "title": "Payments scenario 335", "data": {"sku": "SKU335", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user335@example.com", "threshold": 350}},
    {"id": "PAYMENTS-0336", "title": "Payments scenario 336", "data": {"sku": "SKU336", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user336@example.com", "threshold": 360}},
    {"id": "PAYMENTS-0337", "title": "Payments scenario 337", "data": {"sku": "SKU337", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user337@example.com", "threshold": 370}},
    {"id": "PAYMENTS-0338", "title": "Payments scenario 338", "data": {"sku": "SKU338", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user338@example.com", "threshold": 380}},
    {"id": "PAYMENTS-0339", "title": "Payments scenario 339", "data": {"sku": "SKU339", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user339@example.com", "threshold": 390}},
    {"id": "PAYMENTS-0340", "title": "Payments scenario 340", "data": {"sku": "SKU340", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user340@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
