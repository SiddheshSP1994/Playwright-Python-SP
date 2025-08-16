import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0261", "title": "Orders scenario 261", "data": {"sku": "SKU261", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user261@example.com", "threshold": 610}},
    {"id": "ORDERS-0262", "title": "Orders scenario 262", "data": {"sku": "SKU262", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user262@example.com", "threshold": 620}},
    {"id": "ORDERS-0263", "title": "Orders scenario 263", "data": {"sku": "SKU263", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user263@example.com", "threshold": 630}},
    {"id": "ORDERS-0264", "title": "Orders scenario 264", "data": {"sku": "SKU264", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user264@example.com", "threshold": 640}},
    {"id": "ORDERS-0265", "title": "Orders scenario 265", "data": {"sku": "SKU265", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user265@example.com", "threshold": 650}},
    {"id": "ORDERS-0266", "title": "Orders scenario 266", "data": {"sku": "SKU266", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user266@example.com", "threshold": 660}},
    {"id": "ORDERS-0267", "title": "Orders scenario 267", "data": {"sku": "SKU267", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user267@example.com", "threshold": 670}},
    {"id": "ORDERS-0268", "title": "Orders scenario 268", "data": {"sku": "SKU268", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user268@example.com", "threshold": 680}},
    {"id": "ORDERS-0269", "title": "Orders scenario 269", "data": {"sku": "SKU269", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user269@example.com", "threshold": 690}},
    {"id": "ORDERS-0270", "title": "Orders scenario 270", "data": {"sku": "SKU270", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user270@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
