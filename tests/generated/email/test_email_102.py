import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6101", "title": "Email scenario 6101", "data": {"sku": "SKU6101", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6101@example.com", "threshold": 10}},
    {"id": "EMAIL-6102", "title": "Email scenario 6102", "data": {"sku": "SKU6102", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6102@example.com", "threshold": 20}},
    {"id": "EMAIL-6103", "title": "Email scenario 6103", "data": {"sku": "SKU6103", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6103@example.com", "threshold": 30}},
    {"id": "EMAIL-6104", "title": "Email scenario 6104", "data": {"sku": "SKU6104", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6104@example.com", "threshold": 40}},
    {"id": "EMAIL-6105", "title": "Email scenario 6105", "data": {"sku": "SKU6105", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6105@example.com", "threshold": 50}},
    {"id": "EMAIL-6106", "title": "Email scenario 6106", "data": {"sku": "SKU6106", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6106@example.com", "threshold": 60}},
    {"id": "EMAIL-6107", "title": "Email scenario 6107", "data": {"sku": "SKU6107", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6107@example.com", "threshold": 70}},
    {"id": "EMAIL-6108", "title": "Email scenario 6108", "data": {"sku": "SKU6108", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6108@example.com", "threshold": 80}},
    {"id": "EMAIL-6109", "title": "Email scenario 6109", "data": {"sku": "SKU6109", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6109@example.com", "threshold": 90}},
    {"id": "EMAIL-6110", "title": "Email scenario 6110", "data": {"sku": "SKU6110", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6110@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
