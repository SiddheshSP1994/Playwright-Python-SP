import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3101", "title": "Email scenario 3101", "data": {"sku": "SKU3101", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3101@example.com", "threshold": 10}},
    {"id": "EMAIL-3102", "title": "Email scenario 3102", "data": {"sku": "SKU3102", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3102@example.com", "threshold": 20}},
    {"id": "EMAIL-3103", "title": "Email scenario 3103", "data": {"sku": "SKU3103", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3103@example.com", "threshold": 30}},
    {"id": "EMAIL-3104", "title": "Email scenario 3104", "data": {"sku": "SKU3104", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3104@example.com", "threshold": 40}},
    {"id": "EMAIL-3105", "title": "Email scenario 3105", "data": {"sku": "SKU3105", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3105@example.com", "threshold": 50}},
    {"id": "EMAIL-3106", "title": "Email scenario 3106", "data": {"sku": "SKU3106", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3106@example.com", "threshold": 60}},
    {"id": "EMAIL-3107", "title": "Email scenario 3107", "data": {"sku": "SKU3107", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3107@example.com", "threshold": 70}},
    {"id": "EMAIL-3108", "title": "Email scenario 3108", "data": {"sku": "SKU3108", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3108@example.com", "threshold": 80}},
    {"id": "EMAIL-3109", "title": "Email scenario 3109", "data": {"sku": "SKU3109", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3109@example.com", "threshold": 90}},
    {"id": "EMAIL-3110", "title": "Email scenario 3110", "data": {"sku": "SKU3110", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3110@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
