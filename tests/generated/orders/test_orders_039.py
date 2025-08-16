import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2301", "title": "Orders scenario 2301", "data": {"sku": "SKU2301", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2301@example.com", "threshold": 10}},
    {"id": "ORDERS-2302", "title": "Orders scenario 2302", "data": {"sku": "SKU2302", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2302@example.com", "threshold": 20}},
    {"id": "ORDERS-2303", "title": "Orders scenario 2303", "data": {"sku": "SKU2303", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2303@example.com", "threshold": 30}},
    {"id": "ORDERS-2304", "title": "Orders scenario 2304", "data": {"sku": "SKU2304", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2304@example.com", "threshold": 40}},
    {"id": "ORDERS-2305", "title": "Orders scenario 2305", "data": {"sku": "SKU2305", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2305@example.com", "threshold": 50}},
    {"id": "ORDERS-2306", "title": "Orders scenario 2306", "data": {"sku": "SKU2306", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2306@example.com", "threshold": 60}},
    {"id": "ORDERS-2307", "title": "Orders scenario 2307", "data": {"sku": "SKU2307", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2307@example.com", "threshold": 70}},
    {"id": "ORDERS-2308", "title": "Orders scenario 2308", "data": {"sku": "SKU2308", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2308@example.com", "threshold": 80}},
    {"id": "ORDERS-2309", "title": "Orders scenario 2309", "data": {"sku": "SKU2309", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2309@example.com", "threshold": 90}},
    {"id": "ORDERS-2310", "title": "Orders scenario 2310", "data": {"sku": "SKU2310", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2310@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
