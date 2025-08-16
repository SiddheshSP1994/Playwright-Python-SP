import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2121", "title": "Orders scenario 2121", "data": {"sku": "SKU2121", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2121@example.com", "threshold": 210}},
    {"id": "ORDERS-2122", "title": "Orders scenario 2122", "data": {"sku": "SKU2122", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2122@example.com", "threshold": 220}},
    {"id": "ORDERS-2123", "title": "Orders scenario 2123", "data": {"sku": "SKU2123", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2123@example.com", "threshold": 230}},
    {"id": "ORDERS-2124", "title": "Orders scenario 2124", "data": {"sku": "SKU2124", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2124@example.com", "threshold": 240}},
    {"id": "ORDERS-2125", "title": "Orders scenario 2125", "data": {"sku": "SKU2125", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2125@example.com", "threshold": 250}},
    {"id": "ORDERS-2126", "title": "Orders scenario 2126", "data": {"sku": "SKU2126", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2126@example.com", "threshold": 260}},
    {"id": "ORDERS-2127", "title": "Orders scenario 2127", "data": {"sku": "SKU2127", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2127@example.com", "threshold": 270}},
    {"id": "ORDERS-2128", "title": "Orders scenario 2128", "data": {"sku": "SKU2128", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2128@example.com", "threshold": 280}},
    {"id": "ORDERS-2129", "title": "Orders scenario 2129", "data": {"sku": "SKU2129", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2129@example.com", "threshold": 290}},
    {"id": "ORDERS-2130", "title": "Orders scenario 2130", "data": {"sku": "SKU2130", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2130@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
