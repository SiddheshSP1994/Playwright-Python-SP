import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6641", "title": "Email scenario 6641", "data": {"sku": "SKU6641", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6641@example.com", "threshold": 410}},
    {"id": "EMAIL-6642", "title": "Email scenario 6642", "data": {"sku": "SKU6642", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6642@example.com", "threshold": 420}},
    {"id": "EMAIL-6643", "title": "Email scenario 6643", "data": {"sku": "SKU6643", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6643@example.com", "threshold": 430}},
    {"id": "EMAIL-6644", "title": "Email scenario 6644", "data": {"sku": "SKU6644", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6644@example.com", "threshold": 440}},
    {"id": "EMAIL-6645", "title": "Email scenario 6645", "data": {"sku": "SKU6645", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6645@example.com", "threshold": 450}},
    {"id": "EMAIL-6646", "title": "Email scenario 6646", "data": {"sku": "SKU6646", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6646@example.com", "threshold": 460}},
    {"id": "EMAIL-6647", "title": "Email scenario 6647", "data": {"sku": "SKU6647", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6647@example.com", "threshold": 470}},
    {"id": "EMAIL-6648", "title": "Email scenario 6648", "data": {"sku": "SKU6648", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6648@example.com", "threshold": 480}},
    {"id": "EMAIL-6649", "title": "Email scenario 6649", "data": {"sku": "SKU6649", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6649@example.com", "threshold": 490}},
    {"id": "EMAIL-6650", "title": "Email scenario 6650", "data": {"sku": "SKU6650", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6650@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
