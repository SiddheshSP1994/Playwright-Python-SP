import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6341", "title": "Email scenario 6341", "data": {"sku": "SKU6341", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6341@example.com", "threshold": 410}},
    {"id": "EMAIL-6342", "title": "Email scenario 6342", "data": {"sku": "SKU6342", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6342@example.com", "threshold": 420}},
    {"id": "EMAIL-6343", "title": "Email scenario 6343", "data": {"sku": "SKU6343", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6343@example.com", "threshold": 430}},
    {"id": "EMAIL-6344", "title": "Email scenario 6344", "data": {"sku": "SKU6344", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6344@example.com", "threshold": 440}},
    {"id": "EMAIL-6345", "title": "Email scenario 6345", "data": {"sku": "SKU6345", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6345@example.com", "threshold": 450}},
    {"id": "EMAIL-6346", "title": "Email scenario 6346", "data": {"sku": "SKU6346", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6346@example.com", "threshold": 460}},
    {"id": "EMAIL-6347", "title": "Email scenario 6347", "data": {"sku": "SKU6347", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6347@example.com", "threshold": 470}},
    {"id": "EMAIL-6348", "title": "Email scenario 6348", "data": {"sku": "SKU6348", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6348@example.com", "threshold": 480}},
    {"id": "EMAIL-6349", "title": "Email scenario 6349", "data": {"sku": "SKU6349", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6349@example.com", "threshold": 490}},
    {"id": "EMAIL-6350", "title": "Email scenario 6350", "data": {"sku": "SKU6350", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6350@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
