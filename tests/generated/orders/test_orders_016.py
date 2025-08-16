import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0921", "title": "Orders scenario 921", "data": {"sku": "SKU921", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user921@example.com", "threshold": 210}},
    {"id": "ORDERS-0922", "title": "Orders scenario 922", "data": {"sku": "SKU922", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user922@example.com", "threshold": 220}},
    {"id": "ORDERS-0923", "title": "Orders scenario 923", "data": {"sku": "SKU923", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user923@example.com", "threshold": 230}},
    {"id": "ORDERS-0924", "title": "Orders scenario 924", "data": {"sku": "SKU924", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user924@example.com", "threshold": 240}},
    {"id": "ORDERS-0925", "title": "Orders scenario 925", "data": {"sku": "SKU925", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user925@example.com", "threshold": 250}},
    {"id": "ORDERS-0926", "title": "Orders scenario 926", "data": {"sku": "SKU926", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user926@example.com", "threshold": 260}},
    {"id": "ORDERS-0927", "title": "Orders scenario 927", "data": {"sku": "SKU927", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user927@example.com", "threshold": 270}},
    {"id": "ORDERS-0928", "title": "Orders scenario 928", "data": {"sku": "SKU928", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user928@example.com", "threshold": 280}},
    {"id": "ORDERS-0929", "title": "Orders scenario 929", "data": {"sku": "SKU929", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user929@example.com", "threshold": 290}},
    {"id": "ORDERS-0930", "title": "Orders scenario 930", "data": {"sku": "SKU930", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user930@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
