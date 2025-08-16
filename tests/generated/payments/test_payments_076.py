import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4531", "title": "Payments scenario 4531", "data": {"sku": "SKU4531", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4531@example.com", "threshold": 310}},
    {"id": "PAYMENTS-4532", "title": "Payments scenario 4532", "data": {"sku": "SKU4532", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4532@example.com", "threshold": 320}},
    {"id": "PAYMENTS-4533", "title": "Payments scenario 4533", "data": {"sku": "SKU4533", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4533@example.com", "threshold": 330}},
    {"id": "PAYMENTS-4534", "title": "Payments scenario 4534", "data": {"sku": "SKU4534", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4534@example.com", "threshold": 340}},
    {"id": "PAYMENTS-4535", "title": "Payments scenario 4535", "data": {"sku": "SKU4535", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4535@example.com", "threshold": 350}},
    {"id": "PAYMENTS-4536", "title": "Payments scenario 4536", "data": {"sku": "SKU4536", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4536@example.com", "threshold": 360}},
    {"id": "PAYMENTS-4537", "title": "Payments scenario 4537", "data": {"sku": "SKU4537", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4537@example.com", "threshold": 370}},
    {"id": "PAYMENTS-4538", "title": "Payments scenario 4538", "data": {"sku": "SKU4538", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4538@example.com", "threshold": 380}},
    {"id": "PAYMENTS-4539", "title": "Payments scenario 4539", "data": {"sku": "SKU4539", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4539@example.com", "threshold": 390}},
    {"id": "PAYMENTS-4540", "title": "Payments scenario 4540", "data": {"sku": "SKU4540", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4540@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
