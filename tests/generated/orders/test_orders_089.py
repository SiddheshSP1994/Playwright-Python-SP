import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5301", "title": "Orders scenario 5301", "data": {"sku": "SKU5301", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5301@example.com", "threshold": 10}},
    {"id": "ORDERS-5302", "title": "Orders scenario 5302", "data": {"sku": "SKU5302", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5302@example.com", "threshold": 20}},
    {"id": "ORDERS-5303", "title": "Orders scenario 5303", "data": {"sku": "SKU5303", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5303@example.com", "threshold": 30}},
    {"id": "ORDERS-5304", "title": "Orders scenario 5304", "data": {"sku": "SKU5304", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5304@example.com", "threshold": 40}},
    {"id": "ORDERS-5305", "title": "Orders scenario 5305", "data": {"sku": "SKU5305", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5305@example.com", "threshold": 50}},
    {"id": "ORDERS-5306", "title": "Orders scenario 5306", "data": {"sku": "SKU5306", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5306@example.com", "threshold": 60}},
    {"id": "ORDERS-5307", "title": "Orders scenario 5307", "data": {"sku": "SKU5307", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5307@example.com", "threshold": 70}},
    {"id": "ORDERS-5308", "title": "Orders scenario 5308", "data": {"sku": "SKU5308", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5308@example.com", "threshold": 80}},
    {"id": "ORDERS-5309", "title": "Orders scenario 5309", "data": {"sku": "SKU5309", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5309@example.com", "threshold": 90}},
    {"id": "ORDERS-5310", "title": "Orders scenario 5310", "data": {"sku": "SKU5310", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5310@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
