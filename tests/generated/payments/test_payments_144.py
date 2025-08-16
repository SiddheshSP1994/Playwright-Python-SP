import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8611", "title": "Payments scenario 8611", "data": {"sku": "SKU8611", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8611@example.com", "threshold": 110}},
    {"id": "PAYMENTS-8612", "title": "Payments scenario 8612", "data": {"sku": "SKU8612", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8612@example.com", "threshold": 120}},
    {"id": "PAYMENTS-8613", "title": "Payments scenario 8613", "data": {"sku": "SKU8613", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8613@example.com", "threshold": 130}},
    {"id": "PAYMENTS-8614", "title": "Payments scenario 8614", "data": {"sku": "SKU8614", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8614@example.com", "threshold": 140}},
    {"id": "PAYMENTS-8615", "title": "Payments scenario 8615", "data": {"sku": "SKU8615", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8615@example.com", "threshold": 150}},
    {"id": "PAYMENTS-8616", "title": "Payments scenario 8616", "data": {"sku": "SKU8616", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8616@example.com", "threshold": 160}},
    {"id": "PAYMENTS-8617", "title": "Payments scenario 8617", "data": {"sku": "SKU8617", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8617@example.com", "threshold": 170}},
    {"id": "PAYMENTS-8618", "title": "Payments scenario 8618", "data": {"sku": "SKU8618", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8618@example.com", "threshold": 180}},
    {"id": "PAYMENTS-8619", "title": "Payments scenario 8619", "data": {"sku": "SKU8619", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8619@example.com", "threshold": 190}},
    {"id": "PAYMENTS-8620", "title": "Payments scenario 8620", "data": {"sku": "SKU8620", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8620@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
