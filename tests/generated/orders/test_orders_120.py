import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7161", "title": "Orders scenario 7161", "data": {"sku": "SKU7161", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7161@example.com", "threshold": 610}},
    {"id": "ORDERS-7162", "title": "Orders scenario 7162", "data": {"sku": "SKU7162", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7162@example.com", "threshold": 620}},
    {"id": "ORDERS-7163", "title": "Orders scenario 7163", "data": {"sku": "SKU7163", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7163@example.com", "threshold": 630}},
    {"id": "ORDERS-7164", "title": "Orders scenario 7164", "data": {"sku": "SKU7164", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7164@example.com", "threshold": 640}},
    {"id": "ORDERS-7165", "title": "Orders scenario 7165", "data": {"sku": "SKU7165", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7165@example.com", "threshold": 650}},
    {"id": "ORDERS-7166", "title": "Orders scenario 7166", "data": {"sku": "SKU7166", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7166@example.com", "threshold": 660}},
    {"id": "ORDERS-7167", "title": "Orders scenario 7167", "data": {"sku": "SKU7167", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7167@example.com", "threshold": 670}},
    {"id": "ORDERS-7168", "title": "Orders scenario 7168", "data": {"sku": "SKU7168", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7168@example.com", "threshold": 680}},
    {"id": "ORDERS-7169", "title": "Orders scenario 7169", "data": {"sku": "SKU7169", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7169@example.com", "threshold": 690}},
    {"id": "ORDERS-7170", "title": "Orders scenario 7170", "data": {"sku": "SKU7170", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7170@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
