import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2671", "title": "Payments scenario 2671", "data": {"sku": "SKU2671", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2671@example.com", "threshold": 710}},
    {"id": "PAYMENTS-2672", "title": "Payments scenario 2672", "data": {"sku": "SKU2672", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2672@example.com", "threshold": 720}},
    {"id": "PAYMENTS-2673", "title": "Payments scenario 2673", "data": {"sku": "SKU2673", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2673@example.com", "threshold": 730}},
    {"id": "PAYMENTS-2674", "title": "Payments scenario 2674", "data": {"sku": "SKU2674", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2674@example.com", "threshold": 740}},
    {"id": "PAYMENTS-2675", "title": "Payments scenario 2675", "data": {"sku": "SKU2675", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2675@example.com", "threshold": 750}},
    {"id": "PAYMENTS-2676", "title": "Payments scenario 2676", "data": {"sku": "SKU2676", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2676@example.com", "threshold": 760}},
    {"id": "PAYMENTS-2677", "title": "Payments scenario 2677", "data": {"sku": "SKU2677", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2677@example.com", "threshold": 770}},
    {"id": "PAYMENTS-2678", "title": "Payments scenario 2678", "data": {"sku": "SKU2678", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2678@example.com", "threshold": 780}},
    {"id": "PAYMENTS-2679", "title": "Payments scenario 2679", "data": {"sku": "SKU2679", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2679@example.com", "threshold": 790}},
    {"id": "PAYMENTS-2680", "title": "Payments scenario 2680", "data": {"sku": "SKU2680", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2680@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
