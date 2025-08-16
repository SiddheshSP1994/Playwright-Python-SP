import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3271", "title": "Payments scenario 3271", "data": {"sku": "SKU3271", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3271@example.com", "threshold": 710}},
    {"id": "PAYMENTS-3272", "title": "Payments scenario 3272", "data": {"sku": "SKU3272", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3272@example.com", "threshold": 720}},
    {"id": "PAYMENTS-3273", "title": "Payments scenario 3273", "data": {"sku": "SKU3273", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3273@example.com", "threshold": 730}},
    {"id": "PAYMENTS-3274", "title": "Payments scenario 3274", "data": {"sku": "SKU3274", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3274@example.com", "threshold": 740}},
    {"id": "PAYMENTS-3275", "title": "Payments scenario 3275", "data": {"sku": "SKU3275", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3275@example.com", "threshold": 750}},
    {"id": "PAYMENTS-3276", "title": "Payments scenario 3276", "data": {"sku": "SKU3276", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3276@example.com", "threshold": 760}},
    {"id": "PAYMENTS-3277", "title": "Payments scenario 3277", "data": {"sku": "SKU3277", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3277@example.com", "threshold": 770}},
    {"id": "PAYMENTS-3278", "title": "Payments scenario 3278", "data": {"sku": "SKU3278", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3278@example.com", "threshold": 780}},
    {"id": "PAYMENTS-3279", "title": "Payments scenario 3279", "data": {"sku": "SKU3279", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3279@example.com", "threshold": 790}},
    {"id": "PAYMENTS-3280", "title": "Payments scenario 3280", "data": {"sku": "SKU3280", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3280@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
