import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3501", "title": "Orders scenario 3501", "data": {"sku": "SKU3501", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3501@example.com", "threshold": 10}},
    {"id": "ORDERS-3502", "title": "Orders scenario 3502", "data": {"sku": "SKU3502", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3502@example.com", "threshold": 20}},
    {"id": "ORDERS-3503", "title": "Orders scenario 3503", "data": {"sku": "SKU3503", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3503@example.com", "threshold": 30}},
    {"id": "ORDERS-3504", "title": "Orders scenario 3504", "data": {"sku": "SKU3504", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3504@example.com", "threshold": 40}},
    {"id": "ORDERS-3505", "title": "Orders scenario 3505", "data": {"sku": "SKU3505", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3505@example.com", "threshold": 50}},
    {"id": "ORDERS-3506", "title": "Orders scenario 3506", "data": {"sku": "SKU3506", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3506@example.com", "threshold": 60}},
    {"id": "ORDERS-3507", "title": "Orders scenario 3507", "data": {"sku": "SKU3507", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3507@example.com", "threshold": 70}},
    {"id": "ORDERS-3508", "title": "Orders scenario 3508", "data": {"sku": "SKU3508", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3508@example.com", "threshold": 80}},
    {"id": "ORDERS-3509", "title": "Orders scenario 3509", "data": {"sku": "SKU3509", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3509@example.com", "threshold": 90}},
    {"id": "ORDERS-3510", "title": "Orders scenario 3510", "data": {"sku": "SKU3510", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3510@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
