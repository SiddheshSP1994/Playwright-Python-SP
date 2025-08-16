import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0501", "title": "Orders scenario 501", "data": {"sku": "SKU501", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user501@example.com", "threshold": 10}},
    {"id": "ORDERS-0502", "title": "Orders scenario 502", "data": {"sku": "SKU502", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user502@example.com", "threshold": 20}},
    {"id": "ORDERS-0503", "title": "Orders scenario 503", "data": {"sku": "SKU503", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user503@example.com", "threshold": 30}},
    {"id": "ORDERS-0504", "title": "Orders scenario 504", "data": {"sku": "SKU504", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user504@example.com", "threshold": 40}},
    {"id": "ORDERS-0505", "title": "Orders scenario 505", "data": {"sku": "SKU505", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user505@example.com", "threshold": 50}},
    {"id": "ORDERS-0506", "title": "Orders scenario 506", "data": {"sku": "SKU506", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user506@example.com", "threshold": 60}},
    {"id": "ORDERS-0507", "title": "Orders scenario 507", "data": {"sku": "SKU507", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user507@example.com", "threshold": 70}},
    {"id": "ORDERS-0508", "title": "Orders scenario 508", "data": {"sku": "SKU508", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user508@example.com", "threshold": 80}},
    {"id": "ORDERS-0509", "title": "Orders scenario 509", "data": {"sku": "SKU509", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user509@example.com", "threshold": 90}},
    {"id": "ORDERS-0510", "title": "Orders scenario 510", "data": {"sku": "SKU510", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user510@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
