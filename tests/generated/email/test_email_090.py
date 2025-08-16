import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5381", "title": "Email scenario 5381", "data": {"sku": "SKU5381", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5381@example.com", "threshold": 810}},
    {"id": "EMAIL-5382", "title": "Email scenario 5382", "data": {"sku": "SKU5382", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5382@example.com", "threshold": 820}},
    {"id": "EMAIL-5383", "title": "Email scenario 5383", "data": {"sku": "SKU5383", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5383@example.com", "threshold": 830}},
    {"id": "EMAIL-5384", "title": "Email scenario 5384", "data": {"sku": "SKU5384", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5384@example.com", "threshold": 840}},
    {"id": "EMAIL-5385", "title": "Email scenario 5385", "data": {"sku": "SKU5385", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5385@example.com", "threshold": 850}},
    {"id": "EMAIL-5386", "title": "Email scenario 5386", "data": {"sku": "SKU5386", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5386@example.com", "threshold": 860}},
    {"id": "EMAIL-5387", "title": "Email scenario 5387", "data": {"sku": "SKU5387", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5387@example.com", "threshold": 870}},
    {"id": "EMAIL-5388", "title": "Email scenario 5388", "data": {"sku": "SKU5388", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5388@example.com", "threshold": 880}},
    {"id": "EMAIL-5389", "title": "Email scenario 5389", "data": {"sku": "SKU5389", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5389@example.com", "threshold": 890}},
    {"id": "EMAIL-5390", "title": "Email scenario 5390", "data": {"sku": "SKU5390", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5390@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
