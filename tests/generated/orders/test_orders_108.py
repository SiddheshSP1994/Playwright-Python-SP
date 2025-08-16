import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6441", "title": "Orders scenario 6441", "data": {"sku": "SKU6441", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6441@example.com", "threshold": 410}},
    {"id": "ORDERS-6442", "title": "Orders scenario 6442", "data": {"sku": "SKU6442", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6442@example.com", "threshold": 420}},
    {"id": "ORDERS-6443", "title": "Orders scenario 6443", "data": {"sku": "SKU6443", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6443@example.com", "threshold": 430}},
    {"id": "ORDERS-6444", "title": "Orders scenario 6444", "data": {"sku": "SKU6444", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6444@example.com", "threshold": 440}},
    {"id": "ORDERS-6445", "title": "Orders scenario 6445", "data": {"sku": "SKU6445", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6445@example.com", "threshold": 450}},
    {"id": "ORDERS-6446", "title": "Orders scenario 6446", "data": {"sku": "SKU6446", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6446@example.com", "threshold": 460}},
    {"id": "ORDERS-6447", "title": "Orders scenario 6447", "data": {"sku": "SKU6447", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6447@example.com", "threshold": 470}},
    {"id": "ORDERS-6448", "title": "Orders scenario 6448", "data": {"sku": "SKU6448", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6448@example.com", "threshold": 480}},
    {"id": "ORDERS-6449", "title": "Orders scenario 6449", "data": {"sku": "SKU6449", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6449@example.com", "threshold": 490}},
    {"id": "ORDERS-6450", "title": "Orders scenario 6450", "data": {"sku": "SKU6450", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6450@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
