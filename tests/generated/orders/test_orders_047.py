import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2781", "title": "Orders scenario 2781", "data": {"sku": "SKU2781", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2781@example.com", "threshold": 810}},
    {"id": "ORDERS-2782", "title": "Orders scenario 2782", "data": {"sku": "SKU2782", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2782@example.com", "threshold": 820}},
    {"id": "ORDERS-2783", "title": "Orders scenario 2783", "data": {"sku": "SKU2783", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2783@example.com", "threshold": 830}},
    {"id": "ORDERS-2784", "title": "Orders scenario 2784", "data": {"sku": "SKU2784", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2784@example.com", "threshold": 840}},
    {"id": "ORDERS-2785", "title": "Orders scenario 2785", "data": {"sku": "SKU2785", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2785@example.com", "threshold": 850}},
    {"id": "ORDERS-2786", "title": "Orders scenario 2786", "data": {"sku": "SKU2786", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2786@example.com", "threshold": 860}},
    {"id": "ORDERS-2787", "title": "Orders scenario 2787", "data": {"sku": "SKU2787", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2787@example.com", "threshold": 870}},
    {"id": "ORDERS-2788", "title": "Orders scenario 2788", "data": {"sku": "SKU2788", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2788@example.com", "threshold": 880}},
    {"id": "ORDERS-2789", "title": "Orders scenario 2789", "data": {"sku": "SKU2789", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2789@example.com", "threshold": 890}},
    {"id": "ORDERS-2790", "title": "Orders scenario 2790", "data": {"sku": "SKU2790", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2790@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
