import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2501", "title": "Email scenario 2501", "data": {"sku": "SKU2501", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2501@example.com", "threshold": 10}},
    {"id": "EMAIL-2502", "title": "Email scenario 2502", "data": {"sku": "SKU2502", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2502@example.com", "threshold": 20}},
    {"id": "EMAIL-2503", "title": "Email scenario 2503", "data": {"sku": "SKU2503", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2503@example.com", "threshold": 30}},
    {"id": "EMAIL-2504", "title": "Email scenario 2504", "data": {"sku": "SKU2504", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2504@example.com", "threshold": 40}},
    {"id": "EMAIL-2505", "title": "Email scenario 2505", "data": {"sku": "SKU2505", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2505@example.com", "threshold": 50}},
    {"id": "EMAIL-2506", "title": "Email scenario 2506", "data": {"sku": "SKU2506", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2506@example.com", "threshold": 60}},
    {"id": "EMAIL-2507", "title": "Email scenario 2507", "data": {"sku": "SKU2507", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2507@example.com", "threshold": 70}},
    {"id": "EMAIL-2508", "title": "Email scenario 2508", "data": {"sku": "SKU2508", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2508@example.com", "threshold": 80}},
    {"id": "EMAIL-2509", "title": "Email scenario 2509", "data": {"sku": "SKU2509", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2509@example.com", "threshold": 90}},
    {"id": "EMAIL-2510", "title": "Email scenario 2510", "data": {"sku": "SKU2510", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2510@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
