import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0101", "title": "Email scenario 101", "data": {"sku": "SKU101", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user101@example.com", "threshold": 10}},
    {"id": "EMAIL-0102", "title": "Email scenario 102", "data": {"sku": "SKU102", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user102@example.com", "threshold": 20}},
    {"id": "EMAIL-0103", "title": "Email scenario 103", "data": {"sku": "SKU103", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user103@example.com", "threshold": 30}},
    {"id": "EMAIL-0104", "title": "Email scenario 104", "data": {"sku": "SKU104", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user104@example.com", "threshold": 40}},
    {"id": "EMAIL-0105", "title": "Email scenario 105", "data": {"sku": "SKU105", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user105@example.com", "threshold": 50}},
    {"id": "EMAIL-0106", "title": "Email scenario 106", "data": {"sku": "SKU106", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user106@example.com", "threshold": 60}},
    {"id": "EMAIL-0107", "title": "Email scenario 107", "data": {"sku": "SKU107", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user107@example.com", "threshold": 70}},
    {"id": "EMAIL-0108", "title": "Email scenario 108", "data": {"sku": "SKU108", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user108@example.com", "threshold": 80}},
    {"id": "EMAIL-0109", "title": "Email scenario 109", "data": {"sku": "SKU109", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user109@example.com", "threshold": 90}},
    {"id": "EMAIL-0110", "title": "Email scenario 110", "data": {"sku": "SKU110", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user110@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
