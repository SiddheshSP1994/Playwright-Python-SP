import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3581", "title": "Email scenario 3581", "data": {"sku": "SKU3581", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3581@example.com", "threshold": 810}},
    {"id": "EMAIL-3582", "title": "Email scenario 3582", "data": {"sku": "SKU3582", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3582@example.com", "threshold": 820}},
    {"id": "EMAIL-3583", "title": "Email scenario 3583", "data": {"sku": "SKU3583", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3583@example.com", "threshold": 830}},
    {"id": "EMAIL-3584", "title": "Email scenario 3584", "data": {"sku": "SKU3584", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3584@example.com", "threshold": 840}},
    {"id": "EMAIL-3585", "title": "Email scenario 3585", "data": {"sku": "SKU3585", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3585@example.com", "threshold": 850}},
    {"id": "EMAIL-3586", "title": "Email scenario 3586", "data": {"sku": "SKU3586", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3586@example.com", "threshold": 860}},
    {"id": "EMAIL-3587", "title": "Email scenario 3587", "data": {"sku": "SKU3587", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3587@example.com", "threshold": 870}},
    {"id": "EMAIL-3588", "title": "Email scenario 3588", "data": {"sku": "SKU3588", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3588@example.com", "threshold": 880}},
    {"id": "EMAIL-3589", "title": "Email scenario 3589", "data": {"sku": "SKU3589", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3589@example.com", "threshold": 890}},
    {"id": "EMAIL-3590", "title": "Email scenario 3590", "data": {"sku": "SKU3590", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3590@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
