import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7101", "title": "Orders scenario 7101", "data": {"sku": "SKU7101", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7101@example.com", "threshold": 10}},
    {"id": "ORDERS-7102", "title": "Orders scenario 7102", "data": {"sku": "SKU7102", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7102@example.com", "threshold": 20}},
    {"id": "ORDERS-7103", "title": "Orders scenario 7103", "data": {"sku": "SKU7103", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7103@example.com", "threshold": 30}},
    {"id": "ORDERS-7104", "title": "Orders scenario 7104", "data": {"sku": "SKU7104", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7104@example.com", "threshold": 40}},
    {"id": "ORDERS-7105", "title": "Orders scenario 7105", "data": {"sku": "SKU7105", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7105@example.com", "threshold": 50}},
    {"id": "ORDERS-7106", "title": "Orders scenario 7106", "data": {"sku": "SKU7106", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7106@example.com", "threshold": 60}},
    {"id": "ORDERS-7107", "title": "Orders scenario 7107", "data": {"sku": "SKU7107", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7107@example.com", "threshold": 70}},
    {"id": "ORDERS-7108", "title": "Orders scenario 7108", "data": {"sku": "SKU7108", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7108@example.com", "threshold": 80}},
    {"id": "ORDERS-7109", "title": "Orders scenario 7109", "data": {"sku": "SKU7109", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7109@example.com", "threshold": 90}},
    {"id": "ORDERS-7110", "title": "Orders scenario 7110", "data": {"sku": "SKU7110", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7110@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
