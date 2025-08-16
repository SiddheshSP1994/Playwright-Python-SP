import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8981", "title": "Email scenario 8981", "data": {"sku": "SKU8981", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8981@example.com", "threshold": 810}},
    {"id": "EMAIL-8982", "title": "Email scenario 8982", "data": {"sku": "SKU8982", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8982@example.com", "threshold": 820}},
    {"id": "EMAIL-8983", "title": "Email scenario 8983", "data": {"sku": "SKU8983", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8983@example.com", "threshold": 830}},
    {"id": "EMAIL-8984", "title": "Email scenario 8984", "data": {"sku": "SKU8984", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8984@example.com", "threshold": 840}},
    {"id": "EMAIL-8985", "title": "Email scenario 8985", "data": {"sku": "SKU8985", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8985@example.com", "threshold": 850}},
    {"id": "EMAIL-8986", "title": "Email scenario 8986", "data": {"sku": "SKU8986", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8986@example.com", "threshold": 860}},
    {"id": "EMAIL-8987", "title": "Email scenario 8987", "data": {"sku": "SKU8987", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8987@example.com", "threshold": 870}},
    {"id": "EMAIL-8988", "title": "Email scenario 8988", "data": {"sku": "SKU8988", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8988@example.com", "threshold": 880}},
    {"id": "EMAIL-8989", "title": "Email scenario 8989", "data": {"sku": "SKU8989", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8989@example.com", "threshold": 890}},
    {"id": "EMAIL-8990", "title": "Email scenario 8990", "data": {"sku": "SKU8990", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8990@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
