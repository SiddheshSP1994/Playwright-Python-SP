import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2441", "title": "Email scenario 2441", "data": {"sku": "SKU2441", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2441@example.com", "threshold": 410}},
    {"id": "EMAIL-2442", "title": "Email scenario 2442", "data": {"sku": "SKU2442", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2442@example.com", "threshold": 420}},
    {"id": "EMAIL-2443", "title": "Email scenario 2443", "data": {"sku": "SKU2443", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2443@example.com", "threshold": 430}},
    {"id": "EMAIL-2444", "title": "Email scenario 2444", "data": {"sku": "SKU2444", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2444@example.com", "threshold": 440}},
    {"id": "EMAIL-2445", "title": "Email scenario 2445", "data": {"sku": "SKU2445", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2445@example.com", "threshold": 450}},
    {"id": "EMAIL-2446", "title": "Email scenario 2446", "data": {"sku": "SKU2446", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2446@example.com", "threshold": 460}},
    {"id": "EMAIL-2447", "title": "Email scenario 2447", "data": {"sku": "SKU2447", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2447@example.com", "threshold": 470}},
    {"id": "EMAIL-2448", "title": "Email scenario 2448", "data": {"sku": "SKU2448", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2448@example.com", "threshold": 480}},
    {"id": "EMAIL-2449", "title": "Email scenario 2449", "data": {"sku": "SKU2449", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2449@example.com", "threshold": 490}},
    {"id": "EMAIL-2450", "title": "Email scenario 2450", "data": {"sku": "SKU2450", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2450@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
