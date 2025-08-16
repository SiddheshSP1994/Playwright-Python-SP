import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6041", "title": "Email scenario 6041", "data": {"sku": "SKU6041", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6041@example.com", "threshold": 410}},
    {"id": "EMAIL-6042", "title": "Email scenario 6042", "data": {"sku": "SKU6042", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6042@example.com", "threshold": 420}},
    {"id": "EMAIL-6043", "title": "Email scenario 6043", "data": {"sku": "SKU6043", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6043@example.com", "threshold": 430}},
    {"id": "EMAIL-6044", "title": "Email scenario 6044", "data": {"sku": "SKU6044", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6044@example.com", "threshold": 440}},
    {"id": "EMAIL-6045", "title": "Email scenario 6045", "data": {"sku": "SKU6045", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6045@example.com", "threshold": 450}},
    {"id": "EMAIL-6046", "title": "Email scenario 6046", "data": {"sku": "SKU6046", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6046@example.com", "threshold": 460}},
    {"id": "EMAIL-6047", "title": "Email scenario 6047", "data": {"sku": "SKU6047", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6047@example.com", "threshold": 470}},
    {"id": "EMAIL-6048", "title": "Email scenario 6048", "data": {"sku": "SKU6048", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6048@example.com", "threshold": 480}},
    {"id": "EMAIL-6049", "title": "Email scenario 6049", "data": {"sku": "SKU6049", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6049@example.com", "threshold": 490}},
    {"id": "EMAIL-6050", "title": "Email scenario 6050", "data": {"sku": "SKU6050", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6050@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
