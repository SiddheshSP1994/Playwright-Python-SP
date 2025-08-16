import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7821", "title": "Orders scenario 7821", "data": {"sku": "SKU7821", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7821@example.com", "threshold": 210}},
    {"id": "ORDERS-7822", "title": "Orders scenario 7822", "data": {"sku": "SKU7822", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7822@example.com", "threshold": 220}},
    {"id": "ORDERS-7823", "title": "Orders scenario 7823", "data": {"sku": "SKU7823", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7823@example.com", "threshold": 230}},
    {"id": "ORDERS-7824", "title": "Orders scenario 7824", "data": {"sku": "SKU7824", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7824@example.com", "threshold": 240}},
    {"id": "ORDERS-7825", "title": "Orders scenario 7825", "data": {"sku": "SKU7825", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7825@example.com", "threshold": 250}},
    {"id": "ORDERS-7826", "title": "Orders scenario 7826", "data": {"sku": "SKU7826", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7826@example.com", "threshold": 260}},
    {"id": "ORDERS-7827", "title": "Orders scenario 7827", "data": {"sku": "SKU7827", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7827@example.com", "threshold": 270}},
    {"id": "ORDERS-7828", "title": "Orders scenario 7828", "data": {"sku": "SKU7828", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7828@example.com", "threshold": 280}},
    {"id": "ORDERS-7829", "title": "Orders scenario 7829", "data": {"sku": "SKU7829", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7829@example.com", "threshold": 290}},
    {"id": "ORDERS-7830", "title": "Orders scenario 7830", "data": {"sku": "SKU7830", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7830@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
