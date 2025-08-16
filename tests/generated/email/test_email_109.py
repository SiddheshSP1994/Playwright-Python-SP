import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6521", "title": "Email scenario 6521", "data": {"sku": "SKU6521", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6521@example.com", "threshold": 210}},
    {"id": "EMAIL-6522", "title": "Email scenario 6522", "data": {"sku": "SKU6522", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6522@example.com", "threshold": 220}},
    {"id": "EMAIL-6523", "title": "Email scenario 6523", "data": {"sku": "SKU6523", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6523@example.com", "threshold": 230}},
    {"id": "EMAIL-6524", "title": "Email scenario 6524", "data": {"sku": "SKU6524", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6524@example.com", "threshold": 240}},
    {"id": "EMAIL-6525", "title": "Email scenario 6525", "data": {"sku": "SKU6525", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6525@example.com", "threshold": 250}},
    {"id": "EMAIL-6526", "title": "Email scenario 6526", "data": {"sku": "SKU6526", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6526@example.com", "threshold": 260}},
    {"id": "EMAIL-6527", "title": "Email scenario 6527", "data": {"sku": "SKU6527", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6527@example.com", "threshold": 270}},
    {"id": "EMAIL-6528", "title": "Email scenario 6528", "data": {"sku": "SKU6528", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6528@example.com", "threshold": 280}},
    {"id": "EMAIL-6529", "title": "Email scenario 6529", "data": {"sku": "SKU6529", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6529@example.com", "threshold": 290}},
    {"id": "EMAIL-6530", "title": "Email scenario 6530", "data": {"sku": "SKU6530", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6530@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
