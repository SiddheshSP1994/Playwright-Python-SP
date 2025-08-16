import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7181", "title": "Email scenario 7181", "data": {"sku": "SKU7181", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7181@example.com", "threshold": 810}},
    {"id": "EMAIL-7182", "title": "Email scenario 7182", "data": {"sku": "SKU7182", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7182@example.com", "threshold": 820}},
    {"id": "EMAIL-7183", "title": "Email scenario 7183", "data": {"sku": "SKU7183", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7183@example.com", "threshold": 830}},
    {"id": "EMAIL-7184", "title": "Email scenario 7184", "data": {"sku": "SKU7184", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7184@example.com", "threshold": 840}},
    {"id": "EMAIL-7185", "title": "Email scenario 7185", "data": {"sku": "SKU7185", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7185@example.com", "threshold": 850}},
    {"id": "EMAIL-7186", "title": "Email scenario 7186", "data": {"sku": "SKU7186", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7186@example.com", "threshold": 860}},
    {"id": "EMAIL-7187", "title": "Email scenario 7187", "data": {"sku": "SKU7187", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7187@example.com", "threshold": 870}},
    {"id": "EMAIL-7188", "title": "Email scenario 7188", "data": {"sku": "SKU7188", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7188@example.com", "threshold": 880}},
    {"id": "EMAIL-7189", "title": "Email scenario 7189", "data": {"sku": "SKU7189", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7189@example.com", "threshold": 890}},
    {"id": "EMAIL-7190", "title": "Email scenario 7190", "data": {"sku": "SKU7190", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7190@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
