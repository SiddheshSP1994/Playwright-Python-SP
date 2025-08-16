import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6381", "title": "Orders scenario 6381", "data": {"sku": "SKU6381", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6381@example.com", "threshold": 810}},
    {"id": "ORDERS-6382", "title": "Orders scenario 6382", "data": {"sku": "SKU6382", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6382@example.com", "threshold": 820}},
    {"id": "ORDERS-6383", "title": "Orders scenario 6383", "data": {"sku": "SKU6383", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6383@example.com", "threshold": 830}},
    {"id": "ORDERS-6384", "title": "Orders scenario 6384", "data": {"sku": "SKU6384", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6384@example.com", "threshold": 840}},
    {"id": "ORDERS-6385", "title": "Orders scenario 6385", "data": {"sku": "SKU6385", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6385@example.com", "threshold": 850}},
    {"id": "ORDERS-6386", "title": "Orders scenario 6386", "data": {"sku": "SKU6386", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6386@example.com", "threshold": 860}},
    {"id": "ORDERS-6387", "title": "Orders scenario 6387", "data": {"sku": "SKU6387", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6387@example.com", "threshold": 870}},
    {"id": "ORDERS-6388", "title": "Orders scenario 6388", "data": {"sku": "SKU6388", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6388@example.com", "threshold": 880}},
    {"id": "ORDERS-6389", "title": "Orders scenario 6389", "data": {"sku": "SKU6389", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6389@example.com", "threshold": 890}},
    {"id": "ORDERS-6390", "title": "Orders scenario 6390", "data": {"sku": "SKU6390", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6390@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
