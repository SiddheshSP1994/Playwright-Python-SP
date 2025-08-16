import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6801", "title": "Orders scenario 6801", "data": {"sku": "SKU6801", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6801@example.com", "threshold": 10}},
    {"id": "ORDERS-6802", "title": "Orders scenario 6802", "data": {"sku": "SKU6802", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6802@example.com", "threshold": 20}},
    {"id": "ORDERS-6803", "title": "Orders scenario 6803", "data": {"sku": "SKU6803", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6803@example.com", "threshold": 30}},
    {"id": "ORDERS-6804", "title": "Orders scenario 6804", "data": {"sku": "SKU6804", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6804@example.com", "threshold": 40}},
    {"id": "ORDERS-6805", "title": "Orders scenario 6805", "data": {"sku": "SKU6805", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6805@example.com", "threshold": 50}},
    {"id": "ORDERS-6806", "title": "Orders scenario 6806", "data": {"sku": "SKU6806", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6806@example.com", "threshold": 60}},
    {"id": "ORDERS-6807", "title": "Orders scenario 6807", "data": {"sku": "SKU6807", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6807@example.com", "threshold": 70}},
    {"id": "ORDERS-6808", "title": "Orders scenario 6808", "data": {"sku": "SKU6808", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6808@example.com", "threshold": 80}},
    {"id": "ORDERS-6809", "title": "Orders scenario 6809", "data": {"sku": "SKU6809", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6809@example.com", "threshold": 90}},
    {"id": "ORDERS-6810", "title": "Orders scenario 6810", "data": {"sku": "SKU6810", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6810@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
