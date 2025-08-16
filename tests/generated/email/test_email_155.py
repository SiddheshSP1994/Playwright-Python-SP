import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9281", "title": "Email scenario 9281", "data": {"sku": "SKU9281", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9281@example.com", "threshold": 810}},
    {"id": "EMAIL-9282", "title": "Email scenario 9282", "data": {"sku": "SKU9282", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9282@example.com", "threshold": 820}},
    {"id": "EMAIL-9283", "title": "Email scenario 9283", "data": {"sku": "SKU9283", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9283@example.com", "threshold": 830}},
    {"id": "EMAIL-9284", "title": "Email scenario 9284", "data": {"sku": "SKU9284", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9284@example.com", "threshold": 840}},
    {"id": "EMAIL-9285", "title": "Email scenario 9285", "data": {"sku": "SKU9285", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9285@example.com", "threshold": 850}},
    {"id": "EMAIL-9286", "title": "Email scenario 9286", "data": {"sku": "SKU9286", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9286@example.com", "threshold": 860}},
    {"id": "EMAIL-9287", "title": "Email scenario 9287", "data": {"sku": "SKU9287", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9287@example.com", "threshold": 870}},
    {"id": "EMAIL-9288", "title": "Email scenario 9288", "data": {"sku": "SKU9288", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9288@example.com", "threshold": 880}},
    {"id": "EMAIL-9289", "title": "Email scenario 9289", "data": {"sku": "SKU9289", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9289@example.com", "threshold": 890}},
    {"id": "EMAIL-9290", "title": "Email scenario 9290", "data": {"sku": "SKU9290", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9290@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
