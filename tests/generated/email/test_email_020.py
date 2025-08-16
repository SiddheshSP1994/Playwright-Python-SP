import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1181", "title": "Email scenario 1181", "data": {"sku": "SKU1181", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1181@example.com", "threshold": 810}},
    {"id": "EMAIL-1182", "title": "Email scenario 1182", "data": {"sku": "SKU1182", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1182@example.com", "threshold": 820}},
    {"id": "EMAIL-1183", "title": "Email scenario 1183", "data": {"sku": "SKU1183", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1183@example.com", "threshold": 830}},
    {"id": "EMAIL-1184", "title": "Email scenario 1184", "data": {"sku": "SKU1184", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1184@example.com", "threshold": 840}},
    {"id": "EMAIL-1185", "title": "Email scenario 1185", "data": {"sku": "SKU1185", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1185@example.com", "threshold": 850}},
    {"id": "EMAIL-1186", "title": "Email scenario 1186", "data": {"sku": "SKU1186", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1186@example.com", "threshold": 860}},
    {"id": "EMAIL-1187", "title": "Email scenario 1187", "data": {"sku": "SKU1187", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1187@example.com", "threshold": 870}},
    {"id": "EMAIL-1188", "title": "Email scenario 1188", "data": {"sku": "SKU1188", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1188@example.com", "threshold": 880}},
    {"id": "EMAIL-1189", "title": "Email scenario 1189", "data": {"sku": "SKU1189", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1189@example.com", "threshold": 890}},
    {"id": "EMAIL-1190", "title": "Email scenario 1190", "data": {"sku": "SKU1190", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1190@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
