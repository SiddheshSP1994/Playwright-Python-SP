import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7281", "title": "Orders scenario 7281", "data": {"sku": "SKU7281", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7281@example.com", "threshold": 810}},
    {"id": "ORDERS-7282", "title": "Orders scenario 7282", "data": {"sku": "SKU7282", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7282@example.com", "threshold": 820}},
    {"id": "ORDERS-7283", "title": "Orders scenario 7283", "data": {"sku": "SKU7283", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7283@example.com", "threshold": 830}},
    {"id": "ORDERS-7284", "title": "Orders scenario 7284", "data": {"sku": "SKU7284", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7284@example.com", "threshold": 840}},
    {"id": "ORDERS-7285", "title": "Orders scenario 7285", "data": {"sku": "SKU7285", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7285@example.com", "threshold": 850}},
    {"id": "ORDERS-7286", "title": "Orders scenario 7286", "data": {"sku": "SKU7286", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7286@example.com", "threshold": 860}},
    {"id": "ORDERS-7287", "title": "Orders scenario 7287", "data": {"sku": "SKU7287", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7287@example.com", "threshold": 870}},
    {"id": "ORDERS-7288", "title": "Orders scenario 7288", "data": {"sku": "SKU7288", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7288@example.com", "threshold": 880}},
    {"id": "ORDERS-7289", "title": "Orders scenario 7289", "data": {"sku": "SKU7289", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7289@example.com", "threshold": 890}},
    {"id": "ORDERS-7290", "title": "Orders scenario 7290", "data": {"sku": "SKU7290", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7290@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
