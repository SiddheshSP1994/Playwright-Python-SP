import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8131", "title": "Payments scenario 8131", "data": {"sku": "SKU8131", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8131@example.com", "threshold": 310}},
    {"id": "PAYMENTS-8132", "title": "Payments scenario 8132", "data": {"sku": "SKU8132", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8132@example.com", "threshold": 320}},
    {"id": "PAYMENTS-8133", "title": "Payments scenario 8133", "data": {"sku": "SKU8133", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8133@example.com", "threshold": 330}},
    {"id": "PAYMENTS-8134", "title": "Payments scenario 8134", "data": {"sku": "SKU8134", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8134@example.com", "threshold": 340}},
    {"id": "PAYMENTS-8135", "title": "Payments scenario 8135", "data": {"sku": "SKU8135", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8135@example.com", "threshold": 350}},
    {"id": "PAYMENTS-8136", "title": "Payments scenario 8136", "data": {"sku": "SKU8136", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8136@example.com", "threshold": 360}},
    {"id": "PAYMENTS-8137", "title": "Payments scenario 8137", "data": {"sku": "SKU8137", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8137@example.com", "threshold": 370}},
    {"id": "PAYMENTS-8138", "title": "Payments scenario 8138", "data": {"sku": "SKU8138", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8138@example.com", "threshold": 380}},
    {"id": "PAYMENTS-8139", "title": "Payments scenario 8139", "data": {"sku": "SKU8139", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8139@example.com", "threshold": 390}},
    {"id": "PAYMENTS-8140", "title": "Payments scenario 8140", "data": {"sku": "SKU8140", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8140@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
