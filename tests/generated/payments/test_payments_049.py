import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2911", "title": "Payments scenario 2911", "data": {"sku": "SKU2911", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2911@example.com", "threshold": 110}},
    {"id": "PAYMENTS-2912", "title": "Payments scenario 2912", "data": {"sku": "SKU2912", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2912@example.com", "threshold": 120}},
    {"id": "PAYMENTS-2913", "title": "Payments scenario 2913", "data": {"sku": "SKU2913", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2913@example.com", "threshold": 130}},
    {"id": "PAYMENTS-2914", "title": "Payments scenario 2914", "data": {"sku": "SKU2914", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2914@example.com", "threshold": 140}},
    {"id": "PAYMENTS-2915", "title": "Payments scenario 2915", "data": {"sku": "SKU2915", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2915@example.com", "threshold": 150}},
    {"id": "PAYMENTS-2916", "title": "Payments scenario 2916", "data": {"sku": "SKU2916", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2916@example.com", "threshold": 160}},
    {"id": "PAYMENTS-2917", "title": "Payments scenario 2917", "data": {"sku": "SKU2917", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2917@example.com", "threshold": 170}},
    {"id": "PAYMENTS-2918", "title": "Payments scenario 2918", "data": {"sku": "SKU2918", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2918@example.com", "threshold": 180}},
    {"id": "PAYMENTS-2919", "title": "Payments scenario 2919", "data": {"sku": "SKU2919", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2919@example.com", "threshold": 190}},
    {"id": "PAYMENTS-2920", "title": "Payments scenario 2920", "data": {"sku": "SKU2920", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2920@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
