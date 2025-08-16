import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0811", "title": "Payments scenario 811", "data": {"sku": "SKU811", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user811@example.com", "threshold": 110}},
    {"id": "PAYMENTS-0812", "title": "Payments scenario 812", "data": {"sku": "SKU812", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user812@example.com", "threshold": 120}},
    {"id": "PAYMENTS-0813", "title": "Payments scenario 813", "data": {"sku": "SKU813", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user813@example.com", "threshold": 130}},
    {"id": "PAYMENTS-0814", "title": "Payments scenario 814", "data": {"sku": "SKU814", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user814@example.com", "threshold": 140}},
    {"id": "PAYMENTS-0815", "title": "Payments scenario 815", "data": {"sku": "SKU815", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user815@example.com", "threshold": 150}},
    {"id": "PAYMENTS-0816", "title": "Payments scenario 816", "data": {"sku": "SKU816", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user816@example.com", "threshold": 160}},
    {"id": "PAYMENTS-0817", "title": "Payments scenario 817", "data": {"sku": "SKU817", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user817@example.com", "threshold": 170}},
    {"id": "PAYMENTS-0818", "title": "Payments scenario 818", "data": {"sku": "SKU818", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user818@example.com", "threshold": 180}},
    {"id": "PAYMENTS-0819", "title": "Payments scenario 819", "data": {"sku": "SKU819", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user819@example.com", "threshold": 190}},
    {"id": "PAYMENTS-0820", "title": "Payments scenario 820", "data": {"sku": "SKU820", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user820@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
