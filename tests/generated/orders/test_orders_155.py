import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9261", "title": "Orders scenario 9261", "data": {"sku": "SKU9261", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9261@example.com", "threshold": 610}},
    {"id": "ORDERS-9262", "title": "Orders scenario 9262", "data": {"sku": "SKU9262", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9262@example.com", "threshold": 620}},
    {"id": "ORDERS-9263", "title": "Orders scenario 9263", "data": {"sku": "SKU9263", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9263@example.com", "threshold": 630}},
    {"id": "ORDERS-9264", "title": "Orders scenario 9264", "data": {"sku": "SKU9264", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9264@example.com", "threshold": 640}},
    {"id": "ORDERS-9265", "title": "Orders scenario 9265", "data": {"sku": "SKU9265", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9265@example.com", "threshold": 650}},
    {"id": "ORDERS-9266", "title": "Orders scenario 9266", "data": {"sku": "SKU9266", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9266@example.com", "threshold": 660}},
    {"id": "ORDERS-9267", "title": "Orders scenario 9267", "data": {"sku": "SKU9267", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9267@example.com", "threshold": 670}},
    {"id": "ORDERS-9268", "title": "Orders scenario 9268", "data": {"sku": "SKU9268", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9268@example.com", "threshold": 680}},
    {"id": "ORDERS-9269", "title": "Orders scenario 9269", "data": {"sku": "SKU9269", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9269@example.com", "threshold": 690}},
    {"id": "ORDERS-9270", "title": "Orders scenario 9270", "data": {"sku": "SKU9270", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9270@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
