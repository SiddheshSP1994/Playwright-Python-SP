import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9341", "title": "Email scenario 9341", "data": {"sku": "SKU9341", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9341@example.com", "threshold": 410}},
    {"id": "EMAIL-9342", "title": "Email scenario 9342", "data": {"sku": "SKU9342", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9342@example.com", "threshold": 420}},
    {"id": "EMAIL-9343", "title": "Email scenario 9343", "data": {"sku": "SKU9343", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9343@example.com", "threshold": 430}},
    {"id": "EMAIL-9344", "title": "Email scenario 9344", "data": {"sku": "SKU9344", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9344@example.com", "threshold": 440}},
    {"id": "EMAIL-9345", "title": "Email scenario 9345", "data": {"sku": "SKU9345", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9345@example.com", "threshold": 450}},
    {"id": "EMAIL-9346", "title": "Email scenario 9346", "data": {"sku": "SKU9346", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9346@example.com", "threshold": 460}},
    {"id": "EMAIL-9347", "title": "Email scenario 9347", "data": {"sku": "SKU9347", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9347@example.com", "threshold": 470}},
    {"id": "EMAIL-9348", "title": "Email scenario 9348", "data": {"sku": "SKU9348", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9348@example.com", "threshold": 480}},
    {"id": "EMAIL-9349", "title": "Email scenario 9349", "data": {"sku": "SKU9349", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9349@example.com", "threshold": 490}},
    {"id": "EMAIL-9350", "title": "Email scenario 9350", "data": {"sku": "SKU9350", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9350@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
