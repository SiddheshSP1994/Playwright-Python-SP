import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7221", "title": "Orders scenario 7221", "data": {"sku": "SKU7221", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7221@example.com", "threshold": 210}},
    {"id": "ORDERS-7222", "title": "Orders scenario 7222", "data": {"sku": "SKU7222", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7222@example.com", "threshold": 220}},
    {"id": "ORDERS-7223", "title": "Orders scenario 7223", "data": {"sku": "SKU7223", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7223@example.com", "threshold": 230}},
    {"id": "ORDERS-7224", "title": "Orders scenario 7224", "data": {"sku": "SKU7224", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7224@example.com", "threshold": 240}},
    {"id": "ORDERS-7225", "title": "Orders scenario 7225", "data": {"sku": "SKU7225", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7225@example.com", "threshold": 250}},
    {"id": "ORDERS-7226", "title": "Orders scenario 7226", "data": {"sku": "SKU7226", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7226@example.com", "threshold": 260}},
    {"id": "ORDERS-7227", "title": "Orders scenario 7227", "data": {"sku": "SKU7227", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7227@example.com", "threshold": 270}},
    {"id": "ORDERS-7228", "title": "Orders scenario 7228", "data": {"sku": "SKU7228", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7228@example.com", "threshold": 280}},
    {"id": "ORDERS-7229", "title": "Orders scenario 7229", "data": {"sku": "SKU7229", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7229@example.com", "threshold": 290}},
    {"id": "ORDERS-7230", "title": "Orders scenario 7230", "data": {"sku": "SKU7230", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7230@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
