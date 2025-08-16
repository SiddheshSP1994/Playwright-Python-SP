import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8431", "title": "Payments scenario 8431", "data": {"sku": "SKU8431", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8431@example.com", "threshold": 310}},
    {"id": "PAYMENTS-8432", "title": "Payments scenario 8432", "data": {"sku": "SKU8432", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8432@example.com", "threshold": 320}},
    {"id": "PAYMENTS-8433", "title": "Payments scenario 8433", "data": {"sku": "SKU8433", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8433@example.com", "threshold": 330}},
    {"id": "PAYMENTS-8434", "title": "Payments scenario 8434", "data": {"sku": "SKU8434", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8434@example.com", "threshold": 340}},
    {"id": "PAYMENTS-8435", "title": "Payments scenario 8435", "data": {"sku": "SKU8435", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8435@example.com", "threshold": 350}},
    {"id": "PAYMENTS-8436", "title": "Payments scenario 8436", "data": {"sku": "SKU8436", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8436@example.com", "threshold": 360}},
    {"id": "PAYMENTS-8437", "title": "Payments scenario 8437", "data": {"sku": "SKU8437", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8437@example.com", "threshold": 370}},
    {"id": "PAYMENTS-8438", "title": "Payments scenario 8438", "data": {"sku": "SKU8438", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8438@example.com", "threshold": 380}},
    {"id": "PAYMENTS-8439", "title": "Payments scenario 8439", "data": {"sku": "SKU8439", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8439@example.com", "threshold": 390}},
    {"id": "PAYMENTS-8440", "title": "Payments scenario 8440", "data": {"sku": "SKU8440", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8440@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
