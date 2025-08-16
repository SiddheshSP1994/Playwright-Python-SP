import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8911", "title": "Payments scenario 8911", "data": {"sku": "SKU8911", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8911@example.com", "threshold": 110}},
    {"id": "PAYMENTS-8912", "title": "Payments scenario 8912", "data": {"sku": "SKU8912", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8912@example.com", "threshold": 120}},
    {"id": "PAYMENTS-8913", "title": "Payments scenario 8913", "data": {"sku": "SKU8913", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8913@example.com", "threshold": 130}},
    {"id": "PAYMENTS-8914", "title": "Payments scenario 8914", "data": {"sku": "SKU8914", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8914@example.com", "threshold": 140}},
    {"id": "PAYMENTS-8915", "title": "Payments scenario 8915", "data": {"sku": "SKU8915", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8915@example.com", "threshold": 150}},
    {"id": "PAYMENTS-8916", "title": "Payments scenario 8916", "data": {"sku": "SKU8916", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8916@example.com", "threshold": 160}},
    {"id": "PAYMENTS-8917", "title": "Payments scenario 8917", "data": {"sku": "SKU8917", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8917@example.com", "threshold": 170}},
    {"id": "PAYMENTS-8918", "title": "Payments scenario 8918", "data": {"sku": "SKU8918", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8918@example.com", "threshold": 180}},
    {"id": "PAYMENTS-8919", "title": "Payments scenario 8919", "data": {"sku": "SKU8919", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8919@example.com", "threshold": 190}},
    {"id": "PAYMENTS-8920", "title": "Payments scenario 8920", "data": {"sku": "SKU8920", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8920@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
