import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0381", "title": "Orders scenario 381", "data": {"sku": "SKU381", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user381@example.com", "threshold": 810}},
    {"id": "ORDERS-0382", "title": "Orders scenario 382", "data": {"sku": "SKU382", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user382@example.com", "threshold": 820}},
    {"id": "ORDERS-0383", "title": "Orders scenario 383", "data": {"sku": "SKU383", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user383@example.com", "threshold": 830}},
    {"id": "ORDERS-0384", "title": "Orders scenario 384", "data": {"sku": "SKU384", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user384@example.com", "threshold": 840}},
    {"id": "ORDERS-0385", "title": "Orders scenario 385", "data": {"sku": "SKU385", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user385@example.com", "threshold": 850}},
    {"id": "ORDERS-0386", "title": "Orders scenario 386", "data": {"sku": "SKU386", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user386@example.com", "threshold": 860}},
    {"id": "ORDERS-0387", "title": "Orders scenario 387", "data": {"sku": "SKU387", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user387@example.com", "threshold": 870}},
    {"id": "ORDERS-0388", "title": "Orders scenario 388", "data": {"sku": "SKU388", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user388@example.com", "threshold": 880}},
    {"id": "ORDERS-0389", "title": "Orders scenario 389", "data": {"sku": "SKU389", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user389@example.com", "threshold": 890}},
    {"id": "ORDERS-0390", "title": "Orders scenario 390", "data": {"sku": "SKU390", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user390@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
