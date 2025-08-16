import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9981", "title": "Orders scenario 9981", "data": {"sku": "SKU9981", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9981@example.com", "threshold": 810}},
    {"id": "ORDERS-9982", "title": "Orders scenario 9982", "data": {"sku": "SKU9982", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9982@example.com", "threshold": 820}},
    {"id": "ORDERS-9983", "title": "Orders scenario 9983", "data": {"sku": "SKU9983", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9983@example.com", "threshold": 830}},
    {"id": "ORDERS-9984", "title": "Orders scenario 9984", "data": {"sku": "SKU9984", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9984@example.com", "threshold": 840}},
    {"id": "ORDERS-9985", "title": "Orders scenario 9985", "data": {"sku": "SKU9985", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9985@example.com", "threshold": 850}},
    {"id": "ORDERS-9986", "title": "Orders scenario 9986", "data": {"sku": "SKU9986", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9986@example.com", "threshold": 860}},
    {"id": "ORDERS-9987", "title": "Orders scenario 9987", "data": {"sku": "SKU9987", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9987@example.com", "threshold": 870}},
    {"id": "ORDERS-9988", "title": "Orders scenario 9988", "data": {"sku": "SKU9988", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9988@example.com", "threshold": 880}},
    {"id": "ORDERS-9989", "title": "Orders scenario 9989", "data": {"sku": "SKU9989", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9989@example.com", "threshold": 890}},
    {"id": "ORDERS-9990", "title": "Orders scenario 9990", "data": {"sku": "SKU9990", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9990@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
