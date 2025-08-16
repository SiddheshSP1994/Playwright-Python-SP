import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2381", "title": "Email scenario 2381", "data": {"sku": "SKU2381", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2381@example.com", "threshold": 810}},
    {"id": "EMAIL-2382", "title": "Email scenario 2382", "data": {"sku": "SKU2382", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2382@example.com", "threshold": 820}},
    {"id": "EMAIL-2383", "title": "Email scenario 2383", "data": {"sku": "SKU2383", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2383@example.com", "threshold": 830}},
    {"id": "EMAIL-2384", "title": "Email scenario 2384", "data": {"sku": "SKU2384", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2384@example.com", "threshold": 840}},
    {"id": "EMAIL-2385", "title": "Email scenario 2385", "data": {"sku": "SKU2385", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2385@example.com", "threshold": 850}},
    {"id": "EMAIL-2386", "title": "Email scenario 2386", "data": {"sku": "SKU2386", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2386@example.com", "threshold": 860}},
    {"id": "EMAIL-2387", "title": "Email scenario 2387", "data": {"sku": "SKU2387", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2387@example.com", "threshold": 870}},
    {"id": "EMAIL-2388", "title": "Email scenario 2388", "data": {"sku": "SKU2388", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2388@example.com", "threshold": 880}},
    {"id": "EMAIL-2389", "title": "Email scenario 2389", "data": {"sku": "SKU2389", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2389@example.com", "threshold": 890}},
    {"id": "EMAIL-2390", "title": "Email scenario 2390", "data": {"sku": "SKU2390", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2390@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
