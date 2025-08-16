import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4721", "title": "Email scenario 4721", "data": {"sku": "SKU4721", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4721@example.com", "threshold": 210}},
    {"id": "EMAIL-4722", "title": "Email scenario 4722", "data": {"sku": "SKU4722", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4722@example.com", "threshold": 220}},
    {"id": "EMAIL-4723", "title": "Email scenario 4723", "data": {"sku": "SKU4723", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4723@example.com", "threshold": 230}},
    {"id": "EMAIL-4724", "title": "Email scenario 4724", "data": {"sku": "SKU4724", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4724@example.com", "threshold": 240}},
    {"id": "EMAIL-4725", "title": "Email scenario 4725", "data": {"sku": "SKU4725", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4725@example.com", "threshold": 250}},
    {"id": "EMAIL-4726", "title": "Email scenario 4726", "data": {"sku": "SKU4726", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4726@example.com", "threshold": 260}},
    {"id": "EMAIL-4727", "title": "Email scenario 4727", "data": {"sku": "SKU4727", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4727@example.com", "threshold": 270}},
    {"id": "EMAIL-4728", "title": "Email scenario 4728", "data": {"sku": "SKU4728", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4728@example.com", "threshold": 280}},
    {"id": "EMAIL-4729", "title": "Email scenario 4729", "data": {"sku": "SKU4729", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4729@example.com", "threshold": 290}},
    {"id": "EMAIL-4730", "title": "Email scenario 4730", "data": {"sku": "SKU4730", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4730@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
