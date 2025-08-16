import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3281", "title": "Email scenario 3281", "data": {"sku": "SKU3281", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3281@example.com", "threshold": 810}},
    {"id": "EMAIL-3282", "title": "Email scenario 3282", "data": {"sku": "SKU3282", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3282@example.com", "threshold": 820}},
    {"id": "EMAIL-3283", "title": "Email scenario 3283", "data": {"sku": "SKU3283", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3283@example.com", "threshold": 830}},
    {"id": "EMAIL-3284", "title": "Email scenario 3284", "data": {"sku": "SKU3284", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3284@example.com", "threshold": 840}},
    {"id": "EMAIL-3285", "title": "Email scenario 3285", "data": {"sku": "SKU3285", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3285@example.com", "threshold": 850}},
    {"id": "EMAIL-3286", "title": "Email scenario 3286", "data": {"sku": "SKU3286", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3286@example.com", "threshold": 860}},
    {"id": "EMAIL-3287", "title": "Email scenario 3287", "data": {"sku": "SKU3287", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3287@example.com", "threshold": 870}},
    {"id": "EMAIL-3288", "title": "Email scenario 3288", "data": {"sku": "SKU3288", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3288@example.com", "threshold": 880}},
    {"id": "EMAIL-3289", "title": "Email scenario 3289", "data": {"sku": "SKU3289", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3289@example.com", "threshold": 890}},
    {"id": "EMAIL-3290", "title": "Email scenario 3290", "data": {"sku": "SKU3290", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3290@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
