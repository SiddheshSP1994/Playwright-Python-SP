import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8121", "title": "Orders scenario 8121", "data": {"sku": "SKU8121", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8121@example.com", "threshold": 210}},
    {"id": "ORDERS-8122", "title": "Orders scenario 8122", "data": {"sku": "SKU8122", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8122@example.com", "threshold": 220}},
    {"id": "ORDERS-8123", "title": "Orders scenario 8123", "data": {"sku": "SKU8123", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8123@example.com", "threshold": 230}},
    {"id": "ORDERS-8124", "title": "Orders scenario 8124", "data": {"sku": "SKU8124", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8124@example.com", "threshold": 240}},
    {"id": "ORDERS-8125", "title": "Orders scenario 8125", "data": {"sku": "SKU8125", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8125@example.com", "threshold": 250}},
    {"id": "ORDERS-8126", "title": "Orders scenario 8126", "data": {"sku": "SKU8126", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8126@example.com", "threshold": 260}},
    {"id": "ORDERS-8127", "title": "Orders scenario 8127", "data": {"sku": "SKU8127", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8127@example.com", "threshold": 270}},
    {"id": "ORDERS-8128", "title": "Orders scenario 8128", "data": {"sku": "SKU8128", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8128@example.com", "threshold": 280}},
    {"id": "ORDERS-8129", "title": "Orders scenario 8129", "data": {"sku": "SKU8129", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8129@example.com", "threshold": 290}},
    {"id": "ORDERS-8130", "title": "Orders scenario 8130", "data": {"sku": "SKU8130", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8130@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
