import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0621", "title": "Orders scenario 621", "data": {"sku": "SKU621", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user621@example.com", "threshold": 210}},
    {"id": "ORDERS-0622", "title": "Orders scenario 622", "data": {"sku": "SKU622", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user622@example.com", "threshold": 220}},
    {"id": "ORDERS-0623", "title": "Orders scenario 623", "data": {"sku": "SKU623", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user623@example.com", "threshold": 230}},
    {"id": "ORDERS-0624", "title": "Orders scenario 624", "data": {"sku": "SKU624", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user624@example.com", "threshold": 240}},
    {"id": "ORDERS-0625", "title": "Orders scenario 625", "data": {"sku": "SKU625", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user625@example.com", "threshold": 250}},
    {"id": "ORDERS-0626", "title": "Orders scenario 626", "data": {"sku": "SKU626", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user626@example.com", "threshold": 260}},
    {"id": "ORDERS-0627", "title": "Orders scenario 627", "data": {"sku": "SKU627", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user627@example.com", "threshold": 270}},
    {"id": "ORDERS-0628", "title": "Orders scenario 628", "data": {"sku": "SKU628", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user628@example.com", "threshold": 280}},
    {"id": "ORDERS-0629", "title": "Orders scenario 629", "data": {"sku": "SKU629", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user629@example.com", "threshold": 290}},
    {"id": "ORDERS-0630", "title": "Orders scenario 630", "data": {"sku": "SKU630", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user630@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
