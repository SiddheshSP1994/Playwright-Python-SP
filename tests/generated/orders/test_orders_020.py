import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1161", "title": "Orders scenario 1161", "data": {"sku": "SKU1161", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1161@example.com", "threshold": 610}},
    {"id": "ORDERS-1162", "title": "Orders scenario 1162", "data": {"sku": "SKU1162", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1162@example.com", "threshold": 620}},
    {"id": "ORDERS-1163", "title": "Orders scenario 1163", "data": {"sku": "SKU1163", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1163@example.com", "threshold": 630}},
    {"id": "ORDERS-1164", "title": "Orders scenario 1164", "data": {"sku": "SKU1164", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1164@example.com", "threshold": 640}},
    {"id": "ORDERS-1165", "title": "Orders scenario 1165", "data": {"sku": "SKU1165", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1165@example.com", "threshold": 650}},
    {"id": "ORDERS-1166", "title": "Orders scenario 1166", "data": {"sku": "SKU1166", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1166@example.com", "threshold": 660}},
    {"id": "ORDERS-1167", "title": "Orders scenario 1167", "data": {"sku": "SKU1167", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1167@example.com", "threshold": 670}},
    {"id": "ORDERS-1168", "title": "Orders scenario 1168", "data": {"sku": "SKU1168", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1168@example.com", "threshold": 680}},
    {"id": "ORDERS-1169", "title": "Orders scenario 1169", "data": {"sku": "SKU1169", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1169@example.com", "threshold": 690}},
    {"id": "ORDERS-1170", "title": "Orders scenario 1170", "data": {"sku": "SKU1170", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1170@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
