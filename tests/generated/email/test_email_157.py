import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9401", "title": "Email scenario 9401", "data": {"sku": "SKU9401", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9401@example.com", "threshold": 10}},
    {"id": "EMAIL-9402", "title": "Email scenario 9402", "data": {"sku": "SKU9402", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9402@example.com", "threshold": 20}},
    {"id": "EMAIL-9403", "title": "Email scenario 9403", "data": {"sku": "SKU9403", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9403@example.com", "threshold": 30}},
    {"id": "EMAIL-9404", "title": "Email scenario 9404", "data": {"sku": "SKU9404", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9404@example.com", "threshold": 40}},
    {"id": "EMAIL-9405", "title": "Email scenario 9405", "data": {"sku": "SKU9405", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9405@example.com", "threshold": 50}},
    {"id": "EMAIL-9406", "title": "Email scenario 9406", "data": {"sku": "SKU9406", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9406@example.com", "threshold": 60}},
    {"id": "EMAIL-9407", "title": "Email scenario 9407", "data": {"sku": "SKU9407", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9407@example.com", "threshold": 70}},
    {"id": "EMAIL-9408", "title": "Email scenario 9408", "data": {"sku": "SKU9408", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9408@example.com", "threshold": 80}},
    {"id": "EMAIL-9409", "title": "Email scenario 9409", "data": {"sku": "SKU9409", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9409@example.com", "threshold": 90}},
    {"id": "EMAIL-9410", "title": "Email scenario 9410", "data": {"sku": "SKU9410", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9410@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
