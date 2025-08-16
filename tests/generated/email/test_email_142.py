import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8501", "title": "Email scenario 8501", "data": {"sku": "SKU8501", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8501@example.com", "threshold": 10}},
    {"id": "EMAIL-8502", "title": "Email scenario 8502", "data": {"sku": "SKU8502", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8502@example.com", "threshold": 20}},
    {"id": "EMAIL-8503", "title": "Email scenario 8503", "data": {"sku": "SKU8503", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8503@example.com", "threshold": 30}},
    {"id": "EMAIL-8504", "title": "Email scenario 8504", "data": {"sku": "SKU8504", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8504@example.com", "threshold": 40}},
    {"id": "EMAIL-8505", "title": "Email scenario 8505", "data": {"sku": "SKU8505", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8505@example.com", "threshold": 50}},
    {"id": "EMAIL-8506", "title": "Email scenario 8506", "data": {"sku": "SKU8506", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8506@example.com", "threshold": 60}},
    {"id": "EMAIL-8507", "title": "Email scenario 8507", "data": {"sku": "SKU8507", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8507@example.com", "threshold": 70}},
    {"id": "EMAIL-8508", "title": "Email scenario 8508", "data": {"sku": "SKU8508", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8508@example.com", "threshold": 80}},
    {"id": "EMAIL-8509", "title": "Email scenario 8509", "data": {"sku": "SKU8509", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8509@example.com", "threshold": 90}},
    {"id": "EMAIL-8510", "title": "Email scenario 8510", "data": {"sku": "SKU8510", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8510@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
