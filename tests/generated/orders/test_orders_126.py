import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7521", "title": "Orders scenario 7521", "data": {"sku": "SKU7521", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7521@example.com", "threshold": 210}},
    {"id": "ORDERS-7522", "title": "Orders scenario 7522", "data": {"sku": "SKU7522", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7522@example.com", "threshold": 220}},
    {"id": "ORDERS-7523", "title": "Orders scenario 7523", "data": {"sku": "SKU7523", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7523@example.com", "threshold": 230}},
    {"id": "ORDERS-7524", "title": "Orders scenario 7524", "data": {"sku": "SKU7524", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7524@example.com", "threshold": 240}},
    {"id": "ORDERS-7525", "title": "Orders scenario 7525", "data": {"sku": "SKU7525", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7525@example.com", "threshold": 250}},
    {"id": "ORDERS-7526", "title": "Orders scenario 7526", "data": {"sku": "SKU7526", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7526@example.com", "threshold": 260}},
    {"id": "ORDERS-7527", "title": "Orders scenario 7527", "data": {"sku": "SKU7527", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7527@example.com", "threshold": 270}},
    {"id": "ORDERS-7528", "title": "Orders scenario 7528", "data": {"sku": "SKU7528", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7528@example.com", "threshold": 280}},
    {"id": "ORDERS-7529", "title": "Orders scenario 7529", "data": {"sku": "SKU7529", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7529@example.com", "threshold": 290}},
    {"id": "ORDERS-7530", "title": "Orders scenario 7530", "data": {"sku": "SKU7530", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7530@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
