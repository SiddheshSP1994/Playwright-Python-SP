import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6281", "title": "Email scenario 6281", "data": {"sku": "SKU6281", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6281@example.com", "threshold": 810}},
    {"id": "EMAIL-6282", "title": "Email scenario 6282", "data": {"sku": "SKU6282", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6282@example.com", "threshold": 820}},
    {"id": "EMAIL-6283", "title": "Email scenario 6283", "data": {"sku": "SKU6283", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6283@example.com", "threshold": 830}},
    {"id": "EMAIL-6284", "title": "Email scenario 6284", "data": {"sku": "SKU6284", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6284@example.com", "threshold": 840}},
    {"id": "EMAIL-6285", "title": "Email scenario 6285", "data": {"sku": "SKU6285", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6285@example.com", "threshold": 850}},
    {"id": "EMAIL-6286", "title": "Email scenario 6286", "data": {"sku": "SKU6286", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6286@example.com", "threshold": 860}},
    {"id": "EMAIL-6287", "title": "Email scenario 6287", "data": {"sku": "SKU6287", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6287@example.com", "threshold": 870}},
    {"id": "EMAIL-6288", "title": "Email scenario 6288", "data": {"sku": "SKU6288", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6288@example.com", "threshold": 880}},
    {"id": "EMAIL-6289", "title": "Email scenario 6289", "data": {"sku": "SKU6289", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6289@example.com", "threshold": 890}},
    {"id": "EMAIL-6290", "title": "Email scenario 6290", "data": {"sku": "SKU6290", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6290@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
