import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8381", "title": "Email scenario 8381", "data": {"sku": "SKU8381", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8381@example.com", "threshold": 810}},
    {"id": "EMAIL-8382", "title": "Email scenario 8382", "data": {"sku": "SKU8382", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8382@example.com", "threshold": 820}},
    {"id": "EMAIL-8383", "title": "Email scenario 8383", "data": {"sku": "SKU8383", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8383@example.com", "threshold": 830}},
    {"id": "EMAIL-8384", "title": "Email scenario 8384", "data": {"sku": "SKU8384", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8384@example.com", "threshold": 840}},
    {"id": "EMAIL-8385", "title": "Email scenario 8385", "data": {"sku": "SKU8385", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8385@example.com", "threshold": 850}},
    {"id": "EMAIL-8386", "title": "Email scenario 8386", "data": {"sku": "SKU8386", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8386@example.com", "threshold": 860}},
    {"id": "EMAIL-8387", "title": "Email scenario 8387", "data": {"sku": "SKU8387", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8387@example.com", "threshold": 870}},
    {"id": "EMAIL-8388", "title": "Email scenario 8388", "data": {"sku": "SKU8388", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8388@example.com", "threshold": 880}},
    {"id": "EMAIL-8389", "title": "Email scenario 8389", "data": {"sku": "SKU8389", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8389@example.com", "threshold": 890}},
    {"id": "EMAIL-8390", "title": "Email scenario 8390", "data": {"sku": "SKU8390", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8390@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
