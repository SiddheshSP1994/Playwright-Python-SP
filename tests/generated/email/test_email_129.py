import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7721", "title": "Email scenario 7721", "data": {"sku": "SKU7721", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7721@example.com", "threshold": 210}},
    {"id": "EMAIL-7722", "title": "Email scenario 7722", "data": {"sku": "SKU7722", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7722@example.com", "threshold": 220}},
    {"id": "EMAIL-7723", "title": "Email scenario 7723", "data": {"sku": "SKU7723", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7723@example.com", "threshold": 230}},
    {"id": "EMAIL-7724", "title": "Email scenario 7724", "data": {"sku": "SKU7724", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7724@example.com", "threshold": 240}},
    {"id": "EMAIL-7725", "title": "Email scenario 7725", "data": {"sku": "SKU7725", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7725@example.com", "threshold": 250}},
    {"id": "EMAIL-7726", "title": "Email scenario 7726", "data": {"sku": "SKU7726", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7726@example.com", "threshold": 260}},
    {"id": "EMAIL-7727", "title": "Email scenario 7727", "data": {"sku": "SKU7727", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7727@example.com", "threshold": 270}},
    {"id": "EMAIL-7728", "title": "Email scenario 7728", "data": {"sku": "SKU7728", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7728@example.com", "threshold": 280}},
    {"id": "EMAIL-7729", "title": "Email scenario 7729", "data": {"sku": "SKU7729", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7729@example.com", "threshold": 290}},
    {"id": "EMAIL-7730", "title": "Email scenario 7730", "data": {"sku": "SKU7730", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7730@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
