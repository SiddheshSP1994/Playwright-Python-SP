import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0081", "title": "Orders scenario 81", "data": {"sku": "SKU81", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user81@example.com", "threshold": 810}},
    {"id": "ORDERS-0082", "title": "Orders scenario 82", "data": {"sku": "SKU82", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user82@example.com", "threshold": 820}},
    {"id": "ORDERS-0083", "title": "Orders scenario 83", "data": {"sku": "SKU83", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user83@example.com", "threshold": 830}},
    {"id": "ORDERS-0084", "title": "Orders scenario 84", "data": {"sku": "SKU84", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user84@example.com", "threshold": 840}},
    {"id": "ORDERS-0085", "title": "Orders scenario 85", "data": {"sku": "SKU85", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user85@example.com", "threshold": 850}},
    {"id": "ORDERS-0086", "title": "Orders scenario 86", "data": {"sku": "SKU86", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user86@example.com", "threshold": 860}},
    {"id": "ORDERS-0087", "title": "Orders scenario 87", "data": {"sku": "SKU87", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user87@example.com", "threshold": 870}},
    {"id": "ORDERS-0088", "title": "Orders scenario 88", "data": {"sku": "SKU88", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user88@example.com", "threshold": 880}},
    {"id": "ORDERS-0089", "title": "Orders scenario 89", "data": {"sku": "SKU89", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user89@example.com", "threshold": 890}},
    {"id": "ORDERS-0090", "title": "Orders scenario 90", "data": {"sku": "SKU90", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user90@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
