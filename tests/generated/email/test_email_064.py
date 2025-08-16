import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3821", "title": "Email scenario 3821", "data": {"sku": "SKU3821", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3821@example.com", "threshold": 210}},
    {"id": "EMAIL-3822", "title": "Email scenario 3822", "data": {"sku": "SKU3822", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3822@example.com", "threshold": 220}},
    {"id": "EMAIL-3823", "title": "Email scenario 3823", "data": {"sku": "SKU3823", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3823@example.com", "threshold": 230}},
    {"id": "EMAIL-3824", "title": "Email scenario 3824", "data": {"sku": "SKU3824", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3824@example.com", "threshold": 240}},
    {"id": "EMAIL-3825", "title": "Email scenario 3825", "data": {"sku": "SKU3825", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3825@example.com", "threshold": 250}},
    {"id": "EMAIL-3826", "title": "Email scenario 3826", "data": {"sku": "SKU3826", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3826@example.com", "threshold": 260}},
    {"id": "EMAIL-3827", "title": "Email scenario 3827", "data": {"sku": "SKU3827", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3827@example.com", "threshold": 270}},
    {"id": "EMAIL-3828", "title": "Email scenario 3828", "data": {"sku": "SKU3828", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3828@example.com", "threshold": 280}},
    {"id": "EMAIL-3829", "title": "Email scenario 3829", "data": {"sku": "SKU3829", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3829@example.com", "threshold": 290}},
    {"id": "EMAIL-3830", "title": "Email scenario 3830", "data": {"sku": "SKU3830", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3830@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
