import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6161", "title": "Email scenario 6161", "data": {"sku": "SKU6161", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6161@example.com", "threshold": 610}},
    {"id": "EMAIL-6162", "title": "Email scenario 6162", "data": {"sku": "SKU6162", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6162@example.com", "threshold": 620}},
    {"id": "EMAIL-6163", "title": "Email scenario 6163", "data": {"sku": "SKU6163", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6163@example.com", "threshold": 630}},
    {"id": "EMAIL-6164", "title": "Email scenario 6164", "data": {"sku": "SKU6164", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6164@example.com", "threshold": 640}},
    {"id": "EMAIL-6165", "title": "Email scenario 6165", "data": {"sku": "SKU6165", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6165@example.com", "threshold": 650}},
    {"id": "EMAIL-6166", "title": "Email scenario 6166", "data": {"sku": "SKU6166", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6166@example.com", "threshold": 660}},
    {"id": "EMAIL-6167", "title": "Email scenario 6167", "data": {"sku": "SKU6167", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6167@example.com", "threshold": 670}},
    {"id": "EMAIL-6168", "title": "Email scenario 6168", "data": {"sku": "SKU6168", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6168@example.com", "threshold": 680}},
    {"id": "EMAIL-6169", "title": "Email scenario 6169", "data": {"sku": "SKU6169", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6169@example.com", "threshold": 690}},
    {"id": "EMAIL-6170", "title": "Email scenario 6170", "data": {"sku": "SKU6170", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6170@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
