import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7881", "title": "Orders scenario 7881", "data": {"sku": "SKU7881", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7881@example.com", "threshold": 810}},
    {"id": "ORDERS-7882", "title": "Orders scenario 7882", "data": {"sku": "SKU7882", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7882@example.com", "threshold": 820}},
    {"id": "ORDERS-7883", "title": "Orders scenario 7883", "data": {"sku": "SKU7883", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7883@example.com", "threshold": 830}},
    {"id": "ORDERS-7884", "title": "Orders scenario 7884", "data": {"sku": "SKU7884", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7884@example.com", "threshold": 840}},
    {"id": "ORDERS-7885", "title": "Orders scenario 7885", "data": {"sku": "SKU7885", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7885@example.com", "threshold": 850}},
    {"id": "ORDERS-7886", "title": "Orders scenario 7886", "data": {"sku": "SKU7886", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7886@example.com", "threshold": 860}},
    {"id": "ORDERS-7887", "title": "Orders scenario 7887", "data": {"sku": "SKU7887", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7887@example.com", "threshold": 870}},
    {"id": "ORDERS-7888", "title": "Orders scenario 7888", "data": {"sku": "SKU7888", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7888@example.com", "threshold": 880}},
    {"id": "ORDERS-7889", "title": "Orders scenario 7889", "data": {"sku": "SKU7889", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7889@example.com", "threshold": 890}},
    {"id": "ORDERS-7890", "title": "Orders scenario 7890", "data": {"sku": "SKU7890", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7890@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
