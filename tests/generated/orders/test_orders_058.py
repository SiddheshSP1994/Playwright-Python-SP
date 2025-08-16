import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3441", "title": "Orders scenario 3441", "data": {"sku": "SKU3441", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3441@example.com", "threshold": 410}},
    {"id": "ORDERS-3442", "title": "Orders scenario 3442", "data": {"sku": "SKU3442", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3442@example.com", "threshold": 420}},
    {"id": "ORDERS-3443", "title": "Orders scenario 3443", "data": {"sku": "SKU3443", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3443@example.com", "threshold": 430}},
    {"id": "ORDERS-3444", "title": "Orders scenario 3444", "data": {"sku": "SKU3444", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3444@example.com", "threshold": 440}},
    {"id": "ORDERS-3445", "title": "Orders scenario 3445", "data": {"sku": "SKU3445", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3445@example.com", "threshold": 450}},
    {"id": "ORDERS-3446", "title": "Orders scenario 3446", "data": {"sku": "SKU3446", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3446@example.com", "threshold": 460}},
    {"id": "ORDERS-3447", "title": "Orders scenario 3447", "data": {"sku": "SKU3447", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3447@example.com", "threshold": 470}},
    {"id": "ORDERS-3448", "title": "Orders scenario 3448", "data": {"sku": "SKU3448", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3448@example.com", "threshold": 480}},
    {"id": "ORDERS-3449", "title": "Orders scenario 3449", "data": {"sku": "SKU3449", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3449@example.com", "threshold": 490}},
    {"id": "ORDERS-3450", "title": "Orders scenario 3450", "data": {"sku": "SKU3450", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3450@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
