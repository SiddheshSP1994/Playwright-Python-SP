import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0021", "title": "Orders scenario 21", "data": {"sku": "SKU21", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user21@example.com", "threshold": 210}},
    {"id": "ORDERS-0022", "title": "Orders scenario 22", "data": {"sku": "SKU22", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user22@example.com", "threshold": 220}},
    {"id": "ORDERS-0023", "title": "Orders scenario 23", "data": {"sku": "SKU23", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user23@example.com", "threshold": 230}},
    {"id": "ORDERS-0024", "title": "Orders scenario 24", "data": {"sku": "SKU24", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user24@example.com", "threshold": 240}},
    {"id": "ORDERS-0025", "title": "Orders scenario 25", "data": {"sku": "SKU25", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user25@example.com", "threshold": 250}},
    {"id": "ORDERS-0026", "title": "Orders scenario 26", "data": {"sku": "SKU26", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user26@example.com", "threshold": 260}},
    {"id": "ORDERS-0027", "title": "Orders scenario 27", "data": {"sku": "SKU27", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user27@example.com", "threshold": 270}},
    {"id": "ORDERS-0028", "title": "Orders scenario 28", "data": {"sku": "SKU28", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user28@example.com", "threshold": 280}},
    {"id": "ORDERS-0029", "title": "Orders scenario 29", "data": {"sku": "SKU29", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user29@example.com", "threshold": 290}},
    {"id": "ORDERS-0030", "title": "Orders scenario 30", "data": {"sku": "SKU30", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user30@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
