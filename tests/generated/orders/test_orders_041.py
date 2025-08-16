import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2421", "title": "Orders scenario 2421", "data": {"sku": "SKU2421", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2421@example.com", "threshold": 210}},
    {"id": "ORDERS-2422", "title": "Orders scenario 2422", "data": {"sku": "SKU2422", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2422@example.com", "threshold": 220}},
    {"id": "ORDERS-2423", "title": "Orders scenario 2423", "data": {"sku": "SKU2423", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2423@example.com", "threshold": 230}},
    {"id": "ORDERS-2424", "title": "Orders scenario 2424", "data": {"sku": "SKU2424", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2424@example.com", "threshold": 240}},
    {"id": "ORDERS-2425", "title": "Orders scenario 2425", "data": {"sku": "SKU2425", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2425@example.com", "threshold": 250}},
    {"id": "ORDERS-2426", "title": "Orders scenario 2426", "data": {"sku": "SKU2426", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2426@example.com", "threshold": 260}},
    {"id": "ORDERS-2427", "title": "Orders scenario 2427", "data": {"sku": "SKU2427", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2427@example.com", "threshold": 270}},
    {"id": "ORDERS-2428", "title": "Orders scenario 2428", "data": {"sku": "SKU2428", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2428@example.com", "threshold": 280}},
    {"id": "ORDERS-2429", "title": "Orders scenario 2429", "data": {"sku": "SKU2429", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2429@example.com", "threshold": 290}},
    {"id": "ORDERS-2430", "title": "Orders scenario 2430", "data": {"sku": "SKU2430", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2430@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
