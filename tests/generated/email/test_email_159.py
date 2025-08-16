import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9521", "title": "Email scenario 9521", "data": {"sku": "SKU9521", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9521@example.com", "threshold": 210}},
    {"id": "EMAIL-9522", "title": "Email scenario 9522", "data": {"sku": "SKU9522", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9522@example.com", "threshold": 220}},
    {"id": "EMAIL-9523", "title": "Email scenario 9523", "data": {"sku": "SKU9523", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9523@example.com", "threshold": 230}},
    {"id": "EMAIL-9524", "title": "Email scenario 9524", "data": {"sku": "SKU9524", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9524@example.com", "threshold": 240}},
    {"id": "EMAIL-9525", "title": "Email scenario 9525", "data": {"sku": "SKU9525", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9525@example.com", "threshold": 250}},
    {"id": "EMAIL-9526", "title": "Email scenario 9526", "data": {"sku": "SKU9526", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9526@example.com", "threshold": 260}},
    {"id": "EMAIL-9527", "title": "Email scenario 9527", "data": {"sku": "SKU9527", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9527@example.com", "threshold": 270}},
    {"id": "EMAIL-9528", "title": "Email scenario 9528", "data": {"sku": "SKU9528", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9528@example.com", "threshold": 280}},
    {"id": "EMAIL-9529", "title": "Email scenario 9529", "data": {"sku": "SKU9529", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9529@example.com", "threshold": 290}},
    {"id": "EMAIL-9530", "title": "Email scenario 9530", "data": {"sku": "SKU9530", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9530@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
