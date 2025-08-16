import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4111", "title": "Payments scenario 4111", "data": {"sku": "SKU4111", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4111@example.com", "threshold": 110}},
    {"id": "PAYMENTS-4112", "title": "Payments scenario 4112", "data": {"sku": "SKU4112", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4112@example.com", "threshold": 120}},
    {"id": "PAYMENTS-4113", "title": "Payments scenario 4113", "data": {"sku": "SKU4113", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4113@example.com", "threshold": 130}},
    {"id": "PAYMENTS-4114", "title": "Payments scenario 4114", "data": {"sku": "SKU4114", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4114@example.com", "threshold": 140}},
    {"id": "PAYMENTS-4115", "title": "Payments scenario 4115", "data": {"sku": "SKU4115", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4115@example.com", "threshold": 150}},
    {"id": "PAYMENTS-4116", "title": "Payments scenario 4116", "data": {"sku": "SKU4116", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4116@example.com", "threshold": 160}},
    {"id": "PAYMENTS-4117", "title": "Payments scenario 4117", "data": {"sku": "SKU4117", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4117@example.com", "threshold": 170}},
    {"id": "PAYMENTS-4118", "title": "Payments scenario 4118", "data": {"sku": "SKU4118", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4118@example.com", "threshold": 180}},
    {"id": "PAYMENTS-4119", "title": "Payments scenario 4119", "data": {"sku": "SKU4119", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4119@example.com", "threshold": 190}},
    {"id": "PAYMENTS-4120", "title": "Payments scenario 4120", "data": {"sku": "SKU4120", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4120@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
