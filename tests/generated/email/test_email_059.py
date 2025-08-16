import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3521", "title": "Email scenario 3521", "data": {"sku": "SKU3521", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3521@example.com", "threshold": 210}},
    {"id": "EMAIL-3522", "title": "Email scenario 3522", "data": {"sku": "SKU3522", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3522@example.com", "threshold": 220}},
    {"id": "EMAIL-3523", "title": "Email scenario 3523", "data": {"sku": "SKU3523", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3523@example.com", "threshold": 230}},
    {"id": "EMAIL-3524", "title": "Email scenario 3524", "data": {"sku": "SKU3524", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3524@example.com", "threshold": 240}},
    {"id": "EMAIL-3525", "title": "Email scenario 3525", "data": {"sku": "SKU3525", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3525@example.com", "threshold": 250}},
    {"id": "EMAIL-3526", "title": "Email scenario 3526", "data": {"sku": "SKU3526", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3526@example.com", "threshold": 260}},
    {"id": "EMAIL-3527", "title": "Email scenario 3527", "data": {"sku": "SKU3527", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3527@example.com", "threshold": 270}},
    {"id": "EMAIL-3528", "title": "Email scenario 3528", "data": {"sku": "SKU3528", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3528@example.com", "threshold": 280}},
    {"id": "EMAIL-3529", "title": "Email scenario 3529", "data": {"sku": "SKU3529", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3529@example.com", "threshold": 290}},
    {"id": "EMAIL-3530", "title": "Email scenario 3530", "data": {"sku": "SKU3530", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3530@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
