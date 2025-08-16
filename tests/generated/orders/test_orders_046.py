import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2721", "title": "Orders scenario 2721", "data": {"sku": "SKU2721", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2721@example.com", "threshold": 210}},
    {"id": "ORDERS-2722", "title": "Orders scenario 2722", "data": {"sku": "SKU2722", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2722@example.com", "threshold": 220}},
    {"id": "ORDERS-2723", "title": "Orders scenario 2723", "data": {"sku": "SKU2723", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2723@example.com", "threshold": 230}},
    {"id": "ORDERS-2724", "title": "Orders scenario 2724", "data": {"sku": "SKU2724", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2724@example.com", "threshold": 240}},
    {"id": "ORDERS-2725", "title": "Orders scenario 2725", "data": {"sku": "SKU2725", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2725@example.com", "threshold": 250}},
    {"id": "ORDERS-2726", "title": "Orders scenario 2726", "data": {"sku": "SKU2726", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2726@example.com", "threshold": 260}},
    {"id": "ORDERS-2727", "title": "Orders scenario 2727", "data": {"sku": "SKU2727", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2727@example.com", "threshold": 270}},
    {"id": "ORDERS-2728", "title": "Orders scenario 2728", "data": {"sku": "SKU2728", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2728@example.com", "threshold": 280}},
    {"id": "ORDERS-2729", "title": "Orders scenario 2729", "data": {"sku": "SKU2729", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2729@example.com", "threshold": 290}},
    {"id": "ORDERS-2730", "title": "Orders scenario 2730", "data": {"sku": "SKU2730", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2730@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
