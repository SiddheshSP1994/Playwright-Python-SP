import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9141", "title": "Orders scenario 9141", "data": {"sku": "SKU9141", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9141@example.com", "threshold": 410}},
    {"id": "ORDERS-9142", "title": "Orders scenario 9142", "data": {"sku": "SKU9142", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9142@example.com", "threshold": 420}},
    {"id": "ORDERS-9143", "title": "Orders scenario 9143", "data": {"sku": "SKU9143", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9143@example.com", "threshold": 430}},
    {"id": "ORDERS-9144", "title": "Orders scenario 9144", "data": {"sku": "SKU9144", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9144@example.com", "threshold": 440}},
    {"id": "ORDERS-9145", "title": "Orders scenario 9145", "data": {"sku": "SKU9145", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9145@example.com", "threshold": 450}},
    {"id": "ORDERS-9146", "title": "Orders scenario 9146", "data": {"sku": "SKU9146", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9146@example.com", "threshold": 460}},
    {"id": "ORDERS-9147", "title": "Orders scenario 9147", "data": {"sku": "SKU9147", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9147@example.com", "threshold": 470}},
    {"id": "ORDERS-9148", "title": "Orders scenario 9148", "data": {"sku": "SKU9148", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9148@example.com", "threshold": 480}},
    {"id": "ORDERS-9149", "title": "Orders scenario 9149", "data": {"sku": "SKU9149", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9149@example.com", "threshold": 490}},
    {"id": "ORDERS-9150", "title": "Orders scenario 9150", "data": {"sku": "SKU9150", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9150@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
