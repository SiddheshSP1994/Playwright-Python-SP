import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9381", "title": "Orders scenario 9381", "data": {"sku": "SKU9381", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9381@example.com", "threshold": 810}},
    {"id": "ORDERS-9382", "title": "Orders scenario 9382", "data": {"sku": "SKU9382", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9382@example.com", "threshold": 820}},
    {"id": "ORDERS-9383", "title": "Orders scenario 9383", "data": {"sku": "SKU9383", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9383@example.com", "threshold": 830}},
    {"id": "ORDERS-9384", "title": "Orders scenario 9384", "data": {"sku": "SKU9384", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9384@example.com", "threshold": 840}},
    {"id": "ORDERS-9385", "title": "Orders scenario 9385", "data": {"sku": "SKU9385", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9385@example.com", "threshold": 850}},
    {"id": "ORDERS-9386", "title": "Orders scenario 9386", "data": {"sku": "SKU9386", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9386@example.com", "threshold": 860}},
    {"id": "ORDERS-9387", "title": "Orders scenario 9387", "data": {"sku": "SKU9387", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9387@example.com", "threshold": 870}},
    {"id": "ORDERS-9388", "title": "Orders scenario 9388", "data": {"sku": "SKU9388", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9388@example.com", "threshold": 880}},
    {"id": "ORDERS-9389", "title": "Orders scenario 9389", "data": {"sku": "SKU9389", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9389@example.com", "threshold": 890}},
    {"id": "ORDERS-9390", "title": "Orders scenario 9390", "data": {"sku": "SKU9390", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9390@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
