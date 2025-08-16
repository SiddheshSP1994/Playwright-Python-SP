import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3401", "title": "Email scenario 3401", "data": {"sku": "SKU3401", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3401@example.com", "threshold": 10}},
    {"id": "EMAIL-3402", "title": "Email scenario 3402", "data": {"sku": "SKU3402", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3402@example.com", "threshold": 20}},
    {"id": "EMAIL-3403", "title": "Email scenario 3403", "data": {"sku": "SKU3403", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3403@example.com", "threshold": 30}},
    {"id": "EMAIL-3404", "title": "Email scenario 3404", "data": {"sku": "SKU3404", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3404@example.com", "threshold": 40}},
    {"id": "EMAIL-3405", "title": "Email scenario 3405", "data": {"sku": "SKU3405", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3405@example.com", "threshold": 50}},
    {"id": "EMAIL-3406", "title": "Email scenario 3406", "data": {"sku": "SKU3406", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3406@example.com", "threshold": 60}},
    {"id": "EMAIL-3407", "title": "Email scenario 3407", "data": {"sku": "SKU3407", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3407@example.com", "threshold": 70}},
    {"id": "EMAIL-3408", "title": "Email scenario 3408", "data": {"sku": "SKU3408", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3408@example.com", "threshold": 80}},
    {"id": "EMAIL-3409", "title": "Email scenario 3409", "data": {"sku": "SKU3409", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3409@example.com", "threshold": 90}},
    {"id": "EMAIL-3410", "title": "Email scenario 3410", "data": {"sku": "SKU3410", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3410@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
