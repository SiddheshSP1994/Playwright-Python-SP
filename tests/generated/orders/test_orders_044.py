import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2601", "title": "Orders scenario 2601", "data": {"sku": "SKU2601", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2601@example.com", "threshold": 10}},
    {"id": "ORDERS-2602", "title": "Orders scenario 2602", "data": {"sku": "SKU2602", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2602@example.com", "threshold": 20}},
    {"id": "ORDERS-2603", "title": "Orders scenario 2603", "data": {"sku": "SKU2603", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2603@example.com", "threshold": 30}},
    {"id": "ORDERS-2604", "title": "Orders scenario 2604", "data": {"sku": "SKU2604", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2604@example.com", "threshold": 40}},
    {"id": "ORDERS-2605", "title": "Orders scenario 2605", "data": {"sku": "SKU2605", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2605@example.com", "threshold": 50}},
    {"id": "ORDERS-2606", "title": "Orders scenario 2606", "data": {"sku": "SKU2606", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2606@example.com", "threshold": 60}},
    {"id": "ORDERS-2607", "title": "Orders scenario 2607", "data": {"sku": "SKU2607", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2607@example.com", "threshold": 70}},
    {"id": "ORDERS-2608", "title": "Orders scenario 2608", "data": {"sku": "SKU2608", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2608@example.com", "threshold": 80}},
    {"id": "ORDERS-2609", "title": "Orders scenario 2609", "data": {"sku": "SKU2609", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2609@example.com", "threshold": 90}},
    {"id": "ORDERS-2610", "title": "Orders scenario 2610", "data": {"sku": "SKU2610", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2610@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
