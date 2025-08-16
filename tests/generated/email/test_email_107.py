import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6401", "title": "Email scenario 6401", "data": {"sku": "SKU6401", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6401@example.com", "threshold": 10}},
    {"id": "EMAIL-6402", "title": "Email scenario 6402", "data": {"sku": "SKU6402", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6402@example.com", "threshold": 20}},
    {"id": "EMAIL-6403", "title": "Email scenario 6403", "data": {"sku": "SKU6403", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6403@example.com", "threshold": 30}},
    {"id": "EMAIL-6404", "title": "Email scenario 6404", "data": {"sku": "SKU6404", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6404@example.com", "threshold": 40}},
    {"id": "EMAIL-6405", "title": "Email scenario 6405", "data": {"sku": "SKU6405", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6405@example.com", "threshold": 50}},
    {"id": "EMAIL-6406", "title": "Email scenario 6406", "data": {"sku": "SKU6406", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6406@example.com", "threshold": 60}},
    {"id": "EMAIL-6407", "title": "Email scenario 6407", "data": {"sku": "SKU6407", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6407@example.com", "threshold": 70}},
    {"id": "EMAIL-6408", "title": "Email scenario 6408", "data": {"sku": "SKU6408", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6408@example.com", "threshold": 80}},
    {"id": "EMAIL-6409", "title": "Email scenario 6409", "data": {"sku": "SKU6409", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6409@example.com", "threshold": 90}},
    {"id": "EMAIL-6410", "title": "Email scenario 6410", "data": {"sku": "SKU6410", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6410@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
