import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5721", "title": "Orders scenario 5721", "data": {"sku": "SKU5721", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5721@example.com", "threshold": 210}},
    {"id": "ORDERS-5722", "title": "Orders scenario 5722", "data": {"sku": "SKU5722", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5722@example.com", "threshold": 220}},
    {"id": "ORDERS-5723", "title": "Orders scenario 5723", "data": {"sku": "SKU5723", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5723@example.com", "threshold": 230}},
    {"id": "ORDERS-5724", "title": "Orders scenario 5724", "data": {"sku": "SKU5724", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5724@example.com", "threshold": 240}},
    {"id": "ORDERS-5725", "title": "Orders scenario 5725", "data": {"sku": "SKU5725", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5725@example.com", "threshold": 250}},
    {"id": "ORDERS-5726", "title": "Orders scenario 5726", "data": {"sku": "SKU5726", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5726@example.com", "threshold": 260}},
    {"id": "ORDERS-5727", "title": "Orders scenario 5727", "data": {"sku": "SKU5727", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5727@example.com", "threshold": 270}},
    {"id": "ORDERS-5728", "title": "Orders scenario 5728", "data": {"sku": "SKU5728", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5728@example.com", "threshold": 280}},
    {"id": "ORDERS-5729", "title": "Orders scenario 5729", "data": {"sku": "SKU5729", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5729@example.com", "threshold": 290}},
    {"id": "ORDERS-5730", "title": "Orders scenario 5730", "data": {"sku": "SKU5730", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5730@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
