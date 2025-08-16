import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1061", "title": "Email scenario 1061", "data": {"sku": "SKU1061", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1061@example.com", "threshold": 610}},
    {"id": "EMAIL-1062", "title": "Email scenario 1062", "data": {"sku": "SKU1062", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1062@example.com", "threshold": 620}},
    {"id": "EMAIL-1063", "title": "Email scenario 1063", "data": {"sku": "SKU1063", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1063@example.com", "threshold": 630}},
    {"id": "EMAIL-1064", "title": "Email scenario 1064", "data": {"sku": "SKU1064", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1064@example.com", "threshold": 640}},
    {"id": "EMAIL-1065", "title": "Email scenario 1065", "data": {"sku": "SKU1065", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1065@example.com", "threshold": 650}},
    {"id": "EMAIL-1066", "title": "Email scenario 1066", "data": {"sku": "SKU1066", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1066@example.com", "threshold": 660}},
    {"id": "EMAIL-1067", "title": "Email scenario 1067", "data": {"sku": "SKU1067", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1067@example.com", "threshold": 670}},
    {"id": "EMAIL-1068", "title": "Email scenario 1068", "data": {"sku": "SKU1068", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1068@example.com", "threshold": 680}},
    {"id": "EMAIL-1069", "title": "Email scenario 1069", "data": {"sku": "SKU1069", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1069@example.com", "threshold": 690}},
    {"id": "EMAIL-1070", "title": "Email scenario 1070", "data": {"sku": "SKU1070", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1070@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
