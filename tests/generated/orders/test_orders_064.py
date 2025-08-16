import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3801", "title": "Orders scenario 3801", "data": {"sku": "SKU3801", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3801@example.com", "threshold": 10}},
    {"id": "ORDERS-3802", "title": "Orders scenario 3802", "data": {"sku": "SKU3802", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3802@example.com", "threshold": 20}},
    {"id": "ORDERS-3803", "title": "Orders scenario 3803", "data": {"sku": "SKU3803", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3803@example.com", "threshold": 30}},
    {"id": "ORDERS-3804", "title": "Orders scenario 3804", "data": {"sku": "SKU3804", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3804@example.com", "threshold": 40}},
    {"id": "ORDERS-3805", "title": "Orders scenario 3805", "data": {"sku": "SKU3805", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3805@example.com", "threshold": 50}},
    {"id": "ORDERS-3806", "title": "Orders scenario 3806", "data": {"sku": "SKU3806", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3806@example.com", "threshold": 60}},
    {"id": "ORDERS-3807", "title": "Orders scenario 3807", "data": {"sku": "SKU3807", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3807@example.com", "threshold": 70}},
    {"id": "ORDERS-3808", "title": "Orders scenario 3808", "data": {"sku": "SKU3808", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3808@example.com", "threshold": 80}},
    {"id": "ORDERS-3809", "title": "Orders scenario 3809", "data": {"sku": "SKU3809", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3809@example.com", "threshold": 90}},
    {"id": "ORDERS-3810", "title": "Orders scenario 3810", "data": {"sku": "SKU3810", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3810@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
