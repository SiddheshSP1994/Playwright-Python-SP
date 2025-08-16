import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3261", "title": "Orders scenario 3261", "data": {"sku": "SKU3261", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3261@example.com", "threshold": 610}},
    {"id": "ORDERS-3262", "title": "Orders scenario 3262", "data": {"sku": "SKU3262", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3262@example.com", "threshold": 620}},
    {"id": "ORDERS-3263", "title": "Orders scenario 3263", "data": {"sku": "SKU3263", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3263@example.com", "threshold": 630}},
    {"id": "ORDERS-3264", "title": "Orders scenario 3264", "data": {"sku": "SKU3264", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3264@example.com", "threshold": 640}},
    {"id": "ORDERS-3265", "title": "Orders scenario 3265", "data": {"sku": "SKU3265", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3265@example.com", "threshold": 650}},
    {"id": "ORDERS-3266", "title": "Orders scenario 3266", "data": {"sku": "SKU3266", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3266@example.com", "threshold": 660}},
    {"id": "ORDERS-3267", "title": "Orders scenario 3267", "data": {"sku": "SKU3267", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3267@example.com", "threshold": 670}},
    {"id": "ORDERS-3268", "title": "Orders scenario 3268", "data": {"sku": "SKU3268", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3268@example.com", "threshold": 680}},
    {"id": "ORDERS-3269", "title": "Orders scenario 3269", "data": {"sku": "SKU3269", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3269@example.com", "threshold": 690}},
    {"id": "ORDERS-3270", "title": "Orders scenario 3270", "data": {"sku": "SKU3270", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3270@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
