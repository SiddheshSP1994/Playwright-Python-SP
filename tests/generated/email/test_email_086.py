import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5141", "title": "Email scenario 5141", "data": {"sku": "SKU5141", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5141@example.com", "threshold": 410}},
    {"id": "EMAIL-5142", "title": "Email scenario 5142", "data": {"sku": "SKU5142", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5142@example.com", "threshold": 420}},
    {"id": "EMAIL-5143", "title": "Email scenario 5143", "data": {"sku": "SKU5143", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5143@example.com", "threshold": 430}},
    {"id": "EMAIL-5144", "title": "Email scenario 5144", "data": {"sku": "SKU5144", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5144@example.com", "threshold": 440}},
    {"id": "EMAIL-5145", "title": "Email scenario 5145", "data": {"sku": "SKU5145", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5145@example.com", "threshold": 450}},
    {"id": "EMAIL-5146", "title": "Email scenario 5146", "data": {"sku": "SKU5146", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5146@example.com", "threshold": 460}},
    {"id": "EMAIL-5147", "title": "Email scenario 5147", "data": {"sku": "SKU5147", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5147@example.com", "threshold": 470}},
    {"id": "EMAIL-5148", "title": "Email scenario 5148", "data": {"sku": "SKU5148", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5148@example.com", "threshold": 480}},
    {"id": "EMAIL-5149", "title": "Email scenario 5149", "data": {"sku": "SKU5149", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5149@example.com", "threshold": 490}},
    {"id": "EMAIL-5150", "title": "Email scenario 5150", "data": {"sku": "SKU5150", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5150@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
