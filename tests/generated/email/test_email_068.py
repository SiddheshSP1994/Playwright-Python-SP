import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4061", "title": "Email scenario 4061", "data": {"sku": "SKU4061", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4061@example.com", "threshold": 610}},
    {"id": "EMAIL-4062", "title": "Email scenario 4062", "data": {"sku": "SKU4062", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4062@example.com", "threshold": 620}},
    {"id": "EMAIL-4063", "title": "Email scenario 4063", "data": {"sku": "SKU4063", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4063@example.com", "threshold": 630}},
    {"id": "EMAIL-4064", "title": "Email scenario 4064", "data": {"sku": "SKU4064", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4064@example.com", "threshold": 640}},
    {"id": "EMAIL-4065", "title": "Email scenario 4065", "data": {"sku": "SKU4065", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4065@example.com", "threshold": 650}},
    {"id": "EMAIL-4066", "title": "Email scenario 4066", "data": {"sku": "SKU4066", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4066@example.com", "threshold": 660}},
    {"id": "EMAIL-4067", "title": "Email scenario 4067", "data": {"sku": "SKU4067", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4067@example.com", "threshold": 670}},
    {"id": "EMAIL-4068", "title": "Email scenario 4068", "data": {"sku": "SKU4068", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4068@example.com", "threshold": 680}},
    {"id": "EMAIL-4069", "title": "Email scenario 4069", "data": {"sku": "SKU4069", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4069@example.com", "threshold": 690}},
    {"id": "EMAIL-4070", "title": "Email scenario 4070", "data": {"sku": "SKU4070", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4070@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
