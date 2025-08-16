import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9801", "title": "Orders scenario 9801", "data": {"sku": "SKU9801", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9801@example.com", "threshold": 10}},
    {"id": "ORDERS-9802", "title": "Orders scenario 9802", "data": {"sku": "SKU9802", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9802@example.com", "threshold": 20}},
    {"id": "ORDERS-9803", "title": "Orders scenario 9803", "data": {"sku": "SKU9803", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9803@example.com", "threshold": 30}},
    {"id": "ORDERS-9804", "title": "Orders scenario 9804", "data": {"sku": "SKU9804", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9804@example.com", "threshold": 40}},
    {"id": "ORDERS-9805", "title": "Orders scenario 9805", "data": {"sku": "SKU9805", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9805@example.com", "threshold": 50}},
    {"id": "ORDERS-9806", "title": "Orders scenario 9806", "data": {"sku": "SKU9806", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9806@example.com", "threshold": 60}},
    {"id": "ORDERS-9807", "title": "Orders scenario 9807", "data": {"sku": "SKU9807", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9807@example.com", "threshold": 70}},
    {"id": "ORDERS-9808", "title": "Orders scenario 9808", "data": {"sku": "SKU9808", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9808@example.com", "threshold": 80}},
    {"id": "ORDERS-9809", "title": "Orders scenario 9809", "data": {"sku": "SKU9809", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9809@example.com", "threshold": 90}},
    {"id": "ORDERS-9810", "title": "Orders scenario 9810", "data": {"sku": "SKU9810", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9810@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
