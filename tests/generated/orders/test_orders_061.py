import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3621", "title": "Orders scenario 3621", "data": {"sku": "SKU3621", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3621@example.com", "threshold": 210}},
    {"id": "ORDERS-3622", "title": "Orders scenario 3622", "data": {"sku": "SKU3622", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3622@example.com", "threshold": 220}},
    {"id": "ORDERS-3623", "title": "Orders scenario 3623", "data": {"sku": "SKU3623", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3623@example.com", "threshold": 230}},
    {"id": "ORDERS-3624", "title": "Orders scenario 3624", "data": {"sku": "SKU3624", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3624@example.com", "threshold": 240}},
    {"id": "ORDERS-3625", "title": "Orders scenario 3625", "data": {"sku": "SKU3625", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3625@example.com", "threshold": 250}},
    {"id": "ORDERS-3626", "title": "Orders scenario 3626", "data": {"sku": "SKU3626", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3626@example.com", "threshold": 260}},
    {"id": "ORDERS-3627", "title": "Orders scenario 3627", "data": {"sku": "SKU3627", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3627@example.com", "threshold": 270}},
    {"id": "ORDERS-3628", "title": "Orders scenario 3628", "data": {"sku": "SKU3628", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3628@example.com", "threshold": 280}},
    {"id": "ORDERS-3629", "title": "Orders scenario 3629", "data": {"sku": "SKU3629", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3629@example.com", "threshold": 290}},
    {"id": "ORDERS-3630", "title": "Orders scenario 3630", "data": {"sku": "SKU3630", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3630@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
