import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8481", "title": "Orders scenario 8481", "data": {"sku": "SKU8481", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8481@example.com", "threshold": 810}},
    {"id": "ORDERS-8482", "title": "Orders scenario 8482", "data": {"sku": "SKU8482", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8482@example.com", "threshold": 820}},
    {"id": "ORDERS-8483", "title": "Orders scenario 8483", "data": {"sku": "SKU8483", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8483@example.com", "threshold": 830}},
    {"id": "ORDERS-8484", "title": "Orders scenario 8484", "data": {"sku": "SKU8484", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8484@example.com", "threshold": 840}},
    {"id": "ORDERS-8485", "title": "Orders scenario 8485", "data": {"sku": "SKU8485", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8485@example.com", "threshold": 850}},
    {"id": "ORDERS-8486", "title": "Orders scenario 8486", "data": {"sku": "SKU8486", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8486@example.com", "threshold": 860}},
    {"id": "ORDERS-8487", "title": "Orders scenario 8487", "data": {"sku": "SKU8487", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8487@example.com", "threshold": 870}},
    {"id": "ORDERS-8488", "title": "Orders scenario 8488", "data": {"sku": "SKU8488", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8488@example.com", "threshold": 880}},
    {"id": "ORDERS-8489", "title": "Orders scenario 8489", "data": {"sku": "SKU8489", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8489@example.com", "threshold": 890}},
    {"id": "ORDERS-8490", "title": "Orders scenario 8490", "data": {"sku": "SKU8490", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8490@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
