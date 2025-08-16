import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3461", "title": "Email scenario 3461", "data": {"sku": "SKU3461", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3461@example.com", "threshold": 610}},
    {"id": "EMAIL-3462", "title": "Email scenario 3462", "data": {"sku": "SKU3462", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3462@example.com", "threshold": 620}},
    {"id": "EMAIL-3463", "title": "Email scenario 3463", "data": {"sku": "SKU3463", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3463@example.com", "threshold": 630}},
    {"id": "EMAIL-3464", "title": "Email scenario 3464", "data": {"sku": "SKU3464", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3464@example.com", "threshold": 640}},
    {"id": "EMAIL-3465", "title": "Email scenario 3465", "data": {"sku": "SKU3465", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3465@example.com", "threshold": 650}},
    {"id": "EMAIL-3466", "title": "Email scenario 3466", "data": {"sku": "SKU3466", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3466@example.com", "threshold": 660}},
    {"id": "EMAIL-3467", "title": "Email scenario 3467", "data": {"sku": "SKU3467", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3467@example.com", "threshold": 670}},
    {"id": "EMAIL-3468", "title": "Email scenario 3468", "data": {"sku": "SKU3468", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3468@example.com", "threshold": 680}},
    {"id": "EMAIL-3469", "title": "Email scenario 3469", "data": {"sku": "SKU3469", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3469@example.com", "threshold": 690}},
    {"id": "EMAIL-3470", "title": "Email scenario 3470", "data": {"sku": "SKU3470", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3470@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
