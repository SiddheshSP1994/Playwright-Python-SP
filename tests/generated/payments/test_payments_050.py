import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2971", "title": "Payments scenario 2971", "data": {"sku": "SKU2971", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2971@example.com", "threshold": 710}},
    {"id": "PAYMENTS-2972", "title": "Payments scenario 2972", "data": {"sku": "SKU2972", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2972@example.com", "threshold": 720}},
    {"id": "PAYMENTS-2973", "title": "Payments scenario 2973", "data": {"sku": "SKU2973", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2973@example.com", "threshold": 730}},
    {"id": "PAYMENTS-2974", "title": "Payments scenario 2974", "data": {"sku": "SKU2974", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2974@example.com", "threshold": 740}},
    {"id": "PAYMENTS-2975", "title": "Payments scenario 2975", "data": {"sku": "SKU2975", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2975@example.com", "threshold": 750}},
    {"id": "PAYMENTS-2976", "title": "Payments scenario 2976", "data": {"sku": "SKU2976", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2976@example.com", "threshold": 760}},
    {"id": "PAYMENTS-2977", "title": "Payments scenario 2977", "data": {"sku": "SKU2977", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2977@example.com", "threshold": 770}},
    {"id": "PAYMENTS-2978", "title": "Payments scenario 2978", "data": {"sku": "SKU2978", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2978@example.com", "threshold": 780}},
    {"id": "PAYMENTS-2979", "title": "Payments scenario 2979", "data": {"sku": "SKU2979", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2979@example.com", "threshold": 790}},
    {"id": "PAYMENTS-2980", "title": "Payments scenario 2980", "data": {"sku": "SKU2980", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2980@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
