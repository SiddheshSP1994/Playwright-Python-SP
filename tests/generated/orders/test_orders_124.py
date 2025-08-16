import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7401", "title": "Orders scenario 7401", "data": {"sku": "SKU7401", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7401@example.com", "threshold": 10}},
    {"id": "ORDERS-7402", "title": "Orders scenario 7402", "data": {"sku": "SKU7402", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7402@example.com", "threshold": 20}},
    {"id": "ORDERS-7403", "title": "Orders scenario 7403", "data": {"sku": "SKU7403", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7403@example.com", "threshold": 30}},
    {"id": "ORDERS-7404", "title": "Orders scenario 7404", "data": {"sku": "SKU7404", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7404@example.com", "threshold": 40}},
    {"id": "ORDERS-7405", "title": "Orders scenario 7405", "data": {"sku": "SKU7405", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7405@example.com", "threshold": 50}},
    {"id": "ORDERS-7406", "title": "Orders scenario 7406", "data": {"sku": "SKU7406", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7406@example.com", "threshold": 60}},
    {"id": "ORDERS-7407", "title": "Orders scenario 7407", "data": {"sku": "SKU7407", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7407@example.com", "threshold": 70}},
    {"id": "ORDERS-7408", "title": "Orders scenario 7408", "data": {"sku": "SKU7408", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7408@example.com", "threshold": 80}},
    {"id": "ORDERS-7409", "title": "Orders scenario 7409", "data": {"sku": "SKU7409", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7409@example.com", "threshold": 90}},
    {"id": "ORDERS-7410", "title": "Orders scenario 7410", "data": {"sku": "SKU7410", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7410@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
