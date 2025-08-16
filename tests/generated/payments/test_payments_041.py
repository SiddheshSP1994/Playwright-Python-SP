import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2431", "title": "Payments scenario 2431", "data": {"sku": "SKU2431", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2431@example.com", "threshold": 310}},
    {"id": "PAYMENTS-2432", "title": "Payments scenario 2432", "data": {"sku": "SKU2432", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2432@example.com", "threshold": 320}},
    {"id": "PAYMENTS-2433", "title": "Payments scenario 2433", "data": {"sku": "SKU2433", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2433@example.com", "threshold": 330}},
    {"id": "PAYMENTS-2434", "title": "Payments scenario 2434", "data": {"sku": "SKU2434", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2434@example.com", "threshold": 340}},
    {"id": "PAYMENTS-2435", "title": "Payments scenario 2435", "data": {"sku": "SKU2435", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2435@example.com", "threshold": 350}},
    {"id": "PAYMENTS-2436", "title": "Payments scenario 2436", "data": {"sku": "SKU2436", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2436@example.com", "threshold": 360}},
    {"id": "PAYMENTS-2437", "title": "Payments scenario 2437", "data": {"sku": "SKU2437", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2437@example.com", "threshold": 370}},
    {"id": "PAYMENTS-2438", "title": "Payments scenario 2438", "data": {"sku": "SKU2438", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2438@example.com", "threshold": 380}},
    {"id": "PAYMENTS-2439", "title": "Payments scenario 2439", "data": {"sku": "SKU2439", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2439@example.com", "threshold": 390}},
    {"id": "PAYMENTS-2440", "title": "Payments scenario 2440", "data": {"sku": "SKU2440", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2440@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
