import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9461", "title": "Email scenario 9461", "data": {"sku": "SKU9461", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9461@example.com", "threshold": 610}},
    {"id": "EMAIL-9462", "title": "Email scenario 9462", "data": {"sku": "SKU9462", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9462@example.com", "threshold": 620}},
    {"id": "EMAIL-9463", "title": "Email scenario 9463", "data": {"sku": "SKU9463", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9463@example.com", "threshold": 630}},
    {"id": "EMAIL-9464", "title": "Email scenario 9464", "data": {"sku": "SKU9464", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9464@example.com", "threshold": 640}},
    {"id": "EMAIL-9465", "title": "Email scenario 9465", "data": {"sku": "SKU9465", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9465@example.com", "threshold": 650}},
    {"id": "EMAIL-9466", "title": "Email scenario 9466", "data": {"sku": "SKU9466", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9466@example.com", "threshold": 660}},
    {"id": "EMAIL-9467", "title": "Email scenario 9467", "data": {"sku": "SKU9467", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9467@example.com", "threshold": 670}},
    {"id": "EMAIL-9468", "title": "Email scenario 9468", "data": {"sku": "SKU9468", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9468@example.com", "threshold": 680}},
    {"id": "EMAIL-9469", "title": "Email scenario 9469", "data": {"sku": "SKU9469", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9469@example.com", "threshold": 690}},
    {"id": "EMAIL-9470", "title": "Email scenario 9470", "data": {"sku": "SKU9470", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9470@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
