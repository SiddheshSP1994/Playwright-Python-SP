import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4661", "title": "Email scenario 4661", "data": {"sku": "SKU4661", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4661@example.com", "threshold": 610}},
    {"id": "EMAIL-4662", "title": "Email scenario 4662", "data": {"sku": "SKU4662", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4662@example.com", "threshold": 620}},
    {"id": "EMAIL-4663", "title": "Email scenario 4663", "data": {"sku": "SKU4663", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4663@example.com", "threshold": 630}},
    {"id": "EMAIL-4664", "title": "Email scenario 4664", "data": {"sku": "SKU4664", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4664@example.com", "threshold": 640}},
    {"id": "EMAIL-4665", "title": "Email scenario 4665", "data": {"sku": "SKU4665", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4665@example.com", "threshold": 650}},
    {"id": "EMAIL-4666", "title": "Email scenario 4666", "data": {"sku": "SKU4666", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4666@example.com", "threshold": 660}},
    {"id": "EMAIL-4667", "title": "Email scenario 4667", "data": {"sku": "SKU4667", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4667@example.com", "threshold": 670}},
    {"id": "EMAIL-4668", "title": "Email scenario 4668", "data": {"sku": "SKU4668", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4668@example.com", "threshold": 680}},
    {"id": "EMAIL-4669", "title": "Email scenario 4669", "data": {"sku": "SKU4669", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4669@example.com", "threshold": 690}},
    {"id": "EMAIL-4670", "title": "Email scenario 4670", "data": {"sku": "SKU4670", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4670@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
