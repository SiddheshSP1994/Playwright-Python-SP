import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5781", "title": "Orders scenario 5781", "data": {"sku": "SKU5781", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5781@example.com", "threshold": 810}},
    {"id": "ORDERS-5782", "title": "Orders scenario 5782", "data": {"sku": "SKU5782", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5782@example.com", "threshold": 820}},
    {"id": "ORDERS-5783", "title": "Orders scenario 5783", "data": {"sku": "SKU5783", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5783@example.com", "threshold": 830}},
    {"id": "ORDERS-5784", "title": "Orders scenario 5784", "data": {"sku": "SKU5784", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5784@example.com", "threshold": 840}},
    {"id": "ORDERS-5785", "title": "Orders scenario 5785", "data": {"sku": "SKU5785", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5785@example.com", "threshold": 850}},
    {"id": "ORDERS-5786", "title": "Orders scenario 5786", "data": {"sku": "SKU5786", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5786@example.com", "threshold": 860}},
    {"id": "ORDERS-5787", "title": "Orders scenario 5787", "data": {"sku": "SKU5787", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5787@example.com", "threshold": 870}},
    {"id": "ORDERS-5788", "title": "Orders scenario 5788", "data": {"sku": "SKU5788", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5788@example.com", "threshold": 880}},
    {"id": "ORDERS-5789", "title": "Orders scenario 5789", "data": {"sku": "SKU5789", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5789@example.com", "threshold": 890}},
    {"id": "ORDERS-5790", "title": "Orders scenario 5790", "data": {"sku": "SKU5790", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5790@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
