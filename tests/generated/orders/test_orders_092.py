import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5481", "title": "Orders scenario 5481", "data": {"sku": "SKU5481", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5481@example.com", "threshold": 810}},
    {"id": "ORDERS-5482", "title": "Orders scenario 5482", "data": {"sku": "SKU5482", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5482@example.com", "threshold": 820}},
    {"id": "ORDERS-5483", "title": "Orders scenario 5483", "data": {"sku": "SKU5483", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5483@example.com", "threshold": 830}},
    {"id": "ORDERS-5484", "title": "Orders scenario 5484", "data": {"sku": "SKU5484", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5484@example.com", "threshold": 840}},
    {"id": "ORDERS-5485", "title": "Orders scenario 5485", "data": {"sku": "SKU5485", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5485@example.com", "threshold": 850}},
    {"id": "ORDERS-5486", "title": "Orders scenario 5486", "data": {"sku": "SKU5486", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5486@example.com", "threshold": 860}},
    {"id": "ORDERS-5487", "title": "Orders scenario 5487", "data": {"sku": "SKU5487", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5487@example.com", "threshold": 870}},
    {"id": "ORDERS-5488", "title": "Orders scenario 5488", "data": {"sku": "SKU5488", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5488@example.com", "threshold": 880}},
    {"id": "ORDERS-5489", "title": "Orders scenario 5489", "data": {"sku": "SKU5489", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5489@example.com", "threshold": 890}},
    {"id": "ORDERS-5490", "title": "Orders scenario 5490", "data": {"sku": "SKU5490", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5490@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
