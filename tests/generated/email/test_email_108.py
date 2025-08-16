import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6461", "title": "Email scenario 6461", "data": {"sku": "SKU6461", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6461@example.com", "threshold": 610}},
    {"id": "EMAIL-6462", "title": "Email scenario 6462", "data": {"sku": "SKU6462", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6462@example.com", "threshold": 620}},
    {"id": "EMAIL-6463", "title": "Email scenario 6463", "data": {"sku": "SKU6463", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6463@example.com", "threshold": 630}},
    {"id": "EMAIL-6464", "title": "Email scenario 6464", "data": {"sku": "SKU6464", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6464@example.com", "threshold": 640}},
    {"id": "EMAIL-6465", "title": "Email scenario 6465", "data": {"sku": "SKU6465", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6465@example.com", "threshold": 650}},
    {"id": "EMAIL-6466", "title": "Email scenario 6466", "data": {"sku": "SKU6466", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6466@example.com", "threshold": 660}},
    {"id": "EMAIL-6467", "title": "Email scenario 6467", "data": {"sku": "SKU6467", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6467@example.com", "threshold": 670}},
    {"id": "EMAIL-6468", "title": "Email scenario 6468", "data": {"sku": "SKU6468", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6468@example.com", "threshold": 680}},
    {"id": "EMAIL-6469", "title": "Email scenario 6469", "data": {"sku": "SKU6469", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6469@example.com", "threshold": 690}},
    {"id": "EMAIL-6470", "title": "Email scenario 6470", "data": {"sku": "SKU6470", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6470@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
