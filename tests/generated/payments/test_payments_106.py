import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6331", "title": "Payments scenario 6331", "data": {"sku": "SKU6331", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6331@example.com", "threshold": 310}},
    {"id": "PAYMENTS-6332", "title": "Payments scenario 6332", "data": {"sku": "SKU6332", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6332@example.com", "threshold": 320}},
    {"id": "PAYMENTS-6333", "title": "Payments scenario 6333", "data": {"sku": "SKU6333", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6333@example.com", "threshold": 330}},
    {"id": "PAYMENTS-6334", "title": "Payments scenario 6334", "data": {"sku": "SKU6334", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6334@example.com", "threshold": 340}},
    {"id": "PAYMENTS-6335", "title": "Payments scenario 6335", "data": {"sku": "SKU6335", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6335@example.com", "threshold": 350}},
    {"id": "PAYMENTS-6336", "title": "Payments scenario 6336", "data": {"sku": "SKU6336", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6336@example.com", "threshold": 360}},
    {"id": "PAYMENTS-6337", "title": "Payments scenario 6337", "data": {"sku": "SKU6337", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6337@example.com", "threshold": 370}},
    {"id": "PAYMENTS-6338", "title": "Payments scenario 6338", "data": {"sku": "SKU6338", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6338@example.com", "threshold": 380}},
    {"id": "PAYMENTS-6339", "title": "Payments scenario 6339", "data": {"sku": "SKU6339", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6339@example.com", "threshold": 390}},
    {"id": "PAYMENTS-6340", "title": "Payments scenario 6340", "data": {"sku": "SKU6340", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6340@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
