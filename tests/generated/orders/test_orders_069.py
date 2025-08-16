import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4101", "title": "Orders scenario 4101", "data": {"sku": "SKU4101", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4101@example.com", "threshold": 10}},
    {"id": "ORDERS-4102", "title": "Orders scenario 4102", "data": {"sku": "SKU4102", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4102@example.com", "threshold": 20}},
    {"id": "ORDERS-4103", "title": "Orders scenario 4103", "data": {"sku": "SKU4103", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4103@example.com", "threshold": 30}},
    {"id": "ORDERS-4104", "title": "Orders scenario 4104", "data": {"sku": "SKU4104", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4104@example.com", "threshold": 40}},
    {"id": "ORDERS-4105", "title": "Orders scenario 4105", "data": {"sku": "SKU4105", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4105@example.com", "threshold": 50}},
    {"id": "ORDERS-4106", "title": "Orders scenario 4106", "data": {"sku": "SKU4106", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4106@example.com", "threshold": 60}},
    {"id": "ORDERS-4107", "title": "Orders scenario 4107", "data": {"sku": "SKU4107", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4107@example.com", "threshold": 70}},
    {"id": "ORDERS-4108", "title": "Orders scenario 4108", "data": {"sku": "SKU4108", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4108@example.com", "threshold": 80}},
    {"id": "ORDERS-4109", "title": "Orders scenario 4109", "data": {"sku": "SKU4109", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4109@example.com", "threshold": 90}},
    {"id": "ORDERS-4110", "title": "Orders scenario 4110", "data": {"sku": "SKU4110", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4110@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
