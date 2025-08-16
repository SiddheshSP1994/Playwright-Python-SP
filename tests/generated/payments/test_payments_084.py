import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5011", "title": "Payments scenario 5011", "data": {"sku": "SKU5011", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5011@example.com", "threshold": 110}},
    {"id": "PAYMENTS-5012", "title": "Payments scenario 5012", "data": {"sku": "SKU5012", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5012@example.com", "threshold": 120}},
    {"id": "PAYMENTS-5013", "title": "Payments scenario 5013", "data": {"sku": "SKU5013", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5013@example.com", "threshold": 130}},
    {"id": "PAYMENTS-5014", "title": "Payments scenario 5014", "data": {"sku": "SKU5014", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5014@example.com", "threshold": 140}},
    {"id": "PAYMENTS-5015", "title": "Payments scenario 5015", "data": {"sku": "SKU5015", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5015@example.com", "threshold": 150}},
    {"id": "PAYMENTS-5016", "title": "Payments scenario 5016", "data": {"sku": "SKU5016", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5016@example.com", "threshold": 160}},
    {"id": "PAYMENTS-5017", "title": "Payments scenario 5017", "data": {"sku": "SKU5017", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5017@example.com", "threshold": 170}},
    {"id": "PAYMENTS-5018", "title": "Payments scenario 5018", "data": {"sku": "SKU5018", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5018@example.com", "threshold": 180}},
    {"id": "PAYMENTS-5019", "title": "Payments scenario 5019", "data": {"sku": "SKU5019", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5019@example.com", "threshold": 190}},
    {"id": "PAYMENTS-5020", "title": "Payments scenario 5020", "data": {"sku": "SKU5020", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5020@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
