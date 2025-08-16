import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4411", "title": "Payments scenario 4411", "data": {"sku": "SKU4411", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4411@example.com", "threshold": 110}},
    {"id": "PAYMENTS-4412", "title": "Payments scenario 4412", "data": {"sku": "SKU4412", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4412@example.com", "threshold": 120}},
    {"id": "PAYMENTS-4413", "title": "Payments scenario 4413", "data": {"sku": "SKU4413", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4413@example.com", "threshold": 130}},
    {"id": "PAYMENTS-4414", "title": "Payments scenario 4414", "data": {"sku": "SKU4414", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4414@example.com", "threshold": 140}},
    {"id": "PAYMENTS-4415", "title": "Payments scenario 4415", "data": {"sku": "SKU4415", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4415@example.com", "threshold": 150}},
    {"id": "PAYMENTS-4416", "title": "Payments scenario 4416", "data": {"sku": "SKU4416", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4416@example.com", "threshold": 160}},
    {"id": "PAYMENTS-4417", "title": "Payments scenario 4417", "data": {"sku": "SKU4417", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4417@example.com", "threshold": 170}},
    {"id": "PAYMENTS-4418", "title": "Payments scenario 4418", "data": {"sku": "SKU4418", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4418@example.com", "threshold": 180}},
    {"id": "PAYMENTS-4419", "title": "Payments scenario 4419", "data": {"sku": "SKU4419", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4419@example.com", "threshold": 190}},
    {"id": "PAYMENTS-4420", "title": "Payments scenario 4420", "data": {"sku": "SKU4420", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4420@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
