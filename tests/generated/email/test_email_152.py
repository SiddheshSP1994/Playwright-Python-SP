import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9101", "title": "Email scenario 9101", "data": {"sku": "SKU9101", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9101@example.com", "threshold": 10}},
    {"id": "EMAIL-9102", "title": "Email scenario 9102", "data": {"sku": "SKU9102", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9102@example.com", "threshold": 20}},
    {"id": "EMAIL-9103", "title": "Email scenario 9103", "data": {"sku": "SKU9103", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9103@example.com", "threshold": 30}},
    {"id": "EMAIL-9104", "title": "Email scenario 9104", "data": {"sku": "SKU9104", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9104@example.com", "threshold": 40}},
    {"id": "EMAIL-9105", "title": "Email scenario 9105", "data": {"sku": "SKU9105", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9105@example.com", "threshold": 50}},
    {"id": "EMAIL-9106", "title": "Email scenario 9106", "data": {"sku": "SKU9106", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9106@example.com", "threshold": 60}},
    {"id": "EMAIL-9107", "title": "Email scenario 9107", "data": {"sku": "SKU9107", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9107@example.com", "threshold": 70}},
    {"id": "EMAIL-9108", "title": "Email scenario 9108", "data": {"sku": "SKU9108", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9108@example.com", "threshold": 80}},
    {"id": "EMAIL-9109", "title": "Email scenario 9109", "data": {"sku": "SKU9109", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9109@example.com", "threshold": 90}},
    {"id": "EMAIL-9110", "title": "Email scenario 9110", "data": {"sku": "SKU9110", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9110@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
