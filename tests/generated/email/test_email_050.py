import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2981", "title": "Email scenario 2981", "data": {"sku": "SKU2981", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2981@example.com", "threshold": 810}},
    {"id": "EMAIL-2982", "title": "Email scenario 2982", "data": {"sku": "SKU2982", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2982@example.com", "threshold": 820}},
    {"id": "EMAIL-2983", "title": "Email scenario 2983", "data": {"sku": "SKU2983", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2983@example.com", "threshold": 830}},
    {"id": "EMAIL-2984", "title": "Email scenario 2984", "data": {"sku": "SKU2984", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2984@example.com", "threshold": 840}},
    {"id": "EMAIL-2985", "title": "Email scenario 2985", "data": {"sku": "SKU2985", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2985@example.com", "threshold": 850}},
    {"id": "EMAIL-2986", "title": "Email scenario 2986", "data": {"sku": "SKU2986", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2986@example.com", "threshold": 860}},
    {"id": "EMAIL-2987", "title": "Email scenario 2987", "data": {"sku": "SKU2987", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2987@example.com", "threshold": 870}},
    {"id": "EMAIL-2988", "title": "Email scenario 2988", "data": {"sku": "SKU2988", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2988@example.com", "threshold": 880}},
    {"id": "EMAIL-2989", "title": "Email scenario 2989", "data": {"sku": "SKU2989", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2989@example.com", "threshold": 890}},
    {"id": "EMAIL-2990", "title": "Email scenario 2990", "data": {"sku": "SKU2990", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2990@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
