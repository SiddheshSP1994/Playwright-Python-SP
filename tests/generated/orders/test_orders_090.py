import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5361", "title": "Orders scenario 5361", "data": {"sku": "SKU5361", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5361@example.com", "threshold": 610}},
    {"id": "ORDERS-5362", "title": "Orders scenario 5362", "data": {"sku": "SKU5362", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5362@example.com", "threshold": 620}},
    {"id": "ORDERS-5363", "title": "Orders scenario 5363", "data": {"sku": "SKU5363", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5363@example.com", "threshold": 630}},
    {"id": "ORDERS-5364", "title": "Orders scenario 5364", "data": {"sku": "SKU5364", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5364@example.com", "threshold": 640}},
    {"id": "ORDERS-5365", "title": "Orders scenario 5365", "data": {"sku": "SKU5365", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5365@example.com", "threshold": 650}},
    {"id": "ORDERS-5366", "title": "Orders scenario 5366", "data": {"sku": "SKU5366", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5366@example.com", "threshold": 660}},
    {"id": "ORDERS-5367", "title": "Orders scenario 5367", "data": {"sku": "SKU5367", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5367@example.com", "threshold": 670}},
    {"id": "ORDERS-5368", "title": "Orders scenario 5368", "data": {"sku": "SKU5368", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5368@example.com", "threshold": 680}},
    {"id": "ORDERS-5369", "title": "Orders scenario 5369", "data": {"sku": "SKU5369", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5369@example.com", "threshold": 690}},
    {"id": "ORDERS-5370", "title": "Orders scenario 5370", "data": {"sku": "SKU5370", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5370@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
