import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3701", "title": "Email scenario 3701", "data": {"sku": "SKU3701", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3701@example.com", "threshold": 10}},
    {"id": "EMAIL-3702", "title": "Email scenario 3702", "data": {"sku": "SKU3702", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3702@example.com", "threshold": 20}},
    {"id": "EMAIL-3703", "title": "Email scenario 3703", "data": {"sku": "SKU3703", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3703@example.com", "threshold": 30}},
    {"id": "EMAIL-3704", "title": "Email scenario 3704", "data": {"sku": "SKU3704", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3704@example.com", "threshold": 40}},
    {"id": "EMAIL-3705", "title": "Email scenario 3705", "data": {"sku": "SKU3705", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3705@example.com", "threshold": 50}},
    {"id": "EMAIL-3706", "title": "Email scenario 3706", "data": {"sku": "SKU3706", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3706@example.com", "threshold": 60}},
    {"id": "EMAIL-3707", "title": "Email scenario 3707", "data": {"sku": "SKU3707", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3707@example.com", "threshold": 70}},
    {"id": "EMAIL-3708", "title": "Email scenario 3708", "data": {"sku": "SKU3708", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3708@example.com", "threshold": 80}},
    {"id": "EMAIL-3709", "title": "Email scenario 3709", "data": {"sku": "SKU3709", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3709@example.com", "threshold": 90}},
    {"id": "EMAIL-3710", "title": "Email scenario 3710", "data": {"sku": "SKU3710", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3710@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
