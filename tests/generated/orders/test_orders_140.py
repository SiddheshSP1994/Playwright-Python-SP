import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8361", "title": "Orders scenario 8361", "data": {"sku": "SKU8361", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8361@example.com", "threshold": 610}},
    {"id": "ORDERS-8362", "title": "Orders scenario 8362", "data": {"sku": "SKU8362", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8362@example.com", "threshold": 620}},
    {"id": "ORDERS-8363", "title": "Orders scenario 8363", "data": {"sku": "SKU8363", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8363@example.com", "threshold": 630}},
    {"id": "ORDERS-8364", "title": "Orders scenario 8364", "data": {"sku": "SKU8364", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8364@example.com", "threshold": 640}},
    {"id": "ORDERS-8365", "title": "Orders scenario 8365", "data": {"sku": "SKU8365", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8365@example.com", "threshold": 650}},
    {"id": "ORDERS-8366", "title": "Orders scenario 8366", "data": {"sku": "SKU8366", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8366@example.com", "threshold": 660}},
    {"id": "ORDERS-8367", "title": "Orders scenario 8367", "data": {"sku": "SKU8367", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8367@example.com", "threshold": 670}},
    {"id": "ORDERS-8368", "title": "Orders scenario 8368", "data": {"sku": "SKU8368", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8368@example.com", "threshold": 680}},
    {"id": "ORDERS-8369", "title": "Orders scenario 8369", "data": {"sku": "SKU8369", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8369@example.com", "threshold": 690}},
    {"id": "ORDERS-8370", "title": "Orders scenario 8370", "data": {"sku": "SKU8370", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8370@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
