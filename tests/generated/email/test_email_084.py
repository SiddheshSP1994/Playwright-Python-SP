import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5021", "title": "Email scenario 5021", "data": {"sku": "SKU5021", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5021@example.com", "threshold": 210}},
    {"id": "EMAIL-5022", "title": "Email scenario 5022", "data": {"sku": "SKU5022", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5022@example.com", "threshold": 220}},
    {"id": "EMAIL-5023", "title": "Email scenario 5023", "data": {"sku": "SKU5023", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5023@example.com", "threshold": 230}},
    {"id": "EMAIL-5024", "title": "Email scenario 5024", "data": {"sku": "SKU5024", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5024@example.com", "threshold": 240}},
    {"id": "EMAIL-5025", "title": "Email scenario 5025", "data": {"sku": "SKU5025", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5025@example.com", "threshold": 250}},
    {"id": "EMAIL-5026", "title": "Email scenario 5026", "data": {"sku": "SKU5026", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5026@example.com", "threshold": 260}},
    {"id": "EMAIL-5027", "title": "Email scenario 5027", "data": {"sku": "SKU5027", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5027@example.com", "threshold": 270}},
    {"id": "EMAIL-5028", "title": "Email scenario 5028", "data": {"sku": "SKU5028", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5028@example.com", "threshold": 280}},
    {"id": "EMAIL-5029", "title": "Email scenario 5029", "data": {"sku": "SKU5029", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5029@example.com", "threshold": 290}},
    {"id": "EMAIL-5030", "title": "Email scenario 5030", "data": {"sku": "SKU5030", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5030@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
