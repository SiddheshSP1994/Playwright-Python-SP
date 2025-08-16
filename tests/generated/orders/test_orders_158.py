import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9441", "title": "Orders scenario 9441", "data": {"sku": "SKU9441", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9441@example.com", "threshold": 410}},
    {"id": "ORDERS-9442", "title": "Orders scenario 9442", "data": {"sku": "SKU9442", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9442@example.com", "threshold": 420}},
    {"id": "ORDERS-9443", "title": "Orders scenario 9443", "data": {"sku": "SKU9443", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9443@example.com", "threshold": 430}},
    {"id": "ORDERS-9444", "title": "Orders scenario 9444", "data": {"sku": "SKU9444", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9444@example.com", "threshold": 440}},
    {"id": "ORDERS-9445", "title": "Orders scenario 9445", "data": {"sku": "SKU9445", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9445@example.com", "threshold": 450}},
    {"id": "ORDERS-9446", "title": "Orders scenario 9446", "data": {"sku": "SKU9446", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9446@example.com", "threshold": 460}},
    {"id": "ORDERS-9447", "title": "Orders scenario 9447", "data": {"sku": "SKU9447", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9447@example.com", "threshold": 470}},
    {"id": "ORDERS-9448", "title": "Orders scenario 9448", "data": {"sku": "SKU9448", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9448@example.com", "threshold": 480}},
    {"id": "ORDERS-9449", "title": "Orders scenario 9449", "data": {"sku": "SKU9449", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9449@example.com", "threshold": 490}},
    {"id": "ORDERS-9450", "title": "Orders scenario 9450", "data": {"sku": "SKU9450", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9450@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
