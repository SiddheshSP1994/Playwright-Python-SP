import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6581", "title": "Email scenario 6581", "data": {"sku": "SKU6581", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6581@example.com", "threshold": 810}},
    {"id": "EMAIL-6582", "title": "Email scenario 6582", "data": {"sku": "SKU6582", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6582@example.com", "threshold": 820}},
    {"id": "EMAIL-6583", "title": "Email scenario 6583", "data": {"sku": "SKU6583", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6583@example.com", "threshold": 830}},
    {"id": "EMAIL-6584", "title": "Email scenario 6584", "data": {"sku": "SKU6584", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6584@example.com", "threshold": 840}},
    {"id": "EMAIL-6585", "title": "Email scenario 6585", "data": {"sku": "SKU6585", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6585@example.com", "threshold": 850}},
    {"id": "EMAIL-6586", "title": "Email scenario 6586", "data": {"sku": "SKU6586", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6586@example.com", "threshold": 860}},
    {"id": "EMAIL-6587", "title": "Email scenario 6587", "data": {"sku": "SKU6587", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6587@example.com", "threshold": 870}},
    {"id": "EMAIL-6588", "title": "Email scenario 6588", "data": {"sku": "SKU6588", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6588@example.com", "threshold": 880}},
    {"id": "EMAIL-6589", "title": "Email scenario 6589", "data": {"sku": "SKU6589", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6589@example.com", "threshold": 890}},
    {"id": "EMAIL-6590", "title": "Email scenario 6590", "data": {"sku": "SKU6590", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6590@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
