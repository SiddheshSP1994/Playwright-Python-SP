import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2361", "title": "Orders scenario 2361", "data": {"sku": "SKU2361", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2361@example.com", "threshold": 610}},
    {"id": "ORDERS-2362", "title": "Orders scenario 2362", "data": {"sku": "SKU2362", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2362@example.com", "threshold": 620}},
    {"id": "ORDERS-2363", "title": "Orders scenario 2363", "data": {"sku": "SKU2363", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2363@example.com", "threshold": 630}},
    {"id": "ORDERS-2364", "title": "Orders scenario 2364", "data": {"sku": "SKU2364", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2364@example.com", "threshold": 640}},
    {"id": "ORDERS-2365", "title": "Orders scenario 2365", "data": {"sku": "SKU2365", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2365@example.com", "threshold": 650}},
    {"id": "ORDERS-2366", "title": "Orders scenario 2366", "data": {"sku": "SKU2366", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2366@example.com", "threshold": 660}},
    {"id": "ORDERS-2367", "title": "Orders scenario 2367", "data": {"sku": "SKU2367", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2367@example.com", "threshold": 670}},
    {"id": "ORDERS-2368", "title": "Orders scenario 2368", "data": {"sku": "SKU2368", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2368@example.com", "threshold": 680}},
    {"id": "ORDERS-2369", "title": "Orders scenario 2369", "data": {"sku": "SKU2369", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2369@example.com", "threshold": 690}},
    {"id": "ORDERS-2370", "title": "Orders scenario 2370", "data": {"sku": "SKU2370", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2370@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
