import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4181", "title": "Email scenario 4181", "data": {"sku": "SKU4181", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4181@example.com", "threshold": 810}},
    {"id": "EMAIL-4182", "title": "Email scenario 4182", "data": {"sku": "SKU4182", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4182@example.com", "threshold": 820}},
    {"id": "EMAIL-4183", "title": "Email scenario 4183", "data": {"sku": "SKU4183", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4183@example.com", "threshold": 830}},
    {"id": "EMAIL-4184", "title": "Email scenario 4184", "data": {"sku": "SKU4184", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4184@example.com", "threshold": 840}},
    {"id": "EMAIL-4185", "title": "Email scenario 4185", "data": {"sku": "SKU4185", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4185@example.com", "threshold": 850}},
    {"id": "EMAIL-4186", "title": "Email scenario 4186", "data": {"sku": "SKU4186", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4186@example.com", "threshold": 860}},
    {"id": "EMAIL-4187", "title": "Email scenario 4187", "data": {"sku": "SKU4187", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4187@example.com", "threshold": 870}},
    {"id": "EMAIL-4188", "title": "Email scenario 4188", "data": {"sku": "SKU4188", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4188@example.com", "threshold": 880}},
    {"id": "EMAIL-4189", "title": "Email scenario 4189", "data": {"sku": "SKU4189", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4189@example.com", "threshold": 890}},
    {"id": "EMAIL-4190", "title": "Email scenario 4190", "data": {"sku": "SKU4190", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4190@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
