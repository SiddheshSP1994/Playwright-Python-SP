import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2251", "title": "Payments scenario 2251", "data": {"sku": "SKU2251", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2251@example.com", "threshold": 510}},
    {"id": "PAYMENTS-2252", "title": "Payments scenario 2252", "data": {"sku": "SKU2252", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2252@example.com", "threshold": 520}},
    {"id": "PAYMENTS-2253", "title": "Payments scenario 2253", "data": {"sku": "SKU2253", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2253@example.com", "threshold": 530}},
    {"id": "PAYMENTS-2254", "title": "Payments scenario 2254", "data": {"sku": "SKU2254", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2254@example.com", "threshold": 540}},
    {"id": "PAYMENTS-2255", "title": "Payments scenario 2255", "data": {"sku": "SKU2255", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2255@example.com", "threshold": 550}},
    {"id": "PAYMENTS-2256", "title": "Payments scenario 2256", "data": {"sku": "SKU2256", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2256@example.com", "threshold": 560}},
    {"id": "PAYMENTS-2257", "title": "Payments scenario 2257", "data": {"sku": "SKU2257", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2257@example.com", "threshold": 570}},
    {"id": "PAYMENTS-2258", "title": "Payments scenario 2258", "data": {"sku": "SKU2258", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2258@example.com", "threshold": 580}},
    {"id": "PAYMENTS-2259", "title": "Payments scenario 2259", "data": {"sku": "SKU2259", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2259@example.com", "threshold": 590}},
    {"id": "PAYMENTS-2260", "title": "Payments scenario 2260", "data": {"sku": "SKU2260", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2260@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
