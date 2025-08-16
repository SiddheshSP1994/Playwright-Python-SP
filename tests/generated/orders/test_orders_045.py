import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2661", "title": "Orders scenario 2661", "data": {"sku": "SKU2661", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2661@example.com", "threshold": 610}},
    {"id": "ORDERS-2662", "title": "Orders scenario 2662", "data": {"sku": "SKU2662", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2662@example.com", "threshold": 620}},
    {"id": "ORDERS-2663", "title": "Orders scenario 2663", "data": {"sku": "SKU2663", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2663@example.com", "threshold": 630}},
    {"id": "ORDERS-2664", "title": "Orders scenario 2664", "data": {"sku": "SKU2664", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2664@example.com", "threshold": 640}},
    {"id": "ORDERS-2665", "title": "Orders scenario 2665", "data": {"sku": "SKU2665", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2665@example.com", "threshold": 650}},
    {"id": "ORDERS-2666", "title": "Orders scenario 2666", "data": {"sku": "SKU2666", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2666@example.com", "threshold": 660}},
    {"id": "ORDERS-2667", "title": "Orders scenario 2667", "data": {"sku": "SKU2667", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2667@example.com", "threshold": 670}},
    {"id": "ORDERS-2668", "title": "Orders scenario 2668", "data": {"sku": "SKU2668", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2668@example.com", "threshold": 680}},
    {"id": "ORDERS-2669", "title": "Orders scenario 2669", "data": {"sku": "SKU2669", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2669@example.com", "threshold": 690}},
    {"id": "ORDERS-2670", "title": "Orders scenario 2670", "data": {"sku": "SKU2670", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2670@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
