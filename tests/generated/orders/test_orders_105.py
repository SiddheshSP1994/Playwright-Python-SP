import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6261", "title": "Orders scenario 6261", "data": {"sku": "SKU6261", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6261@example.com", "threshold": 610}},
    {"id": "ORDERS-6262", "title": "Orders scenario 6262", "data": {"sku": "SKU6262", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6262@example.com", "threshold": 620}},
    {"id": "ORDERS-6263", "title": "Orders scenario 6263", "data": {"sku": "SKU6263", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6263@example.com", "threshold": 630}},
    {"id": "ORDERS-6264", "title": "Orders scenario 6264", "data": {"sku": "SKU6264", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6264@example.com", "threshold": 640}},
    {"id": "ORDERS-6265", "title": "Orders scenario 6265", "data": {"sku": "SKU6265", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6265@example.com", "threshold": 650}},
    {"id": "ORDERS-6266", "title": "Orders scenario 6266", "data": {"sku": "SKU6266", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6266@example.com", "threshold": 660}},
    {"id": "ORDERS-6267", "title": "Orders scenario 6267", "data": {"sku": "SKU6267", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6267@example.com", "threshold": 670}},
    {"id": "ORDERS-6268", "title": "Orders scenario 6268", "data": {"sku": "SKU6268", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6268@example.com", "threshold": 680}},
    {"id": "ORDERS-6269", "title": "Orders scenario 6269", "data": {"sku": "SKU6269", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6269@example.com", "threshold": 690}},
    {"id": "ORDERS-6270", "title": "Orders scenario 6270", "data": {"sku": "SKU6270", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6270@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
