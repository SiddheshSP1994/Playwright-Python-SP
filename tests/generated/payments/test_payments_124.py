import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-7411", "title": "Payments scenario 7411", "data": {"sku": "SKU7411", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7411@example.com", "threshold": 110}},
    {"id": "PAYMENTS-7412", "title": "Payments scenario 7412", "data": {"sku": "SKU7412", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7412@example.com", "threshold": 120}},
    {"id": "PAYMENTS-7413", "title": "Payments scenario 7413", "data": {"sku": "SKU7413", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7413@example.com", "threshold": 130}},
    {"id": "PAYMENTS-7414", "title": "Payments scenario 7414", "data": {"sku": "SKU7414", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7414@example.com", "threshold": 140}},
    {"id": "PAYMENTS-7415", "title": "Payments scenario 7415", "data": {"sku": "SKU7415", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7415@example.com", "threshold": 150}},
    {"id": "PAYMENTS-7416", "title": "Payments scenario 7416", "data": {"sku": "SKU7416", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7416@example.com", "threshold": 160}},
    {"id": "PAYMENTS-7417", "title": "Payments scenario 7417", "data": {"sku": "SKU7417", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7417@example.com", "threshold": 170}},
    {"id": "PAYMENTS-7418", "title": "Payments scenario 7418", "data": {"sku": "SKU7418", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7418@example.com", "threshold": 180}},
    {"id": "PAYMENTS-7419", "title": "Payments scenario 7419", "data": {"sku": "SKU7419", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7419@example.com", "threshold": 190}},
    {"id": "PAYMENTS-7420", "title": "Payments scenario 7420", "data": {"sku": "SKU7420", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7420@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
