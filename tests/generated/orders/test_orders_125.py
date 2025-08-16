import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7461", "title": "Orders scenario 7461", "data": {"sku": "SKU7461", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7461@example.com", "threshold": 610}},
    {"id": "ORDERS-7462", "title": "Orders scenario 7462", "data": {"sku": "SKU7462", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7462@example.com", "threshold": 620}},
    {"id": "ORDERS-7463", "title": "Orders scenario 7463", "data": {"sku": "SKU7463", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7463@example.com", "threshold": 630}},
    {"id": "ORDERS-7464", "title": "Orders scenario 7464", "data": {"sku": "SKU7464", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7464@example.com", "threshold": 640}},
    {"id": "ORDERS-7465", "title": "Orders scenario 7465", "data": {"sku": "SKU7465", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7465@example.com", "threshold": 650}},
    {"id": "ORDERS-7466", "title": "Orders scenario 7466", "data": {"sku": "SKU7466", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7466@example.com", "threshold": 660}},
    {"id": "ORDERS-7467", "title": "Orders scenario 7467", "data": {"sku": "SKU7467", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7467@example.com", "threshold": 670}},
    {"id": "ORDERS-7468", "title": "Orders scenario 7468", "data": {"sku": "SKU7468", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7468@example.com", "threshold": 680}},
    {"id": "ORDERS-7469", "title": "Orders scenario 7469", "data": {"sku": "SKU7469", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7469@example.com", "threshold": 690}},
    {"id": "ORDERS-7470", "title": "Orders scenario 7470", "data": {"sku": "SKU7470", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7470@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
