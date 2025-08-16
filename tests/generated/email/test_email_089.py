import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5321", "title": "Email scenario 5321", "data": {"sku": "SKU5321", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5321@example.com", "threshold": 210}},
    {"id": "EMAIL-5322", "title": "Email scenario 5322", "data": {"sku": "SKU5322", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5322@example.com", "threshold": 220}},
    {"id": "EMAIL-5323", "title": "Email scenario 5323", "data": {"sku": "SKU5323", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5323@example.com", "threshold": 230}},
    {"id": "EMAIL-5324", "title": "Email scenario 5324", "data": {"sku": "SKU5324", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5324@example.com", "threshold": 240}},
    {"id": "EMAIL-5325", "title": "Email scenario 5325", "data": {"sku": "SKU5325", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5325@example.com", "threshold": 250}},
    {"id": "EMAIL-5326", "title": "Email scenario 5326", "data": {"sku": "SKU5326", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5326@example.com", "threshold": 260}},
    {"id": "EMAIL-5327", "title": "Email scenario 5327", "data": {"sku": "SKU5327", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5327@example.com", "threshold": 270}},
    {"id": "EMAIL-5328", "title": "Email scenario 5328", "data": {"sku": "SKU5328", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5328@example.com", "threshold": 280}},
    {"id": "EMAIL-5329", "title": "Email scenario 5329", "data": {"sku": "SKU5329", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5329@example.com", "threshold": 290}},
    {"id": "EMAIL-5330", "title": "Email scenario 5330", "data": {"sku": "SKU5330", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5330@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
