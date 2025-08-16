import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3341", "title": "Email scenario 3341", "data": {"sku": "SKU3341", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3341@example.com", "threshold": 410}},
    {"id": "EMAIL-3342", "title": "Email scenario 3342", "data": {"sku": "SKU3342", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3342@example.com", "threshold": 420}},
    {"id": "EMAIL-3343", "title": "Email scenario 3343", "data": {"sku": "SKU3343", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3343@example.com", "threshold": 430}},
    {"id": "EMAIL-3344", "title": "Email scenario 3344", "data": {"sku": "SKU3344", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3344@example.com", "threshold": 440}},
    {"id": "EMAIL-3345", "title": "Email scenario 3345", "data": {"sku": "SKU3345", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3345@example.com", "threshold": 450}},
    {"id": "EMAIL-3346", "title": "Email scenario 3346", "data": {"sku": "SKU3346", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3346@example.com", "threshold": 460}},
    {"id": "EMAIL-3347", "title": "Email scenario 3347", "data": {"sku": "SKU3347", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3347@example.com", "threshold": 470}},
    {"id": "EMAIL-3348", "title": "Email scenario 3348", "data": {"sku": "SKU3348", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3348@example.com", "threshold": 480}},
    {"id": "EMAIL-3349", "title": "Email scenario 3349", "data": {"sku": "SKU3349", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3349@example.com", "threshold": 490}},
    {"id": "EMAIL-3350", "title": "Email scenario 3350", "data": {"sku": "SKU3350", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3350@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
