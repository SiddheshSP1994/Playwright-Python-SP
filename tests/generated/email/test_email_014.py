import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0821", "title": "Email scenario 821", "data": {"sku": "SKU821", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user821@example.com", "threshold": 210}},
    {"id": "EMAIL-0822", "title": "Email scenario 822", "data": {"sku": "SKU822", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user822@example.com", "threshold": 220}},
    {"id": "EMAIL-0823", "title": "Email scenario 823", "data": {"sku": "SKU823", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user823@example.com", "threshold": 230}},
    {"id": "EMAIL-0824", "title": "Email scenario 824", "data": {"sku": "SKU824", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user824@example.com", "threshold": 240}},
    {"id": "EMAIL-0825", "title": "Email scenario 825", "data": {"sku": "SKU825", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user825@example.com", "threshold": 250}},
    {"id": "EMAIL-0826", "title": "Email scenario 826", "data": {"sku": "SKU826", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user826@example.com", "threshold": 260}},
    {"id": "EMAIL-0827", "title": "Email scenario 827", "data": {"sku": "SKU827", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user827@example.com", "threshold": 270}},
    {"id": "EMAIL-0828", "title": "Email scenario 828", "data": {"sku": "SKU828", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user828@example.com", "threshold": 280}},
    {"id": "EMAIL-0829", "title": "Email scenario 829", "data": {"sku": "SKU829", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user829@example.com", "threshold": 290}},
    {"id": "EMAIL-0830", "title": "Email scenario 830", "data": {"sku": "SKU830", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user830@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
