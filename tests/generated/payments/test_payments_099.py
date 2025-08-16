import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5911", "title": "Payments scenario 5911", "data": {"sku": "SKU5911", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5911@example.com", "threshold": 110}},
    {"id": "PAYMENTS-5912", "title": "Payments scenario 5912", "data": {"sku": "SKU5912", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5912@example.com", "threshold": 120}},
    {"id": "PAYMENTS-5913", "title": "Payments scenario 5913", "data": {"sku": "SKU5913", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5913@example.com", "threshold": 130}},
    {"id": "PAYMENTS-5914", "title": "Payments scenario 5914", "data": {"sku": "SKU5914", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5914@example.com", "threshold": 140}},
    {"id": "PAYMENTS-5915", "title": "Payments scenario 5915", "data": {"sku": "SKU5915", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5915@example.com", "threshold": 150}},
    {"id": "PAYMENTS-5916", "title": "Payments scenario 5916", "data": {"sku": "SKU5916", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5916@example.com", "threshold": 160}},
    {"id": "PAYMENTS-5917", "title": "Payments scenario 5917", "data": {"sku": "SKU5917", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5917@example.com", "threshold": 170}},
    {"id": "PAYMENTS-5918", "title": "Payments scenario 5918", "data": {"sku": "SKU5918", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5918@example.com", "threshold": 180}},
    {"id": "PAYMENTS-5919", "title": "Payments scenario 5919", "data": {"sku": "SKU5919", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5919@example.com", "threshold": 190}},
    {"id": "PAYMENTS-5920", "title": "Payments scenario 5920", "data": {"sku": "SKU5920", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5920@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
