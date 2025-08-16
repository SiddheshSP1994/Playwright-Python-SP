import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4161", "title": "Orders scenario 4161", "data": {"sku": "SKU4161", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4161@example.com", "threshold": 610}},
    {"id": "ORDERS-4162", "title": "Orders scenario 4162", "data": {"sku": "SKU4162", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4162@example.com", "threshold": 620}},
    {"id": "ORDERS-4163", "title": "Orders scenario 4163", "data": {"sku": "SKU4163", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4163@example.com", "threshold": 630}},
    {"id": "ORDERS-4164", "title": "Orders scenario 4164", "data": {"sku": "SKU4164", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4164@example.com", "threshold": 640}},
    {"id": "ORDERS-4165", "title": "Orders scenario 4165", "data": {"sku": "SKU4165", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4165@example.com", "threshold": 650}},
    {"id": "ORDERS-4166", "title": "Orders scenario 4166", "data": {"sku": "SKU4166", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4166@example.com", "threshold": 660}},
    {"id": "ORDERS-4167", "title": "Orders scenario 4167", "data": {"sku": "SKU4167", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4167@example.com", "threshold": 670}},
    {"id": "ORDERS-4168", "title": "Orders scenario 4168", "data": {"sku": "SKU4168", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4168@example.com", "threshold": 680}},
    {"id": "ORDERS-4169", "title": "Orders scenario 4169", "data": {"sku": "SKU4169", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4169@example.com", "threshold": 690}},
    {"id": "ORDERS-4170", "title": "Orders scenario 4170", "data": {"sku": "SKU4170", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4170@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
