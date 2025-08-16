import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3381", "title": "Orders scenario 3381", "data": {"sku": "SKU3381", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3381@example.com", "threshold": 810}},
    {"id": "ORDERS-3382", "title": "Orders scenario 3382", "data": {"sku": "SKU3382", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3382@example.com", "threshold": 820}},
    {"id": "ORDERS-3383", "title": "Orders scenario 3383", "data": {"sku": "SKU3383", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3383@example.com", "threshold": 830}},
    {"id": "ORDERS-3384", "title": "Orders scenario 3384", "data": {"sku": "SKU3384", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3384@example.com", "threshold": 840}},
    {"id": "ORDERS-3385", "title": "Orders scenario 3385", "data": {"sku": "SKU3385", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3385@example.com", "threshold": 850}},
    {"id": "ORDERS-3386", "title": "Orders scenario 3386", "data": {"sku": "SKU3386", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3386@example.com", "threshold": 860}},
    {"id": "ORDERS-3387", "title": "Orders scenario 3387", "data": {"sku": "SKU3387", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3387@example.com", "threshold": 870}},
    {"id": "ORDERS-3388", "title": "Orders scenario 3388", "data": {"sku": "SKU3388", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3388@example.com", "threshold": 880}},
    {"id": "ORDERS-3389", "title": "Orders scenario 3389", "data": {"sku": "SKU3389", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3389@example.com", "threshold": 890}},
    {"id": "ORDERS-3390", "title": "Orders scenario 3390", "data": {"sku": "SKU3390", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3390@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
