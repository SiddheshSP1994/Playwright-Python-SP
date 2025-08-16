import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3091", "title": "Payments scenario 3091", "data": {"sku": "SKU3091", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3091@example.com", "threshold": 910}},
    {"id": "PAYMENTS-3092", "title": "Payments scenario 3092", "data": {"sku": "SKU3092", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3092@example.com", "threshold": 920}},
    {"id": "PAYMENTS-3093", "title": "Payments scenario 3093", "data": {"sku": "SKU3093", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3093@example.com", "threshold": 930}},
    {"id": "PAYMENTS-3094", "title": "Payments scenario 3094", "data": {"sku": "SKU3094", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3094@example.com", "threshold": 940}},
    {"id": "PAYMENTS-3095", "title": "Payments scenario 3095", "data": {"sku": "SKU3095", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3095@example.com", "threshold": 950}},
    {"id": "PAYMENTS-3096", "title": "Payments scenario 3096", "data": {"sku": "SKU3096", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3096@example.com", "threshold": 960}},
    {"id": "PAYMENTS-3097", "title": "Payments scenario 3097", "data": {"sku": "SKU3097", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3097@example.com", "threshold": 970}},
    {"id": "PAYMENTS-3098", "title": "Payments scenario 3098", "data": {"sku": "SKU3098", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3098@example.com", "threshold": 980}},
    {"id": "PAYMENTS-3099", "title": "Payments scenario 3099", "data": {"sku": "SKU3099", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3099@example.com", "threshold": 990}},
    {"id": "PAYMENTS-3100", "title": "Payments scenario 3100", "data": {"sku": "SKU3100", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3100@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
