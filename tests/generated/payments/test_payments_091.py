import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5431", "title": "Payments scenario 5431", "data": {"sku": "SKU5431", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5431@example.com", "threshold": 310}},
    {"id": "PAYMENTS-5432", "title": "Payments scenario 5432", "data": {"sku": "SKU5432", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5432@example.com", "threshold": 320}},
    {"id": "PAYMENTS-5433", "title": "Payments scenario 5433", "data": {"sku": "SKU5433", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5433@example.com", "threshold": 330}},
    {"id": "PAYMENTS-5434", "title": "Payments scenario 5434", "data": {"sku": "SKU5434", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5434@example.com", "threshold": 340}},
    {"id": "PAYMENTS-5435", "title": "Payments scenario 5435", "data": {"sku": "SKU5435", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5435@example.com", "threshold": 350}},
    {"id": "PAYMENTS-5436", "title": "Payments scenario 5436", "data": {"sku": "SKU5436", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5436@example.com", "threshold": 360}},
    {"id": "PAYMENTS-5437", "title": "Payments scenario 5437", "data": {"sku": "SKU5437", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5437@example.com", "threshold": 370}},
    {"id": "PAYMENTS-5438", "title": "Payments scenario 5438", "data": {"sku": "SKU5438", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5438@example.com", "threshold": 380}},
    {"id": "PAYMENTS-5439", "title": "Payments scenario 5439", "data": {"sku": "SKU5439", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5439@example.com", "threshold": 390}},
    {"id": "PAYMENTS-5440", "title": "Payments scenario 5440", "data": {"sku": "SKU5440", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5440@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
