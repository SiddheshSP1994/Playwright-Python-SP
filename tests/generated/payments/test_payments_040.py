import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2371", "title": "Payments scenario 2371", "data": {"sku": "SKU2371", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2371@example.com", "threshold": 710}},
    {"id": "PAYMENTS-2372", "title": "Payments scenario 2372", "data": {"sku": "SKU2372", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2372@example.com", "threshold": 720}},
    {"id": "PAYMENTS-2373", "title": "Payments scenario 2373", "data": {"sku": "SKU2373", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2373@example.com", "threshold": 730}},
    {"id": "PAYMENTS-2374", "title": "Payments scenario 2374", "data": {"sku": "SKU2374", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2374@example.com", "threshold": 740}},
    {"id": "PAYMENTS-2375", "title": "Payments scenario 2375", "data": {"sku": "SKU2375", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2375@example.com", "threshold": 750}},
    {"id": "PAYMENTS-2376", "title": "Payments scenario 2376", "data": {"sku": "SKU2376", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2376@example.com", "threshold": 760}},
    {"id": "PAYMENTS-2377", "title": "Payments scenario 2377", "data": {"sku": "SKU2377", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2377@example.com", "threshold": 770}},
    {"id": "PAYMENTS-2378", "title": "Payments scenario 2378", "data": {"sku": "SKU2378", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2378@example.com", "threshold": 780}},
    {"id": "PAYMENTS-2379", "title": "Payments scenario 2379", "data": {"sku": "SKU2379", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2379@example.com", "threshold": 790}},
    {"id": "PAYMENTS-2380", "title": "Payments scenario 2380", "data": {"sku": "SKU2380", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2380@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
