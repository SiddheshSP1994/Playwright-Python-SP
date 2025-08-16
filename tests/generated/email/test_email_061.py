import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3641", "title": "Email scenario 3641", "data": {"sku": "SKU3641", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3641@example.com", "threshold": 410}},
    {"id": "EMAIL-3642", "title": "Email scenario 3642", "data": {"sku": "SKU3642", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3642@example.com", "threshold": 420}},
    {"id": "EMAIL-3643", "title": "Email scenario 3643", "data": {"sku": "SKU3643", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3643@example.com", "threshold": 430}},
    {"id": "EMAIL-3644", "title": "Email scenario 3644", "data": {"sku": "SKU3644", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3644@example.com", "threshold": 440}},
    {"id": "EMAIL-3645", "title": "Email scenario 3645", "data": {"sku": "SKU3645", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3645@example.com", "threshold": 450}},
    {"id": "EMAIL-3646", "title": "Email scenario 3646", "data": {"sku": "SKU3646", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3646@example.com", "threshold": 460}},
    {"id": "EMAIL-3647", "title": "Email scenario 3647", "data": {"sku": "SKU3647", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3647@example.com", "threshold": 470}},
    {"id": "EMAIL-3648", "title": "Email scenario 3648", "data": {"sku": "SKU3648", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3648@example.com", "threshold": 480}},
    {"id": "EMAIL-3649", "title": "Email scenario 3649", "data": {"sku": "SKU3649", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3649@example.com", "threshold": 490}},
    {"id": "EMAIL-3650", "title": "Email scenario 3650", "data": {"sku": "SKU3650", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3650@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
