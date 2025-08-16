import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6141", "title": "Orders scenario 6141", "data": {"sku": "SKU6141", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6141@example.com", "threshold": 410}},
    {"id": "ORDERS-6142", "title": "Orders scenario 6142", "data": {"sku": "SKU6142", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6142@example.com", "threshold": 420}},
    {"id": "ORDERS-6143", "title": "Orders scenario 6143", "data": {"sku": "SKU6143", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6143@example.com", "threshold": 430}},
    {"id": "ORDERS-6144", "title": "Orders scenario 6144", "data": {"sku": "SKU6144", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6144@example.com", "threshold": 440}},
    {"id": "ORDERS-6145", "title": "Orders scenario 6145", "data": {"sku": "SKU6145", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6145@example.com", "threshold": 450}},
    {"id": "ORDERS-6146", "title": "Orders scenario 6146", "data": {"sku": "SKU6146", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6146@example.com", "threshold": 460}},
    {"id": "ORDERS-6147", "title": "Orders scenario 6147", "data": {"sku": "SKU6147", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6147@example.com", "threshold": 470}},
    {"id": "ORDERS-6148", "title": "Orders scenario 6148", "data": {"sku": "SKU6148", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6148@example.com", "threshold": 480}},
    {"id": "ORDERS-6149", "title": "Orders scenario 6149", "data": {"sku": "SKU6149", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6149@example.com", "threshold": 490}},
    {"id": "ORDERS-6150", "title": "Orders scenario 6150", "data": {"sku": "SKU6150", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6150@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
