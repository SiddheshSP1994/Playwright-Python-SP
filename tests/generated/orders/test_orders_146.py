import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8721", "title": "Orders scenario 8721", "data": {"sku": "SKU8721", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8721@example.com", "threshold": 210}},
    {"id": "ORDERS-8722", "title": "Orders scenario 8722", "data": {"sku": "SKU8722", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8722@example.com", "threshold": 220}},
    {"id": "ORDERS-8723", "title": "Orders scenario 8723", "data": {"sku": "SKU8723", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8723@example.com", "threshold": 230}},
    {"id": "ORDERS-8724", "title": "Orders scenario 8724", "data": {"sku": "SKU8724", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8724@example.com", "threshold": 240}},
    {"id": "ORDERS-8725", "title": "Orders scenario 8725", "data": {"sku": "SKU8725", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8725@example.com", "threshold": 250}},
    {"id": "ORDERS-8726", "title": "Orders scenario 8726", "data": {"sku": "SKU8726", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8726@example.com", "threshold": 260}},
    {"id": "ORDERS-8727", "title": "Orders scenario 8727", "data": {"sku": "SKU8727", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8727@example.com", "threshold": 270}},
    {"id": "ORDERS-8728", "title": "Orders scenario 8728", "data": {"sku": "SKU8728", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8728@example.com", "threshold": 280}},
    {"id": "ORDERS-8729", "title": "Orders scenario 8729", "data": {"sku": "SKU8729", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8729@example.com", "threshold": 290}},
    {"id": "ORDERS-8730", "title": "Orders scenario 8730", "data": {"sku": "SKU8730", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8730@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
