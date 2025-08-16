import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2061", "title": "Orders scenario 2061", "data": {"sku": "SKU2061", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2061@example.com", "threshold": 610}},
    {"id": "ORDERS-2062", "title": "Orders scenario 2062", "data": {"sku": "SKU2062", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2062@example.com", "threshold": 620}},
    {"id": "ORDERS-2063", "title": "Orders scenario 2063", "data": {"sku": "SKU2063", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2063@example.com", "threshold": 630}},
    {"id": "ORDERS-2064", "title": "Orders scenario 2064", "data": {"sku": "SKU2064", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2064@example.com", "threshold": 640}},
    {"id": "ORDERS-2065", "title": "Orders scenario 2065", "data": {"sku": "SKU2065", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2065@example.com", "threshold": 650}},
    {"id": "ORDERS-2066", "title": "Orders scenario 2066", "data": {"sku": "SKU2066", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2066@example.com", "threshold": 660}},
    {"id": "ORDERS-2067", "title": "Orders scenario 2067", "data": {"sku": "SKU2067", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2067@example.com", "threshold": 670}},
    {"id": "ORDERS-2068", "title": "Orders scenario 2068", "data": {"sku": "SKU2068", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2068@example.com", "threshold": 680}},
    {"id": "ORDERS-2069", "title": "Orders scenario 2069", "data": {"sku": "SKU2069", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2069@example.com", "threshold": 690}},
    {"id": "ORDERS-2070", "title": "Orders scenario 2070", "data": {"sku": "SKU2070", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2070@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
