import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8781", "title": "Orders scenario 8781", "data": {"sku": "SKU8781", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8781@example.com", "threshold": 810}},
    {"id": "ORDERS-8782", "title": "Orders scenario 8782", "data": {"sku": "SKU8782", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8782@example.com", "threshold": 820}},
    {"id": "ORDERS-8783", "title": "Orders scenario 8783", "data": {"sku": "SKU8783", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8783@example.com", "threshold": 830}},
    {"id": "ORDERS-8784", "title": "Orders scenario 8784", "data": {"sku": "SKU8784", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8784@example.com", "threshold": 840}},
    {"id": "ORDERS-8785", "title": "Orders scenario 8785", "data": {"sku": "SKU8785", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8785@example.com", "threshold": 850}},
    {"id": "ORDERS-8786", "title": "Orders scenario 8786", "data": {"sku": "SKU8786", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8786@example.com", "threshold": 860}},
    {"id": "ORDERS-8787", "title": "Orders scenario 8787", "data": {"sku": "SKU8787", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8787@example.com", "threshold": 870}},
    {"id": "ORDERS-8788", "title": "Orders scenario 8788", "data": {"sku": "SKU8788", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8788@example.com", "threshold": 880}},
    {"id": "ORDERS-8789", "title": "Orders scenario 8789", "data": {"sku": "SKU8789", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8789@example.com", "threshold": 890}},
    {"id": "ORDERS-8790", "title": "Orders scenario 8790", "data": {"sku": "SKU8790", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8790@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
