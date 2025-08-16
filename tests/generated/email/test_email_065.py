import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3881", "title": "Email scenario 3881", "data": {"sku": "SKU3881", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3881@example.com", "threshold": 810}},
    {"id": "EMAIL-3882", "title": "Email scenario 3882", "data": {"sku": "SKU3882", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3882@example.com", "threshold": 820}},
    {"id": "EMAIL-3883", "title": "Email scenario 3883", "data": {"sku": "SKU3883", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3883@example.com", "threshold": 830}},
    {"id": "EMAIL-3884", "title": "Email scenario 3884", "data": {"sku": "SKU3884", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3884@example.com", "threshold": 840}},
    {"id": "EMAIL-3885", "title": "Email scenario 3885", "data": {"sku": "SKU3885", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3885@example.com", "threshold": 850}},
    {"id": "EMAIL-3886", "title": "Email scenario 3886", "data": {"sku": "SKU3886", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3886@example.com", "threshold": 860}},
    {"id": "EMAIL-3887", "title": "Email scenario 3887", "data": {"sku": "SKU3887", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3887@example.com", "threshold": 870}},
    {"id": "EMAIL-3888", "title": "Email scenario 3888", "data": {"sku": "SKU3888", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3888@example.com", "threshold": 880}},
    {"id": "EMAIL-3889", "title": "Email scenario 3889", "data": {"sku": "SKU3889", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3889@example.com", "threshold": 890}},
    {"id": "EMAIL-3890", "title": "Email scenario 3890", "data": {"sku": "SKU3890", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3890@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
