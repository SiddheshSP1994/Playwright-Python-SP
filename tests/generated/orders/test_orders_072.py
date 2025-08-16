import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4281", "title": "Orders scenario 4281", "data": {"sku": "SKU4281", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4281@example.com", "threshold": 810}},
    {"id": "ORDERS-4282", "title": "Orders scenario 4282", "data": {"sku": "SKU4282", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4282@example.com", "threshold": 820}},
    {"id": "ORDERS-4283", "title": "Orders scenario 4283", "data": {"sku": "SKU4283", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4283@example.com", "threshold": 830}},
    {"id": "ORDERS-4284", "title": "Orders scenario 4284", "data": {"sku": "SKU4284", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4284@example.com", "threshold": 840}},
    {"id": "ORDERS-4285", "title": "Orders scenario 4285", "data": {"sku": "SKU4285", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4285@example.com", "threshold": 850}},
    {"id": "ORDERS-4286", "title": "Orders scenario 4286", "data": {"sku": "SKU4286", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4286@example.com", "threshold": 860}},
    {"id": "ORDERS-4287", "title": "Orders scenario 4287", "data": {"sku": "SKU4287", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4287@example.com", "threshold": 870}},
    {"id": "ORDERS-4288", "title": "Orders scenario 4288", "data": {"sku": "SKU4288", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4288@example.com", "threshold": 880}},
    {"id": "ORDERS-4289", "title": "Orders scenario 4289", "data": {"sku": "SKU4289", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4289@example.com", "threshold": 890}},
    {"id": "ORDERS-4290", "title": "Orders scenario 4290", "data": {"sku": "SKU4290", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4290@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
