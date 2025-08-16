import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4221", "title": "Orders scenario 4221", "data": {"sku": "SKU4221", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4221@example.com", "threshold": 210}},
    {"id": "ORDERS-4222", "title": "Orders scenario 4222", "data": {"sku": "SKU4222", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4222@example.com", "threshold": 220}},
    {"id": "ORDERS-4223", "title": "Orders scenario 4223", "data": {"sku": "SKU4223", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4223@example.com", "threshold": 230}},
    {"id": "ORDERS-4224", "title": "Orders scenario 4224", "data": {"sku": "SKU4224", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4224@example.com", "threshold": 240}},
    {"id": "ORDERS-4225", "title": "Orders scenario 4225", "data": {"sku": "SKU4225", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4225@example.com", "threshold": 250}},
    {"id": "ORDERS-4226", "title": "Orders scenario 4226", "data": {"sku": "SKU4226", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4226@example.com", "threshold": 260}},
    {"id": "ORDERS-4227", "title": "Orders scenario 4227", "data": {"sku": "SKU4227", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4227@example.com", "threshold": 270}},
    {"id": "ORDERS-4228", "title": "Orders scenario 4228", "data": {"sku": "SKU4228", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4228@example.com", "threshold": 280}},
    {"id": "ORDERS-4229", "title": "Orders scenario 4229", "data": {"sku": "SKU4229", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4229@example.com", "threshold": 290}},
    {"id": "ORDERS-4230", "title": "Orders scenario 4230", "data": {"sku": "SKU4230", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4230@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
