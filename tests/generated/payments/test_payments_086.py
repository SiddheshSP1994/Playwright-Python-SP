import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5131", "title": "Payments scenario 5131", "data": {"sku": "SKU5131", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5131@example.com", "threshold": 310}},
    {"id": "PAYMENTS-5132", "title": "Payments scenario 5132", "data": {"sku": "SKU5132", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5132@example.com", "threshold": 320}},
    {"id": "PAYMENTS-5133", "title": "Payments scenario 5133", "data": {"sku": "SKU5133", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5133@example.com", "threshold": 330}},
    {"id": "PAYMENTS-5134", "title": "Payments scenario 5134", "data": {"sku": "SKU5134", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5134@example.com", "threshold": 340}},
    {"id": "PAYMENTS-5135", "title": "Payments scenario 5135", "data": {"sku": "SKU5135", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5135@example.com", "threshold": 350}},
    {"id": "PAYMENTS-5136", "title": "Payments scenario 5136", "data": {"sku": "SKU5136", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5136@example.com", "threshold": 360}},
    {"id": "PAYMENTS-5137", "title": "Payments scenario 5137", "data": {"sku": "SKU5137", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5137@example.com", "threshold": 370}},
    {"id": "PAYMENTS-5138", "title": "Payments scenario 5138", "data": {"sku": "SKU5138", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5138@example.com", "threshold": 380}},
    {"id": "PAYMENTS-5139", "title": "Payments scenario 5139", "data": {"sku": "SKU5139", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5139@example.com", "threshold": 390}},
    {"id": "PAYMENTS-5140", "title": "Payments scenario 5140", "data": {"sku": "SKU5140", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5140@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
