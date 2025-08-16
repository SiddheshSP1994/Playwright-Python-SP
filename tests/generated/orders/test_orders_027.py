import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1581", "title": "Orders scenario 1581", "data": {"sku": "SKU1581", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1581@example.com", "threshold": 810}},
    {"id": "ORDERS-1582", "title": "Orders scenario 1582", "data": {"sku": "SKU1582", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1582@example.com", "threshold": 820}},
    {"id": "ORDERS-1583", "title": "Orders scenario 1583", "data": {"sku": "SKU1583", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1583@example.com", "threshold": 830}},
    {"id": "ORDERS-1584", "title": "Orders scenario 1584", "data": {"sku": "SKU1584", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1584@example.com", "threshold": 840}},
    {"id": "ORDERS-1585", "title": "Orders scenario 1585", "data": {"sku": "SKU1585", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1585@example.com", "threshold": 850}},
    {"id": "ORDERS-1586", "title": "Orders scenario 1586", "data": {"sku": "SKU1586", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1586@example.com", "threshold": 860}},
    {"id": "ORDERS-1587", "title": "Orders scenario 1587", "data": {"sku": "SKU1587", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1587@example.com", "threshold": 870}},
    {"id": "ORDERS-1588", "title": "Orders scenario 1588", "data": {"sku": "SKU1588", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1588@example.com", "threshold": 880}},
    {"id": "ORDERS-1589", "title": "Orders scenario 1589", "data": {"sku": "SKU1589", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1589@example.com", "threshold": 890}},
    {"id": "ORDERS-1590", "title": "Orders scenario 1590", "data": {"sku": "SKU1590", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1590@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
