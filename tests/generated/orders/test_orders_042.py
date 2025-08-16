import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2481", "title": "Orders scenario 2481", "data": {"sku": "SKU2481", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2481@example.com", "threshold": 810}},
    {"id": "ORDERS-2482", "title": "Orders scenario 2482", "data": {"sku": "SKU2482", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2482@example.com", "threshold": 820}},
    {"id": "ORDERS-2483", "title": "Orders scenario 2483", "data": {"sku": "SKU2483", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2483@example.com", "threshold": 830}},
    {"id": "ORDERS-2484", "title": "Orders scenario 2484", "data": {"sku": "SKU2484", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2484@example.com", "threshold": 840}},
    {"id": "ORDERS-2485", "title": "Orders scenario 2485", "data": {"sku": "SKU2485", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2485@example.com", "threshold": 850}},
    {"id": "ORDERS-2486", "title": "Orders scenario 2486", "data": {"sku": "SKU2486", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2486@example.com", "threshold": 860}},
    {"id": "ORDERS-2487", "title": "Orders scenario 2487", "data": {"sku": "SKU2487", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2487@example.com", "threshold": 870}},
    {"id": "ORDERS-2488", "title": "Orders scenario 2488", "data": {"sku": "SKU2488", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2488@example.com", "threshold": 880}},
    {"id": "ORDERS-2489", "title": "Orders scenario 2489", "data": {"sku": "SKU2489", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2489@example.com", "threshold": 890}},
    {"id": "ORDERS-2490", "title": "Orders scenario 2490", "data": {"sku": "SKU2490", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2490@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
