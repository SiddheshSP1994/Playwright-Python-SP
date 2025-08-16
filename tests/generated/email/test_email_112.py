import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6701", "title": "Email scenario 6701", "data": {"sku": "SKU6701", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6701@example.com", "threshold": 10}},
    {"id": "EMAIL-6702", "title": "Email scenario 6702", "data": {"sku": "SKU6702", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6702@example.com", "threshold": 20}},
    {"id": "EMAIL-6703", "title": "Email scenario 6703", "data": {"sku": "SKU6703", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6703@example.com", "threshold": 30}},
    {"id": "EMAIL-6704", "title": "Email scenario 6704", "data": {"sku": "SKU6704", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6704@example.com", "threshold": 40}},
    {"id": "EMAIL-6705", "title": "Email scenario 6705", "data": {"sku": "SKU6705", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6705@example.com", "threshold": 50}},
    {"id": "EMAIL-6706", "title": "Email scenario 6706", "data": {"sku": "SKU6706", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6706@example.com", "threshold": 60}},
    {"id": "EMAIL-6707", "title": "Email scenario 6707", "data": {"sku": "SKU6707", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6707@example.com", "threshold": 70}},
    {"id": "EMAIL-6708", "title": "Email scenario 6708", "data": {"sku": "SKU6708", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6708@example.com", "threshold": 80}},
    {"id": "EMAIL-6709", "title": "Email scenario 6709", "data": {"sku": "SKU6709", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6709@example.com", "threshold": 90}},
    {"id": "EMAIL-6710", "title": "Email scenario 6710", "data": {"sku": "SKU6710", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6710@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
