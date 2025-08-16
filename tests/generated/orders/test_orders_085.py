import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5061", "title": "Orders scenario 5061", "data": {"sku": "SKU5061", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5061@example.com", "threshold": 610}},
    {"id": "ORDERS-5062", "title": "Orders scenario 5062", "data": {"sku": "SKU5062", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5062@example.com", "threshold": 620}},
    {"id": "ORDERS-5063", "title": "Orders scenario 5063", "data": {"sku": "SKU5063", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5063@example.com", "threshold": 630}},
    {"id": "ORDERS-5064", "title": "Orders scenario 5064", "data": {"sku": "SKU5064", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5064@example.com", "threshold": 640}},
    {"id": "ORDERS-5065", "title": "Orders scenario 5065", "data": {"sku": "SKU5065", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5065@example.com", "threshold": 650}},
    {"id": "ORDERS-5066", "title": "Orders scenario 5066", "data": {"sku": "SKU5066", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5066@example.com", "threshold": 660}},
    {"id": "ORDERS-5067", "title": "Orders scenario 5067", "data": {"sku": "SKU5067", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5067@example.com", "threshold": 670}},
    {"id": "ORDERS-5068", "title": "Orders scenario 5068", "data": {"sku": "SKU5068", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5068@example.com", "threshold": 680}},
    {"id": "ORDERS-5069", "title": "Orders scenario 5069", "data": {"sku": "SKU5069", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5069@example.com", "threshold": 690}},
    {"id": "ORDERS-5070", "title": "Orders scenario 5070", "data": {"sku": "SKU5070", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5070@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
