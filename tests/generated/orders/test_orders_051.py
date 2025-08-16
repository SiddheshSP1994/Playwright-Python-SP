import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3021", "title": "Orders scenario 3021", "data": {"sku": "SKU3021", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3021@example.com", "threshold": 210}},
    {"id": "ORDERS-3022", "title": "Orders scenario 3022", "data": {"sku": "SKU3022", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3022@example.com", "threshold": 220}},
    {"id": "ORDERS-3023", "title": "Orders scenario 3023", "data": {"sku": "SKU3023", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3023@example.com", "threshold": 230}},
    {"id": "ORDERS-3024", "title": "Orders scenario 3024", "data": {"sku": "SKU3024", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3024@example.com", "threshold": 240}},
    {"id": "ORDERS-3025", "title": "Orders scenario 3025", "data": {"sku": "SKU3025", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3025@example.com", "threshold": 250}},
    {"id": "ORDERS-3026", "title": "Orders scenario 3026", "data": {"sku": "SKU3026", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3026@example.com", "threshold": 260}},
    {"id": "ORDERS-3027", "title": "Orders scenario 3027", "data": {"sku": "SKU3027", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3027@example.com", "threshold": 270}},
    {"id": "ORDERS-3028", "title": "Orders scenario 3028", "data": {"sku": "SKU3028", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3028@example.com", "threshold": 280}},
    {"id": "ORDERS-3029", "title": "Orders scenario 3029", "data": {"sku": "SKU3029", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3029@example.com", "threshold": 290}},
    {"id": "ORDERS-3030", "title": "Orders scenario 3030", "data": {"sku": "SKU3030", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3030@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
