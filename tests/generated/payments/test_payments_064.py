import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3811", "title": "Payments scenario 3811", "data": {"sku": "SKU3811", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3811@example.com", "threshold": 110}},
    {"id": "PAYMENTS-3812", "title": "Payments scenario 3812", "data": {"sku": "SKU3812", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3812@example.com", "threshold": 120}},
    {"id": "PAYMENTS-3813", "title": "Payments scenario 3813", "data": {"sku": "SKU3813", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3813@example.com", "threshold": 130}},
    {"id": "PAYMENTS-3814", "title": "Payments scenario 3814", "data": {"sku": "SKU3814", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3814@example.com", "threshold": 140}},
    {"id": "PAYMENTS-3815", "title": "Payments scenario 3815", "data": {"sku": "SKU3815", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3815@example.com", "threshold": 150}},
    {"id": "PAYMENTS-3816", "title": "Payments scenario 3816", "data": {"sku": "SKU3816", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3816@example.com", "threshold": 160}},
    {"id": "PAYMENTS-3817", "title": "Payments scenario 3817", "data": {"sku": "SKU3817", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3817@example.com", "threshold": 170}},
    {"id": "PAYMENTS-3818", "title": "Payments scenario 3818", "data": {"sku": "SKU3818", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3818@example.com", "threshold": 180}},
    {"id": "PAYMENTS-3819", "title": "Payments scenario 3819", "data": {"sku": "SKU3819", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3819@example.com", "threshold": 190}},
    {"id": "PAYMENTS-3820", "title": "Payments scenario 3820", "data": {"sku": "SKU3820", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3820@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
