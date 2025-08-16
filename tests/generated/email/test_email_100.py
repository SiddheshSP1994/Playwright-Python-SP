import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5981", "title": "Email scenario 5981", "data": {"sku": "SKU5981", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5981@example.com", "threshold": 810}},
    {"id": "EMAIL-5982", "title": "Email scenario 5982", "data": {"sku": "SKU5982", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5982@example.com", "threshold": 820}},
    {"id": "EMAIL-5983", "title": "Email scenario 5983", "data": {"sku": "SKU5983", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5983@example.com", "threshold": 830}},
    {"id": "EMAIL-5984", "title": "Email scenario 5984", "data": {"sku": "SKU5984", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5984@example.com", "threshold": 840}},
    {"id": "EMAIL-5985", "title": "Email scenario 5985", "data": {"sku": "SKU5985", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5985@example.com", "threshold": 850}},
    {"id": "EMAIL-5986", "title": "Email scenario 5986", "data": {"sku": "SKU5986", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5986@example.com", "threshold": 860}},
    {"id": "EMAIL-5987", "title": "Email scenario 5987", "data": {"sku": "SKU5987", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5987@example.com", "threshold": 870}},
    {"id": "EMAIL-5988", "title": "Email scenario 5988", "data": {"sku": "SKU5988", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5988@example.com", "threshold": 880}},
    {"id": "EMAIL-5989", "title": "Email scenario 5989", "data": {"sku": "SKU5989", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5989@example.com", "threshold": 890}},
    {"id": "EMAIL-5990", "title": "Email scenario 5990", "data": {"sku": "SKU5990", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5990@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
