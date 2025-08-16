import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4361", "title": "Email scenario 4361", "data": {"sku": "SKU4361", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4361@example.com", "threshold": 610}},
    {"id": "EMAIL-4362", "title": "Email scenario 4362", "data": {"sku": "SKU4362", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4362@example.com", "threshold": 620}},
    {"id": "EMAIL-4363", "title": "Email scenario 4363", "data": {"sku": "SKU4363", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4363@example.com", "threshold": 630}},
    {"id": "EMAIL-4364", "title": "Email scenario 4364", "data": {"sku": "SKU4364", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4364@example.com", "threshold": 640}},
    {"id": "EMAIL-4365", "title": "Email scenario 4365", "data": {"sku": "SKU4365", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4365@example.com", "threshold": 650}},
    {"id": "EMAIL-4366", "title": "Email scenario 4366", "data": {"sku": "SKU4366", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4366@example.com", "threshold": 660}},
    {"id": "EMAIL-4367", "title": "Email scenario 4367", "data": {"sku": "SKU4367", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4367@example.com", "threshold": 670}},
    {"id": "EMAIL-4368", "title": "Email scenario 4368", "data": {"sku": "SKU4368", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4368@example.com", "threshold": 680}},
    {"id": "EMAIL-4369", "title": "Email scenario 4369", "data": {"sku": "SKU4369", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4369@example.com", "threshold": 690}},
    {"id": "EMAIL-4370", "title": "Email scenario 4370", "data": {"sku": "SKU4370", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4370@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
