import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1641", "title": "Orders scenario 1641", "data": {"sku": "SKU1641", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1641@example.com", "threshold": 410}},
    {"id": "ORDERS-1642", "title": "Orders scenario 1642", "data": {"sku": "SKU1642", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1642@example.com", "threshold": 420}},
    {"id": "ORDERS-1643", "title": "Orders scenario 1643", "data": {"sku": "SKU1643", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1643@example.com", "threshold": 430}},
    {"id": "ORDERS-1644", "title": "Orders scenario 1644", "data": {"sku": "SKU1644", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1644@example.com", "threshold": 440}},
    {"id": "ORDERS-1645", "title": "Orders scenario 1645", "data": {"sku": "SKU1645", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1645@example.com", "threshold": 450}},
    {"id": "ORDERS-1646", "title": "Orders scenario 1646", "data": {"sku": "SKU1646", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1646@example.com", "threshold": 460}},
    {"id": "ORDERS-1647", "title": "Orders scenario 1647", "data": {"sku": "SKU1647", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1647@example.com", "threshold": 470}},
    {"id": "ORDERS-1648", "title": "Orders scenario 1648", "data": {"sku": "SKU1648", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1648@example.com", "threshold": 480}},
    {"id": "ORDERS-1649", "title": "Orders scenario 1649", "data": {"sku": "SKU1649", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1649@example.com", "threshold": 490}},
    {"id": "ORDERS-1650", "title": "Orders scenario 1650", "data": {"sku": "SKU1650", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1650@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
