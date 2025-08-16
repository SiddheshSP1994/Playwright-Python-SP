import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1101", "title": "Orders scenario 1101", "data": {"sku": "SKU1101", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1101@example.com", "threshold": 10}},
    {"id": "ORDERS-1102", "title": "Orders scenario 1102", "data": {"sku": "SKU1102", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1102@example.com", "threshold": 20}},
    {"id": "ORDERS-1103", "title": "Orders scenario 1103", "data": {"sku": "SKU1103", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1103@example.com", "threshold": 30}},
    {"id": "ORDERS-1104", "title": "Orders scenario 1104", "data": {"sku": "SKU1104", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1104@example.com", "threshold": 40}},
    {"id": "ORDERS-1105", "title": "Orders scenario 1105", "data": {"sku": "SKU1105", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1105@example.com", "threshold": 50}},
    {"id": "ORDERS-1106", "title": "Orders scenario 1106", "data": {"sku": "SKU1106", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1106@example.com", "threshold": 60}},
    {"id": "ORDERS-1107", "title": "Orders scenario 1107", "data": {"sku": "SKU1107", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1107@example.com", "threshold": 70}},
    {"id": "ORDERS-1108", "title": "Orders scenario 1108", "data": {"sku": "SKU1108", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1108@example.com", "threshold": 80}},
    {"id": "ORDERS-1109", "title": "Orders scenario 1109", "data": {"sku": "SKU1109", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1109@example.com", "threshold": 90}},
    {"id": "ORDERS-1110", "title": "Orders scenario 1110", "data": {"sku": "SKU1110", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1110@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
