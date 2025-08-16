import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7361", "title": "Email scenario 7361", "data": {"sku": "SKU7361", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7361@example.com", "threshold": 610}},
    {"id": "EMAIL-7362", "title": "Email scenario 7362", "data": {"sku": "SKU7362", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7362@example.com", "threshold": 620}},
    {"id": "EMAIL-7363", "title": "Email scenario 7363", "data": {"sku": "SKU7363", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7363@example.com", "threshold": 630}},
    {"id": "EMAIL-7364", "title": "Email scenario 7364", "data": {"sku": "SKU7364", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7364@example.com", "threshold": 640}},
    {"id": "EMAIL-7365", "title": "Email scenario 7365", "data": {"sku": "SKU7365", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7365@example.com", "threshold": 650}},
    {"id": "EMAIL-7366", "title": "Email scenario 7366", "data": {"sku": "SKU7366", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7366@example.com", "threshold": 660}},
    {"id": "EMAIL-7367", "title": "Email scenario 7367", "data": {"sku": "SKU7367", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7367@example.com", "threshold": 670}},
    {"id": "EMAIL-7368", "title": "Email scenario 7368", "data": {"sku": "SKU7368", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7368@example.com", "threshold": 680}},
    {"id": "EMAIL-7369", "title": "Email scenario 7369", "data": {"sku": "SKU7369", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7369@example.com", "threshold": 690}},
    {"id": "EMAIL-7370", "title": "Email scenario 7370", "data": {"sku": "SKU7370", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7370@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
