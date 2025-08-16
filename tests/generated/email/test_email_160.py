import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9581", "title": "Email scenario 9581", "data": {"sku": "SKU9581", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9581@example.com", "threshold": 810}},
    {"id": "EMAIL-9582", "title": "Email scenario 9582", "data": {"sku": "SKU9582", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9582@example.com", "threshold": 820}},
    {"id": "EMAIL-9583", "title": "Email scenario 9583", "data": {"sku": "SKU9583", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9583@example.com", "threshold": 830}},
    {"id": "EMAIL-9584", "title": "Email scenario 9584", "data": {"sku": "SKU9584", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9584@example.com", "threshold": 840}},
    {"id": "EMAIL-9585", "title": "Email scenario 9585", "data": {"sku": "SKU9585", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9585@example.com", "threshold": 850}},
    {"id": "EMAIL-9586", "title": "Email scenario 9586", "data": {"sku": "SKU9586", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9586@example.com", "threshold": 860}},
    {"id": "EMAIL-9587", "title": "Email scenario 9587", "data": {"sku": "SKU9587", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9587@example.com", "threshold": 870}},
    {"id": "EMAIL-9588", "title": "Email scenario 9588", "data": {"sku": "SKU9588", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9588@example.com", "threshold": 880}},
    {"id": "EMAIL-9589", "title": "Email scenario 9589", "data": {"sku": "SKU9589", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9589@example.com", "threshold": 890}},
    {"id": "EMAIL-9590", "title": "Email scenario 9590", "data": {"sku": "SKU9590", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9590@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
