import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8301", "title": "Orders scenario 8301", "data": {"sku": "SKU8301", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8301@example.com", "threshold": 10}},
    {"id": "ORDERS-8302", "title": "Orders scenario 8302", "data": {"sku": "SKU8302", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8302@example.com", "threshold": 20}},
    {"id": "ORDERS-8303", "title": "Orders scenario 8303", "data": {"sku": "SKU8303", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8303@example.com", "threshold": 30}},
    {"id": "ORDERS-8304", "title": "Orders scenario 8304", "data": {"sku": "SKU8304", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8304@example.com", "threshold": 40}},
    {"id": "ORDERS-8305", "title": "Orders scenario 8305", "data": {"sku": "SKU8305", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8305@example.com", "threshold": 50}},
    {"id": "ORDERS-8306", "title": "Orders scenario 8306", "data": {"sku": "SKU8306", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8306@example.com", "threshold": 60}},
    {"id": "ORDERS-8307", "title": "Orders scenario 8307", "data": {"sku": "SKU8307", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8307@example.com", "threshold": 70}},
    {"id": "ORDERS-8308", "title": "Orders scenario 8308", "data": {"sku": "SKU8308", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8308@example.com", "threshold": 80}},
    {"id": "ORDERS-8309", "title": "Orders scenario 8309", "data": {"sku": "SKU8309", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8309@example.com", "threshold": 90}},
    {"id": "ORDERS-8310", "title": "Orders scenario 8310", "data": {"sku": "SKU8310", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8310@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
