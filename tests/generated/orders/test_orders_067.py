import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3981", "title": "Orders scenario 3981", "data": {"sku": "SKU3981", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3981@example.com", "threshold": 810}},
    {"id": "ORDERS-3982", "title": "Orders scenario 3982", "data": {"sku": "SKU3982", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3982@example.com", "threshold": 820}},
    {"id": "ORDERS-3983", "title": "Orders scenario 3983", "data": {"sku": "SKU3983", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3983@example.com", "threshold": 830}},
    {"id": "ORDERS-3984", "title": "Orders scenario 3984", "data": {"sku": "SKU3984", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3984@example.com", "threshold": 840}},
    {"id": "ORDERS-3985", "title": "Orders scenario 3985", "data": {"sku": "SKU3985", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3985@example.com", "threshold": 850}},
    {"id": "ORDERS-3986", "title": "Orders scenario 3986", "data": {"sku": "SKU3986", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3986@example.com", "threshold": 860}},
    {"id": "ORDERS-3987", "title": "Orders scenario 3987", "data": {"sku": "SKU3987", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3987@example.com", "threshold": 870}},
    {"id": "ORDERS-3988", "title": "Orders scenario 3988", "data": {"sku": "SKU3988", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3988@example.com", "threshold": 880}},
    {"id": "ORDERS-3989", "title": "Orders scenario 3989", "data": {"sku": "SKU3989", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3989@example.com", "threshold": 890}},
    {"id": "ORDERS-3990", "title": "Orders scenario 3990", "data": {"sku": "SKU3990", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3990@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
